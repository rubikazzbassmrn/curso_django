from django.urls import path
from . import views

urlpatterns = [
    #blog paths
    path('', views.blog, name="blog"),
    #category es una cadena de caracteres, pero lo idea es hacerlo entero
    path('category/<int:category_id>/', views.category, name="category")
]