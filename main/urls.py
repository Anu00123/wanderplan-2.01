from django.urls import path
from .  import views


urlpatterns = [
    path('', views.index, name="home" ),
    path('destination', views.destination, name="destination"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),
    path('contact/success/', views.success_page, name='success_page'),
    path('bookings/', views.booking_done, name='booking_done'),  
    path('health/',views.health_check, name='health-check'),
    
]
