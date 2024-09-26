# myapp/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('about/', views.about, name='about'),  # About view
    # Add more URL patterns as needed
]