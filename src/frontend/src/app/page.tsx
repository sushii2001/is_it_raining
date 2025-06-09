'use client';


import { useState, useEffect } from 'react';
import WeatherDisplay from '@/../components/WeatherDisplay';

export default function Home() {
  const [location, setLocation] = useState('Kuala Lumpur');
  const [is_raining, setIsRaining] = useState<boolean | null>(null);
  const [time, setTime] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [latitude, setLatitude] = useState<number | null>(null);
  const [longitude, setLongitude] = useState<number | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`/api/weather?location=${location}`);
        // const response = await fetch(`http://127.0.0.1:8000/weather?location=${location}`);
        const data = await response.json();
        console.log("Data: " , {data})
        if (data.error) {
          setError(data.error);
          setIsRaining(null);
          setTime(null);
          setLatitude(null);
          setLongitude(null);
        } else {
          setLocation(data.location);
          setIsRaining(data.is_raining);
          setTime(data.time);
          setError(null);
          setLatitude(data.latitude);
          setLongitude(data.longitude);
        }
      } catch (err: any) {
        console.error('Error fetching data:', err);
        setError('Failed to fetch weather data.');
        setIsRaining(null);
        setTime(null);
        setLatitude(null);
        setLongitude(null);
      }
    };

    fetchData();
    const intervalId = setInterval(fetchData, 10000);

    return () => clearInterval(intervalId);
  });

  return (
    <div>
      <h1>Is It Raining?</h1>
      <WeatherDisplay
        key={time}  // forces remount on update
        location={location}
        is_raining={is_raining}
        time={time}
        error={error}
        latitude={latitude}
        longitude={longitude}
      />
    </div>
  );
}
