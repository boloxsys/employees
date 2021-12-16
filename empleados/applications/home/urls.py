from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('prueba/', views.PruebaView.as_view(), name="pruebaView"),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view())
]
