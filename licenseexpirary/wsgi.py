"""
WSGI config for licenseexpirary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Try to import Railway database configuration first
try:
    from . import railway_db
    print("Imported Railway database configuration")
except ImportError:
    print("No Railway database configuration found")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'licenseexpirary.settings')

application = get_wsgi_application()
