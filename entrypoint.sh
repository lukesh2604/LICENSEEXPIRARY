#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the server
echo "Starting server..."
gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:${PORT:-8000}
