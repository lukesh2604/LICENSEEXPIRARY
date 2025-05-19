#!/bin/bash
echo "Starting .profile script..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Verifying environment variables..."
echo "Allowed hosts: $ALLOWED_HOSTS"
echo "Debug mode: $DEBUG"
echo "Port: $PORT"
