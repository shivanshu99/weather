from django.shortcuts import render
from django.http import HttpResponse
import requests, json ,pyowm
import urllib.request
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def index(request):
    if request.method == 'POST':
        city = request.POST['city'] 
        weather=getweather(city)
        return render(request, "index.html",weather)
    else:
        city = "CHENNAI"
        weather=getweather(city)
        return render(request,"index.html",weather)

def base(request): 
    if request.method == 'POST':   
        city = request.POST['city']
        source = urllib.request.urlopen(     
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=9744d321816742d43329496578d36495').read() 
        x = json.loads(source)
        current_temperature = str(round((x["main"]["temp"]-273.15),2))+" °C" ,
        current_pressure = str(x["main"]["pressure"]) +" hPa",
        current_humidiy = str(x["main"]["humidity"])+" %" ,
        weather_description = str(x["weather"][0]["description"] ),   
        wind_speed = str(x["wind"]["speed"])+" mh/h",

        temp = {      
               
            "current_temperature" : current_temperature[0],
            "current_pressure" : current_pressure[0],
            "current_humidiy" : current_humidiy[0],
            "weather_description" : weather_description[0],   
            "wind_speed" : wind_speed[0],
 
        }


        return render(request, "base.html",temp)
    else:
        return render(request,"base.html")

def getweather(city):
    source = urllib.request.urlopen(     
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=9744d321816742d43329496578d36495').read()
    sourc = urllib.request.urlopen(  
            
            'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + '&appid=58b6f7c78582bffab3936dac99c31b25').read()


    y = json.loads(sourc)
    Mon_temperature = str(round(y["list"][0]["temp"]["day"]-273.15))+" °C",
    Tue_temperature = str(round(y["list"][1]["temp"]["day"]-273.15))+" °C",
    Wed_temperature = str(round(y["list"][2]["temp"]["day"]-273.15))+" °C",
    Thu_temperature = str(round(y["list"][3]["temp"]["day"]-273.15))+" °C",
    Fri_temperature = str(round(y["list"][4]["temp"]["day"]-273.15))+" °C",
    Sat_temperature = str(round(y["list"][5]["temp"]["day"]-273.15))+" °C",
    Sun_temperature = str(round(y["list"][6]["temp"]["day"]-273.15))+" °C",
        


    x = json.loads(source)
    name_of_place = x['name'], 
    coordinate_x = str(x['coord']['lon']),
    coordinate_y = str(x["coord"]["lat"]),   
    current_temperature = str(round((x["main"]["temp"]-273.15),2))+" °C" ,
    temp_minimum = str(round((x["main"]["temp_min"]-273.15),2))+" °C",
    temp_maximum = str(round((x["main"]["temp_max"]-273.15),2))+" °C",
    current_pressure = str(x["main"]["pressure"]) +" hPa",
    current_humidiy = str(x["main"]["humidity"])+" %" ,
    weather_description = str(x["weather"][0]["description"] ),   
    wind_speed = str(x["wind"]["speed"])+" mh/h",
        
    weather = {  
           

            "name_of_place" : name_of_place[0],     
            "coordinate_x" : coordinate_x[0],
            "coordinate_y" : coordinate_y[0],   
            "current_temperature" : current_temperature[0],
            "temp_minimum" : temp_minimum[0],
            "temp_maximum" : temp_maximum[0],
            "current_pressure" : current_pressure[0],
            "current_humidiy" : current_humidiy[0],
            "weather_description" : weather_description[0],   
            "wind_speed" : wind_speed[0],
            "Mon_temperature" :Mon_temperature[0],
            "Tue_temperature" :Tue_temperature[0], 
            "Wed_temperature" :Wed_temperature[0], 
            "Thu_temperature" :Thu_temperature[0], 
            "Fri_temperature" :Fri_temperature[0], 
            "Sat_temperature" :Sat_temperature[0], 
            "Sun_temperature" :Sun_temperature[0],  
        }
    return weather
