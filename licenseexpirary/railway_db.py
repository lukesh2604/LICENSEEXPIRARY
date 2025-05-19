# Special database configuration for Railway deployment

import os
import dj_database_url

# Set DATABASE_URL to None if it points to 'db' host
if 'db' in os.environ.get('DATABASE_URL', ''):
    print("WARNING: Overriding invalid DATABASE_URL with Railway-provided one")
    # This will cause dj_database_url to use the Railway-provided DATABASE_URL
    os.environ['DATABASE_URL_OVERRIDE'] = 'True'
