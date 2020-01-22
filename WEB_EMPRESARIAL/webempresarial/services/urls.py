from django.urls import path
from . import views

urlpatterns = [
    #Services paths
    path('services/', views.services, name="services"),
]