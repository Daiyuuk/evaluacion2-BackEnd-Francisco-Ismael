from django.shortcuts import render
from django.http import Http404

CATALOGO = [
    {'slug': 'fusionreborn', 'titulo': 'FusionReborn', 'descripcion': 'Descripción de la película 1', 'calificacion': '5 estrellas', 'imagen': 'FusionReborn.jpg', 'portada': 'portadafusionborn.jpg'},
    {'slug': 'turbo', 'titulo': 'Turbo ', 'descripcion': 'Descripción de la película 2', 'calificacion': '4 estrellas', 'imagen': 'Turbo.jpg', 'portada': 'portadaturbo.jpg'},
    {'slug': 'gato-con-botas', 'titulo': 'Gato con botas', 'descripcion': 'Descripción de la película 3', 'calificacion': '5 estrellas', 'imagen': 'gatoconbotas.jpg', 'portada': 'portadagatoconbotas.jpg'},
    {'slug': 'bolt', 'titulo': 'bolt', 'descripcion': 'Descripción de la película 4', 'calificacion': '3 estrellas', 'imagen': 'bolt.jpg', 'portada': 'portadabolt.jpg'},
    {'slug': 'ratatouille', 'titulo': 'Ratatouille', 'descripcion': 'Descripción de la película 5', 'calificacion': '4 estrellas', 'imagen': 'ratatouille.jpg', 'portada': 'portadaratatouille.jpg'},
    {'slug': 'el-viaje-de-chihiro', 'titulo': 'El viaje de Chihiro', 'descripcion': 'Descripción de la película 6', 'calificacion': '5 estrellas', 'imagen': 'elviajedechihiro.jpg', 'portada': 'portadaelviajedechihiro.jpg'},
]


def inicio(request):
    return render(request, 'inicio.html')


def menu_peliculas(request):
    return render(request, 'menu_peliculas.html', {'catalogos': CATALOGO})

def detalle_pelicula(request, slug):
    pelicula = next((p for p in CATALOGO if p['slug'] == slug), None)
    if pelicula is None:
        raise Http404("La película no existe")
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})
