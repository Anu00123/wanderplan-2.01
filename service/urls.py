from django.urls import path
from .  import views


urlpatterns = [
    path('insurance/', views.Insurance, name='insurance'),
    path('payment/<int:pk>/', views.payment, name='payment'),
    path('success_page',views.success_page, name='success_payment')
]