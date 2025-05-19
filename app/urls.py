from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck/', views.healthcheck, name='healthcheck'),
    path('health/', views.healthcheck, name='health_alt'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('license/new/', views.license_create, name='license_create'),
    path('license/<int:pk>/', views.license_detail, name='license_detail'),
    path('license/<int:pk>/update/', views.license_update, name='license_update'),
    path('license/<int:pk>/delete/', views.license_delete, name='license_delete'),
]