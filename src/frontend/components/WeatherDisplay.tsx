import React from 'react';

interface WeatherDisplayProps {
  location: string;
  is_raining: boolean | null;
  time: string | null;
  error: string | null;
  latitude: number | null;
  longitude: number | null;
}

const WeatherDisplay: React.FC<WeatherDisplayProps> = ({ location, is_raining, time, error, latitude, longitude }) => {
  return (
    <div>
      <h2>Weather in {location}</h2>
      {error ? (
        <p>Error: {error}</p>
      ) : is_raining === null ? (
        <p>Loading...</p>
      ) : is_raining ? (
        <div>
          <p>It is currently raining in {location}.</p>
          <p>Last updated: {time}</p>
        </div>
      ) : (
        <div>
          <p>It is not currently raining in {location}.</p>
          <p>Last updated: {time}</p>
        </div>
      )}
    </div>
  );
};

export default WeatherDisplay;
