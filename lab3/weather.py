import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '2a82c7f220cc453fb52225104251002'  

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    base_url = "http://api.weatherapi.com/v1/current.json"
    url = f"{base_url}?key={WEATHER_API_KEY}&q={city}"

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(url)
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. 
        data = response.json()

        #Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        current_temp = data['current']['temp_f']    
        feels_like_temp = data['current']['feelslike_f'] 
        weather_condition = data['current']['condition']['text']   
        humidity_percentage = data['current']['humidity']
        wind_speed = data['current']['wind_mph']
        wind_direction = data['current']['wind_dir']
        pressure = data['current']['pressure_mb']
        uv_index = data['current']['uv']
        cloud_cover = data['current']['cloud']
        visibility = data['current']['vis_miles']



        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather Data for {city}:")
        print(f"Current Temperature: {current_temp}°F")
        print(f"Feels Like Temperature: {feels_like_temp}°F")
        print(f"Weather Condition: {weather_condition}")
        print(f"Humidity: {humidity_percentage}%")
        print(f"Wind Speed: {wind_speed} mph")
        print(f"Wind Direction: {wind_direction}")
        print(f"Atmospheric Pressure: {pressure} mb")
        print(f"UV Index: {uv_index}")
        print(f"Cloud Cover: {cloud_cover}%")
        print(f"Visibility: {visibility} miles")
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter a city name: ")
    
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
