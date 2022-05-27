import json
from django.shortcuts import render
import requests
from weather.helpers import parseWeather
from django.http import JsonResponse
from django.views.decorators.cache import cache_page


@cache_page(60 * 2)
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=42f1fbf81675a2142233f497487de014'
    city = request.GET.get('city')
    country = request.GET.get('country')
    if city is not None and country is not None:
        weather = requests.get(url.format(request.GET.get('city'))).json()
        if weather['cod'] == 200:
            dic = {'weather': parseWeather(weather)}
            # MARTIN NO ESTOY SEGURO SI EL EJERCICIO PEDIA QUE DEVUELVA SOLO UNA RESPUESTA HTTP O UN TEMPLATE CON LOS DATOS POR LO QUE SE MENCIONA QUE DEBEN PODER SER LEIDOS. DE TODAS FORMAS SI SE DESEA SOLO LA RESPUESTA HTTP PODRIA DESCOMENTARSE LO DE ABAJO
            # response = {
            #     "status": 200,
            #     "data": dic
            # }
            # return JsonResponse(response)
            return render(request, 'weather/index.html', dic)
    return render(request, 'weather/index.html')
