#!/bin/bash

# This is a special script for Railway deployment
echo "================== Railway Helper Script =================="

# Debug environment variables
echo "Checking environment variables:"
if [[ -z "$DATABASE_URL" ]]; then
  echo "WARNING: DATABASE_URL is not set!"
else  
  # Check if DATABASE_URL contains 'db' hostname
  if [[ "$DATABASE_URL" == *"@db:"* ]]; then
    echo "WARNING: DATABASE_URL contains invalid 'db' hostname!"
    echo "This will not work on Railway. Unsetting DATABASE_URL to use Railway's default."
    unset DATABASE_URL
  else
    echo "DATABASE_URL is set and appears valid (value hidden for security)"
  fi
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
