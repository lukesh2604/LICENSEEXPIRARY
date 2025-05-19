#!/bin/bash

# This script is specifically for Railway deployment

# Apply database migrations
echo "Running migrations..."
python manage.py migrate

# Determine the port
PORT=${PORT:-8000}
echo "Starting server on port $PORT"

# Start gunicorn
exec gunicorn licenseexpirary.wsgi:application --bind "0.0.0.0:$PORT"
