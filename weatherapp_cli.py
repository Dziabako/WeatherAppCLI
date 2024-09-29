from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')


city = str(input("Enter the city name: ")).capitalize()
forecast_weather_url = "http://api.weatherapi.com/v1/forecast.json"

params = {
    "key": api_key,
    "q": city,
    "days": 2
}

response = requests.get(forecast_weather_url, params=params)
data = response.json()

message = f"""
City: {data['location']['name']}
Region: {data['location']['region']}
Country: {data['location']['country']}
\n
Present Day Forecast:
Current Temperature: {data['current']['temp_c']}°C
Condition: {data['current']['condition']['text']}
Wind: {data['current']['wind_kph']} km/h
Pressure: {data['current']['pressure_mb']} mb
Humidity: {data['current']['humidity']}%
Clouds: {data['current']['cloud']}%
Feelslike: {data['current']['feelslike_c']}°C
\n
Forecast for {data['forecast']['forecastday'][0]['date']}:
Max Temperature: {data['forecast']['forecastday'][0]['day']['maxtemp_c']}°C
Min Temperature: {data['forecast']['forecastday'][0]['day']['mintemp_c']}°C
Condition: {data['forecast']['forecastday'][0]['day']['condition']['text']}
Chance of rain: {data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']}%
\n
Forecast for {data['forecast']['forecastday'][1]['date']}:
Max Temperature: {data['forecast']['forecastday'][1]['day']['maxtemp_c']}°C
Min Temperature: {data['forecast']['forecastday'][1]['day']['mintemp_c']}°C
Condition: {data['forecast']['forecastday'][1]['day']['condition']['text']}
Chance of rain: {data['forecast']['forecastday'][1]['day']['daily_chance_of_rain']}%
"""

print(message)
