from django.shortcuts import render




def homefranciscoismael(request):
    catalogo = [{"nombre":"FusionReborn","calificacion":"6.7","genero":"anime"},
                    {"nombre":"Turbo","calificacion":"6.5","genero":"familiar"},
                    {"nombre":"Hoppers","calificacion":"9.8","genero":"familiar"},
                    {"nombre":"Licuadoras ninja vaqueras asesinas","calificacion":"10","genero":"romance"}]
    return render(request, 'homefranciscoismael/homefranciscoismael.html'), {"pelis":catalogo}



def FusionReborn(request):
    datos =[{}]
    return render(request, 'homefranciscoismael/FusionReborn.html')

def Turbo(request):
    return render(request, 'homefranciscoismael/Turbo.html')