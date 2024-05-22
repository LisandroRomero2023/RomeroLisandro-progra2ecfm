from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('analisis/', views.analisis, name='analisis'),
] 
