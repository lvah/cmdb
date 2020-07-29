from django.urls import path
from hostinfo import views

urlpatterns = [
    path('hostscan/', views.hostscan, name='hostscan'),
    path('', views.hostscan, name='hostscan'),
]
