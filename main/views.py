from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
  
from .models import CityWeather 
  
def index(request):
    
    if request.method == 'POST': 
        city = request.POST['city'] 
       
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    +city+ '&appid=b4cbedd0a6afef4c083b2c0c661560f9').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 

        temp_k =str(list_of_data['main']['temp'])
        temp  = round(float(temp_k) - 273.15)
        # data for variable list_of_data 
        data = { 
            "city":str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(temp) +'°C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 

         # Create and save a CityWeather instance with the retrieved data
        city_weather = CityWeather.objects.create(
            city=list_of_data['name'],
            country_code=list_of_data['sys']['country'],
            temp=temp,
            pressure=list_of_data['main']['pressure'],
            humidity=list_of_data['main']['humidity']
        )

        
        
       
    else: 
        data ={} 
    city_data = CityWeather.objects.all().order_by('-timestamp')
    return render(request, "index.html", {'data': data, 'city_data': city_data}) 