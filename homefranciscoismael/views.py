from django.shortcuts import render
from django.http import Http404

CATALOGO = [
    ## ANIME
    {'slug': 'fusionreborn', 'titulo': 'Dragon Ball Z: FusionReborn', 'descripcion': 'Un monstruo malvado nace en el Otro Mundo y solo la fusión de Gokú y Vegeta, dando origen a Gogeta, podrá detenerlo. Una batalla épica por el destino del más alla.', 'calificacion': '4.1/5', 'imagen': 'FusionReborn.jpg', 'portada': 'portadafusionborn.jpg','categoria':'anime'},
    {'slug': 'el-viaje-de-chihiro', 'titulo': 'El viaje de Chihiro', 'descripcion': 'Chihiro es una niña caprichosa que debe adentrarse en un mundo de fantasía para poder salvar a sus padres, convertidos en cerdos.', 'calificacion': '4.9/5', 'imagen': 'elviajedechihiro.jpg', 'portada': 'portadaelviajedechihiro.jpg','categoria':'anime'},
    {'slug':'dbsBroly','titulo':'Dragon Ball Super: Broly', 'descripcion':'En esta nueva película del universo Dragon Ball, Goku y Vegeta se encuentran con Broly, un guerrero Saiyajin que no se parece en nada a cualquier otro luchador con el que se hayan enfrentado antes.', 'calificacion':'4.5/5', 'imagen':'DBSBroly.jpg', 'portada':'Brolyportada.jpg','categoria':'anime'},
    {'slug':'akira','titulo':'Akira', 'descripcion':'Un proyecto militar secreto pone en peligro a Neo-Tokio cuando convierte a un miembro de una pandilla de motociclistas en un psicópata devastador que solo puede ser detenido por dos adolescentes y un grupo de psíquicos.', 'calificacion':'5/5', 'imagen':'akira.jpg', 'portada':'akiraportada.jpg','categoria':'anime'},
    {'slug':'princesamononoke','titulo':'La princesa Mononoke', 'descripcion':'En un viaje para descubrir la cura de la maldición de Tatarigami, Ashitaka se encuentra en medio de una guerra entre los dioses del bosque y Tatara, una colonia minera. En esta búsqueda también conoce a San, la Princesa Mononoke.', 'calificacion':'5/5', 'imagen':'mononoke.jpg', 'portada':'portadamononoke.jpg','categoria':'anime'}, 
    {'slug':'yourname','titulo':'Your Name', 'descripcion':'Mitsuha, una adolescente que vive en un pequeño pueblo de Japón, sueña con escapar de su vida cotidiana y conocer una ciudad llena de oportunidades. Taki, un joven que vive en Tokio, lleva una vida completamente diferente. Un día, ambos comienzan a intercambiar cuerpos misteriosamente mientras duermen, despertando cada uno en la vida del otro', 'calificacion':'4.7/5', 'imagen':'yourname.jpg', 'portada':'portadayourname.jpg','categoria':'anime'}, 
    {'slug':'evangelion','titulo':'The End of Evangelion', 'descripcion':'Tras el colapso de NERV, la organización SEELE lanza un ataque militar definitivo para iniciar el Tercer Impacto y fusionar a toda la humanidad. Con Asuka luchando ferozmente y el mundo al borde de la extinción, el destino de la existencia queda en manos de un traumatizado Shinji Ikari.', 'calificacion':'4.5/5', 'imagen':'evangelion.jpg', 'portada':'portadaevangelion.jpg','categoria':'anime'}, 
    {'slug':'silentvoice','titulo':'A Silent Voice', 'descripcion':'Shôko Nishimiya, una estudiante de primaria sorda, empieza a sentir el bullying de sus nuevos compañeros cuando se cambia de colegio. El peor de todos es Ishida Shôya, quien termina por forzar que Nishimiya se cambie de escuela. Años después, Ishida buscará la redención de sus malas acciones.', 'calificacion':'4.5/5', 'imagen':'silentvoice.jpg', 'portada':'portadasilentvoice.jpg','categoria':'anime'}, 
    {'slug':'tapion','titulo':'Dragón Ball Z: El ataque del dragón', 'descripcion':'Los guerreros Z se encuentran en medio de otro conflicto extraterrestre, que incluye a un guerrero con espada llamado Tapion, un mago llamado Hoi y un enorme monstruo llamado Hildegarn.', 'calificacion':'3.7/5', 'imagen':'tapion.jpg', 'portada':'portapion.jpg','categoria':'anime'}, 
    {'slug':'hero','titulo':'Dragon Ball Super: Super Hero', 'descripcion':'La malvada organización de La Patrulla Roja se reúne con nuevos y más poderosos androides, Gamma 1 y Gamma 2, en busca de venganza.', 'calificacion':'3.9/5', 'imagen':'hero.jpg', 'portada':'portadahero.','categoria':'anime'}, 

    ## FAMILIARES
    {'slug': 'turbo', 'titulo': 'Turbo ', 'descripcion': 'Descripción de la película 2', 'calificacion': '4 estrellas', 'imagen': 'Turbo.jpg', 'portada': 'portadaturbo.jpg'},
    {'slug': 'gato-con-botas', 'titulo': 'Gato con botas', 'descripcion': 'Descripción de la película 3', 'calificacion': '5 estrellas', 'imagen': 'gatoconbotas.jpg', 'portada': 'portadagatoconbotas.jpg'},
    {'slug': 'bolt', 'titulo': 'bolt', 'descripcion': 'Descripción de la película 4', 'calificacion': '3 estrellas', 'imagen': 'bolt.jpg', 'portada': 'portadabolt.jpg'},
    {'slug': 'ratatouille', 'titulo': 'Ratatouille', 'descripcion': 'Descripción de la película 5', 'calificacion': '4 estrellas', 'imagen': 'ratatouille.jpg', 'portada': 'portadaratatouille.jpg'},
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
