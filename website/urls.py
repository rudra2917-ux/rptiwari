from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('flour-mills-in-india/', views.flour_mills, name='flour_mills'),
    path('contact/', views.contact, name='contact'),
]
