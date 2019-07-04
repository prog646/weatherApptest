import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect

# Create your views here.


def index (request):
    appid = '69dbf57c4228fb249368038366c9fa86'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/")

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"] [0] ["icon"]
        }

        all_cities.append(city_info)


    context = {'all_info' : all_cities, 'form' : form}
    return render (request, 'weather/index.html', context)


def delete(request, id):
    try:
        cities = CityForm(id)
        cities.delete(id)
        return HttpResponseRedirect("index")
    except City.DoesNotExist:
        return 'Ошибка'
