from django.contrib import admin
from .models import License

# Register your models here.
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'expiry_date', 'is_expired', 'created_at')
    list_filter = ('expiry_date', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('expiry_date',)
