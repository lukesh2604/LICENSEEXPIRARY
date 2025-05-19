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

# Run migrations during build (for testing - in production, run manually after deployment)
RUN python manage.py migrate

# Use a bash shell to run the application
# This allows for proper environment variable expansion
CMD bash -c "python manage.py migrate && gunicorn licenseexpirary.wsgi:application --bind 0.0.0.0:\${PORT:-8000}"
