from django.urls import path
from . import views

urlpatterns = [
    path('distance/', views.distance, name='address_distance')
]