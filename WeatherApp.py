#WeatherApp
import requests
aKey = "45a5402888082c4816fc15f0eb1e8737"
baseUrl = "http://api.openweathermap.org/data/2.5/weather"
def fetchWeather(cityName, akey):
    url = baseUrl + '?q=' + cityName + '&appid=' + akey + '&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
def displayWeather(weatherData, cityName):
    if weatherData and weatherData.get('cod') != '404': 
        Main = weatherData['main']
        Weather = weatherData['weather'][0]
        print(f"\nWeather in {cityName}:")
        print(f"Temperature : {Main['temp']}°C")
        print(f"Humidity    : {Main['humidity']}%")
        print(f"Pressure    : {Main['pressure']} hPa")
        print(f"Conditions  : {Weather['description'].capitalize()}")
    else:
        print(f"\nCity '{cityName}' not found. Please check your spelling or try another city.")
cityName = input("Enter the city name: ")
weatherData = fetchWeather(cityName, aKey)
displayWeather(weatherData, cityName)
#<----------------------------THANK YOU !!-------------------------------------------------------------->