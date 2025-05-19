# Railway Deployment Guide for License Expiry Tracker

This guide provides step-by-step instructions for deploying the License Expiry Tracker application on Railway.

## Prerequisites

1. A [Railway account](https://railway.app/)
2. [Git](https://git-scm.com/) installed on your local machine
3. A GitHub account (recommended)

## Deployment Steps

### 1. Prepare Your Project for Version Control

```bash
# Initialize git repository (if not already done)
cd /path/to/licenseexpirary
git init
git add .
git commit -m "Initial commit for deployment"
```

### 2. Create a GitHub Repository (Recommended)

- Go to [GitHub](https://github.com/) and create a new repository
- Follow GitHub's instructions to push your existing repository:

```bash
git remote add origin https://github.com/yourusername/license-expiry-tracker.git
git branch -M main
git push -u origin main
```

### 3. Deploy to Railway using the Railway CLI

#### Install Railway CLI
```bash
npm i -g @railway/cli
```

#### Login to Railway
```bash
railway login
```

#### Initialize Railway Project
```bash
railway init
```

#### Deploy Your Project
```bash
railway up
```

### 4. Deploy to Railway using the Web Interface

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Select your repository
5. Configure the deployment:
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command: `gunicorn licenseexpirary.wsgi`

### 5. Configure Environment Variables

Set the following environment variables in your Railway project:

- `DEBUG`: False
- `SECRET_KEY`: [Generate a secure random key]
- `ALLOWED_HOSTS`: your-app-name.railway.app
- `DATABASE_URL`: [Railway will auto-configure this]
- `SECURE_SSL_REDIRECT`: True

### 6. Create a Superuser for Admin Access

You need to create a superuser to access the admin interface. In Railway, you can do this through their shell:

1. Go to your project dashboard
2. Click on "Shell" tab
3. Run:
```bash
python manage.py createsuperuser
```

### 7. Set Up a PostgreSQL Database

Railway automatically provisions a PostgreSQL database when you select it as a service:

1. In your project, click "New Service"
2. Choose "Database" → "PostgreSQL"
3. Railway will automatically create and configure the database and set the DATABASE_URL environment variable

### 8. Set Up Media Storage

For production use, you should use a cloud storage service like AWS S3 or Railway's Volumes:

#### Using Railway Volumes
1. Go to your project dashboard
2. Click "Add Volume"
3. Mount the volume to `/app/media`
4. Set environment variable: `MEDIA_ROOT=/app/media`

### 9. Access Your Application

After deployment is complete:

1. Railway will provide a URL to access your application (usually something like `https://your-app-name.railway.app`)
2. Go to `/admin` to access the Django admin interface
3. Log in with your superuser credentials

### 10. Monitor and Maintain

- Check logs in the Railway dashboard for any errors
- Configure additional features like custom domains if needed
- Set up monitoring and alerts for your application

## Troubleshooting

### Common Issues and Solutions

1. **Static files not loading properly**:
   - Check if `STATIC_ROOT` is properly set
   - Make sure `collectstatic` ran without errors

2. **Database migration errors**:
   - Check migration logs in the Railway dashboard
   - Run migrations manually through the Railway shell

3. **Application crashes**:
   - Check logs for details
   - Verify all environment variables are set correctly

4. **Media files not accessible**:
   - Ensure volume is properly mounted
   - Check permissions on the media directory

For more help, consult the [Railway documentation](https://docs.railway.app/) or [Django deployment guide](https://docs.djangoproject.com/en/5.2/howto/deployment/).
