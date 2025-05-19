#!/bin/bash

# This is a special script for Railway deployment
echo "================== Railway Helper Script =================="

# Debug environment variables
echo "Checking environment variables:"
if [[ -z "$DATABASE_URL" ]]; then
  echo "WARNING: DATABASE_URL is not set!"
else  
  echo "DATABASE_URL is set (value hidden for security)"
fi

echo "PORT=$PORT"

# Make sure no .env file exists with conflicting settings
if [[ -f .env ]]; then
  echo "Found .env file, removing to avoid conflicts with Railway environment variables"
  rm -f .env
fi

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Start the server
echo "Starting Gunicorn server..."
PORT="${PORT:-8000}"
echo "Using port: $PORT"
exec gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:$PORT
