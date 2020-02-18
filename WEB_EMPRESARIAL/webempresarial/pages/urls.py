from django.urls import path
from . import views

urlpatterns = [
    #category es una cadena de caracteres, pero lo idea es hacerlo entero
    path('<int:page_id>/', views.page, name="page")
]