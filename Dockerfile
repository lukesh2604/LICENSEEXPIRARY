FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False

# Set work directory
WORKDIR /app

# Install system dependencies including PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create static directory and collect static files
RUN mkdir -p /app/staticfiles && python manage.py collectstatic --noinput

# Do not run migrations during build, they'll be run at startup
# Instead, ensure directories exist and permissions are correct

# Create script to run at container startup
RUN echo '#!/bin/bash\n\
echo "Debugging environment variables:"\n\
echo "DATABASE_URL: $DATABASE_URL"\n\
echo "PORT: $PORT"\n\
echo "Ensuring no .env file with conflicting settings exists:"\n\
rm -f .env\n\
echo "Waiting for PostgreSQL..."\n\
sleep 5\n\
echo "Running migrations..."\n\
python manage.py migrate\n\
echo "Starting Gunicorn..."\n\
PORT="${PORT:-8000}"\n\
echo "Using port: $PORT"\n\
exec gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:$PORT --log-level debug\n\
' > /app/start.sh && chmod +x /app/start.sh

# Use the startup script
CMD ["/app/start.sh"]
