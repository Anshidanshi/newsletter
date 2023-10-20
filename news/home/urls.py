# newsletter/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
    path('unsubscribe/<str:pk>', views.unsubscribe, name='unsubscribe'),
    path('unsubscribe', views.unsubscribed, name='unsubscribed'),
]
