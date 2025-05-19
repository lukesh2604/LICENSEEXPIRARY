from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import License
from .forms import LicenseForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to the page the user was trying to access, or home if none
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            return render(request, 'app/login.html', {'error_message': 'Invalid username or password.'})
    
    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def unauthorized(request):
    return render(request, 'app/unauthorized.html')

@login_required(login_url='login')
def home(request):
    filter_type = request.GET.get('filter', 'all')
    
    if filter_type == 'expires_month':
        today = timezone.now().date()
        thirty_days_later = today + timezone.timedelta(days=30)
        licenses = License.objects.filter(
            expiry_date__gte=today,
            expiry_date__lte=thirty_days_later
        ).order_by('expiry_date')
        filter_title = "Licenses Expiring Within 1 Month"
    elif filter_type == 'expires_three_months':
        today = timezone.now().date()
        ninety_days_later = today + timezone.timedelta(days=90)
        thirty_days_later = today + timezone.timedelta(days=30)
        licenses = License.objects.filter(
            expiry_date__gte=today,
            expiry_date__lte=ninety_days_later
        ).exclude(
            expiry_date__lte=thirty_days_later
        ).order_by('expiry_date')
        filter_title = "Licenses Expiring Within 3 Months"
    else:
        licenses = License.objects.all().order_by('expiry_date')
        filter_title = "All Licenses"
    
    context = {
        'licenses': licenses,
        'filter_type': filter_type,
        'filter_title': filter_title
    }
    return render(request, 'app/home.html', context)

@login_required(login_url='login')
def license_create(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST, request.FILES)
        if form.is_valid():
            license = form.save()
            messages.success(request, 'License information saved successfully!')
            return redirect('license_detail', pk=license.pk)
    else:
        form = LicenseForm()
    
    return render(request, 'app/license_form.html', {'form': form, 'action': 'Create'})

@login_required(login_url='login')
def license_detail(request, pk):
    license = get_object_or_404(License, pk=pk)
    return render(request, 'app/license_detail.html', {'license': license})

@login_required(login_url='login')
def license_update(request, pk):
    license = get_object_or_404(License, pk=pk)
    
    if request.method == 'POST':
        form = LicenseForm(request.POST, request.FILES, instance=license)
        if form.is_valid():
            form.save()
            messages.success(request, 'License information updated successfully!')
            return redirect('license_detail', pk=license.pk)
    else:
        form = LicenseForm(instance=license)
    
    return render(request, 'app/license_form.html', {'form': form, 'license': license, 'action': 'Update'})

@login_required(login_url='login')
def license_delete(request, pk):
    license = get_object_or_404(License, pk=pk)
    
    if request.method == 'POST':
        license.delete()
        messages.success(request, 'License information deleted successfully!')
        return redirect('home')
        
    return render(request, 'app/license_confirm_delete.html', {'license': license})