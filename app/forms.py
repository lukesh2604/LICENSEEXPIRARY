from django import forms
from .models import License

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['first_name', 'last_name', 'email', 'expiry_date', 'front_photo', 'back_photo']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def clean_expiry_date(self):
        # Add any custom validation for expiry date if needed
        expiry_date = self.cleaned_data.get('expiry_date')
        return expiry_date
