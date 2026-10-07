from django.urls import path
from . import views

app_name = 'homefranciscoismael'

urlpatterns = [
    path('', views.homefranciscoismael, name='homefranciscoismael'),
    path('fusionreborn/', views.FusionReborn, name='fusionreborn')
]