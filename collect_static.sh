#!/bin/bash
# Script to collect static files and prepare for deployment

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Static files collection completed!"
