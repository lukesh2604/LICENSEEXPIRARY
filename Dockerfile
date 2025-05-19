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

# Create a script to run migrations and start the server
COPY ./entrypoint.sh /app/entrypoint.sh
# Ensure proper line endings and execution permissions
RUN sed -i 's/\r$//' /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Run entrypoint script
CMD ["/bin/bash", "/app/entrypoint.sh"]

# Alternative CMD in case entrypoint script fails
# CMD gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:$PORT
