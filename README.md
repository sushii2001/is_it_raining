# Rain Tracker

This application tracks the rain status for a specified location and notifies the user if it starts to rain.

## Prerequisites

*   Python 3.6+
*   pip

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd isit_raining
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Python script:

    ```bash
    python src/main.py
    ```

2.  Open `index.html` in a browser.

## Configuration

*   Modify the `locationName` variable in `index.html` to specify the location to track.

## Debugging

*   Radar images are saved to the `radar_images` directory.

## API Endpoint

The Python script provides an API endpoint at `/rain` that returns the rain status in JSON format.

*   URL: `http://localhost:5000/rain?location=<location>`
*   Method: GET
*   Parameters:
    *   `location`: The location to check for rain.

## Example Response

```json
{
    "location": "Pulau Tikus, Penang",
    "latitude": 5.4318216,
    "longitude": 100.3117683,
    "is_raining": false
}
```

## Testing

To run the tests, use the following commands:

### Backend

```bash
python -m unittest tests/backend/test_main.py
```

### Frontend

```bash
cd tests/frontend
npx jest
```
