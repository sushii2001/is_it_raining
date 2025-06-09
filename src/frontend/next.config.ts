import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/weather',
        destination: 'http://127.0.0.1:8000/weather',
      },
    ];
  },
};

export default nextConfig;
