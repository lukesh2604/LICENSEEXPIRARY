from django.db import models
from django.utils import timezone
import os

# Create your models here.
class License(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    expiry_date = models.DateField()
    front_photo = models.FileField(upload_to="license_photos/", blank=True, null=True)
    back_photo = models.FileField(upload_to="license_photos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Expires: {self.expiry_date}"
    
    @property
    def is_expired(self):
        return self.expiry_date < timezone.now().date()
    
    @property
    def expires_within_month(self):
        today = timezone.now().date()
        thirty_days_later = today + timezone.timedelta(days=30)
        return today <= self.expiry_date <= thirty_days_later
    
    @property
    def expires_within_three_months(self):
        today = timezone.now().date()
        ninety_days_later = today + timezone.timedelta(days=90)
        thirty_days_later = today + timezone.timedelta(days=30)
        return today <= self.expiry_date <= ninety_days_later and self.expiry_date > thirty_days_later
    
    def delete(self, *args, **kwargs):
        # Delete the associated files
        if self.front_photo and self.front_photo.path:
            if os.path.isfile(self.front_photo.path):
                os.remove(self.front_photo.path)
        
        if self.back_photo and self.back_photo.path:
            if os.path.isfile(self.back_photo.path):
                os.remove(self.back_photo.path)
        
        super().delete(*args, **kwargs)