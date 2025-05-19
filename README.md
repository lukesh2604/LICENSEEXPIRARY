# License Expiry Tracker

A Django application that helps manage license information and track expiry dates.

## Features

- User authentication system for secure access
- Store license information with optional photo uploads 
- Track license expiry dates
- Filter licenses expiring within 1 month or 3 months
- Mobile responsive interface
- Auto-deletion of image files when license records are deleted

## Technologies Used

- Django 5.2
- Bootstrap 5
- PostgreSQL (in production)
- Gunicorn (WSGI server)
- Whitenoise (Static file serving)

## Deployment

This application is configured for deployment on Railway.app.

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`
