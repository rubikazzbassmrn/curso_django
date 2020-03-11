from django.urls import path
from . import views

urlpatterns = [
    #contact paths
    path('contact/', views.contact, name="contact"),
]