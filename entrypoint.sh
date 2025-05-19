#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the server
echo "Starting server..."
# Check if PORT is set, otherwise default to 8000
if [ -z "$PORT" ]; then
    PORT=8000
fi
echo "Using port: $PORT"
gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:$PORT
