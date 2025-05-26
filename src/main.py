import requests
from PIL import Image
from io import BytesIO
import numpy as np
import math
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_lat_lon(location_name):
    """Get latitude and longitude from a location name using Nominatim API"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location_name,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "RainChecker/1.0 (your_email@example.com)"
    }
    response = requests.get(url, params=params, headers=headers)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise ValueError(f"Failed to decode JSON response from Nominatim API. Status code: {response.status_code}. Please check the Nominatim API usage policy or try again later.")
    if not data:
        raise ValueError("Location not found.")
    return float(data[0]["lat"]), float(data[0]["lon"])

def deg2num(lat_deg, lon_deg, zoom):
    """Convert lat/lon to slippy map tile numbers"""
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile

def check_rain_py(location_name):
    zoom = 10
    try:
        lat, lon = get_lat_lon(location_name)
    except ValueError as e:
        return {"error": str(e)}
    tile_x, tile_y = deg2num(lat, lon, zoom)

    # Get radar data from RainViewer
    rainviewer_url = "https://api.rainviewer.com/public/weather-maps.json"
    try:
        data = requests.get(rainviewer_url).json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Failed to decode JSON response from RainViewer API."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to RainViewer API: {e}"}
    host = data["host"]
    latest_frame = data["radar"]["past"][-1]["path"]

    # Download the radar tile
    tile_url = f"{host}{latest_frame}/256/{zoom}/{tile_x}/{tile_y}/2/1_1.png"
    try:
        response = requests.get(tile_url)
        image = Image.open(BytesIO(response.content)).convert("RGBA")
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to download radar tile: {e}"}
    except Exception as e:
        return {"error": f"Failed to process radar tile: {e}"}

    # Analyze the radar image
    image_data = np.array(image)
    alpha_channel = image_data[:, :, 3]  # alpha = opacity
    is_raining = bool(np.any(alpha_channel > 0))

    # Save the radar image
    try:
        image.save(f"radar_images/{location_name.replace(' ', '_')}.png")
    except FileNotFoundError:
        import os
        os.makedirs("radar_images", exist_ok=True)
        image.save(f"radar_images/{location_name.replace(' ', '_')}.png")


    return {
        "location": location_name,
        "latitude": lat,
        "longitude": lon,
        "is_raining": is_raining,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route('/rain')
def rain_route():
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location parameter is required."}), 400
    result = check_rain_py(location)
    print(f"API Response: {result}")
    return jsonify(result), 200, {'Content-Type': 'application/json'}

# Remove the following lines
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
