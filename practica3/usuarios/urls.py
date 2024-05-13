from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('acceso/', views.acceso, name='acceso'),
    path('<str:username>/', views.perfil, name='perfil'),
    path('subir_archivos/', views.subir_archivos, name='subir_archivos'),
]
    
