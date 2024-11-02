from datetime import datetime
import requests
from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return HttpResponse("Hello")


# forecast_url = f"{BASE_URL}/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alert%appid={API_KEY}"

# https://api.openweathermap.org/data/2.5/forecast?lat=44.65&lon=24.2667&appid=65e78526df92d578180ec22aa20ec1ef

# https://api.openweathermap.org/data/2.5/weather?q=Dragasani&appid=65e78526df92d578180ec22aa20ec1ef
# https://api.openweathermap.org/data/2.5/onecall?lat=44.65&lon=24.2667&exclude=current,minutely,hourly,alert%appid=65e78526df92d578180ec22aa20ec1ef

# current_weather_url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}"
# forecast_url = f"{BASE_URL}/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alert&appid={API_KEY}"

def weather(request):
    API_KEY = "65e78526df92d578180ec22aa20ec1ef"
    BASE_URL = "https://api.openweathermap.org/data/2.5"
 
    if request.method == 'POST':
        city = request.POST['city']
        current_weather_url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}"

        weather_response = requests.get(current_weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
    
            lat = weather_data['coord']['lat']
            lon = weather_data['coord']['lon']

            forecast_url = f"{BASE_URL}/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
            forecast_response = requests.get(forecast_url)

            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()

                # Fetch weather
                today = datetime.today()
                weather_data = {
                    'city': city,
                    'temperature': round(weather_data['main']['temp'] - 273.15),
                    'humidity': weather_data['main']['humidity'],
                    'description': weather_data['weather'][0]['description'],
                    'wind': round(weather_data['wind']['speed'] * 3600 / 1000) ,
                    'icon': weather_data["weather"][0]['icon'],

                }
                # Fetch forecast

                ora='00:00:00'
                daily_forecasts = []
                for daily_data in forecast_data['list']:
                    dt_txt = daily_data['dt_txt']
                    

                    if dt_txt.endswith(ora):
                        timestamp = daily_data['dt']
                        daily_forecasts.append({
                            'day': datetime.fromtimestamp(timestamp).strftime('%A'),
                            'temperature': round(daily_data['main']['temp'] - 273.15),
                            # 'description': daily_data['weather'][0]['description']
                        })

            else:
                print("Error forecast")
                return render(request, "weather.html")
        
        else:
            print("Error weather")
            return render(request, "weather.html")

        context = {
            'weather_data': weather_data,
            'daily_forecasts': daily_forecasts,
        }

        return render(request, "weather.html", context)
    
    else:
        return render(request, "weather.html")


def nasa(request):
    return render(request, "nasa.html")

