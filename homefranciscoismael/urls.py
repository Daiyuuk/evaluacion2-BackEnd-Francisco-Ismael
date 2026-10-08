from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('menu-peliculas/', views.menu_peliculas, name='menu_peliculas'),
    path('pelicula/<slug:slug>/', views.detalle_pelicula, name='detalle_pelicula'),
]