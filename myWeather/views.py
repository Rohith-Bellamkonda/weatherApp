from django.shortcuts import render
import json
import requests

# Create your views here.
def weather(request):
	if "location" in request.GET:
		city  =request.GET.get('location')
		url ="https://api.openweathermap.org/data/2.5/weather?q={}&appid=940f4dd16b76d895ca59cbe0a1a1b9fe".format(city)
		x = requests.get(url)
		y =x.json()
		context = {
		'city': "City Name: {}".format(y['name']),
		'Country': "Country : {}".format(y['sys']['country'] ),
		'Temp': "Temparature: {:.2f} C".format(y['main']['temp']-273.5),
		'Pressure': "Pressure: {}".format(y['main']['pressure']),
		'Humidity': "Humidity: {}".format(y['main']['humidity']),
		'Weather_condition': "Weather Condition: {}".format(y['weather'][0]['description'].upper()),
		}
		return render(request,'home.html',context)
	
		
	return render(request,'home.html')