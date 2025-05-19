from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# For Railway deployment, we need to serve media files even in production
# Note: In a real production environment, you would use a proper storage service
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)