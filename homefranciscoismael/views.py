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
    {'slug': 'turbo', 'titulo': 'Turbo ', 'descripcion': 'Turbo es un caracol de jardín con un sueño imposible: convertirse en el caracol más rápido del mundo. Cuando un extraño accidente le da el poder de la supervelocidad, Turbo intentará cumplir su sueño: ganar las 500 millas de Indianápolis.', 'calificacion': '3.5/5', 'imagen': 'Turbo.jpg', 'portada': 'portadaturbo.jpg','categoria':'familiar'},
    {'slug': 'gato-con-botas', 'titulo': 'Gato con botas', 'descripcion': 'El famoso gato tiene la aventura de su vida cuando une fuerzas con Humpty Dumpty y la gata Kitty para robarse al ganso de los huevos de oro.', 'calificacion': '3.5/5', 'imagen': 'gatoconbotas.jpg', 'portada': 'portadagatoconbotas.jpg','categoria':'familiar'},
    {'slug': 'bolt', 'titulo': 'Bolt', 'descripcion': 'Pensando que él tiene superpoderes de verdad, una estrella canina de un exitoso programa de televisión viaje a través del país, desde Hollywood hasta Nueva York, para rescatar a su dueña, la otra estrella de su espectáculo televisivo.', 'calificacion': '4/5', 'imagen': 'bolt.jpg', 'portada': 'portadabolt.jpg','categoria':'familiar'},
    {'slug': 'ratatouille', 'titulo': 'Ratatouille', 'descripcion': 'La rata Remy viaja a París para cumplir su sueño: convertirse en un gran chef. Aunque las ratas no pueden entrar en las cocinas, se hace amigo de un chico mediocre que trabaja en un restaurante de lujo.', 'calificacion': '4.7/5', 'imagen': 'ratatouille.jpg', 'portada': 'portadarata.webp','categoria':'familiar'},
    {'slug':'hoppers','titulo':'Hoppers','descripcion':'Una amante de los animales se une a su mundo y hace descubrimientos sorprendentes.','calificacion':'4.9/5','imagen':'hoppers.jpg','portada':'portadahoppers.webp','categoria':'familiar'},
    {'slug':'toystory','titulo':'Toy Story','descripcion':'Woody, el juguete favorito de Andy, se siente amenazado por la inesperada llegada de Buzz Lightyear, el guardián del espacio.','calificacion':'5/5','imagen':'toys.jpg','portada':'portadatoys.webp','categoria':'familiar'},
    {'slug':'shrek','titulo':'Shrek','descripcion':'Un ogro llamado Shrek vive en su pantano, pero su preciada soledad se ve súbitamente interrumpida por la invasión de los ruidosos personajes de los cuentos de hadas.','calificacion':'5/5','imagen':'shrek.webp','portada':'portadashrek.jpg','categoria':'familiar'},
    {'slug':'shrek-dos','titulo':'Shrek 2','descripcion':'Los padres de la princesa y reyes de Muy, Muy Lejano invitan a cenar Shrek y Fiona, pero el rey Harold descubre que su yerno es un ogro y acude al Hada Madrina para alejar a Shrek de Fiona.','calificacion':'5/5','imagen':'shrek2.jpg','portada':'portadashrek2.jpg','categoria':'familiar'},
    {'slug':'emoji','titulo':'Emoji la película','descripcion':'Gene, un emoji con varias expresiones, pide a su amigo Hi-5 y al desencriptador Jailbreak que le ayuden a convertirse en un emoji de una cara, como todos sus amigos. Durante su aventura recorren varias aplicaciones y descubren que el teléfono en el que viven está en peligro.','calificacion':'1.7/5','imagen':'emoji.webp','portada':'portadaemoji','categoria':'familiar'},
    {'slug':'minecraft','titulo':'Una Película de Minecraft','descripcion':'Cuatro inadaptados son arrastrados por un portal al Overworld, un misterioso lugar que se nutre de la imaginación. Para volver a casa, tendrán que dominar el terreno mientras se embarcan en una búsqueda con un artesano llamado Steve.','calificacion':'3/5','imagen':'mine.jpg','portada':'portadamine.jpg','categoria':'familiar'},
    
    

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
