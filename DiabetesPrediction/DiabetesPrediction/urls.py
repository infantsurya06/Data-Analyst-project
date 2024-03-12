# Inside your_app/urls.py or project/urls.py
from django.urls import path
from .views import result

urlpatterns = [
    # Other URL patterns
    path('result/', result, name='result'),
]
