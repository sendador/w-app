import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import City
from .forms import CityForm


@login_required(login_url='/login/')
def indexView(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=c5c72205df8a96e917a5ec1560de5406'
    error_message = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name'].capitalize()
            existing_city_count = City.objects.filter(name=new_city, user=request.user).count()
            if existing_city_count == 0:
                response = requests.get(url.format(new_city)).json()
                if response['cod'] == 200:
                    obj = form.save()
                    obj.user = request.user
                    obj.save()
                else:
                    error_message = 'City doesnt exist'
            else:
                error_message = "This city is already added!"
        if error_message:
            message = error_message
            message_class = 'error-msg'
        else:
            message = 'City added successfully'
            message_class = 'successful-msg'

    form = CityForm()
    cities = City.objects.filter(user=request.user)
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class,
    }
    return render(request, 'dashboard.html', context)


def delete_city(self, city_name):
    City.objects.filter(name=city_name).delete()
    return redirect('home')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
