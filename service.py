import os
import requests

class OpenWeatherService:
    """
    A service class to interact with the OpenWeather API.
    It provides methods to get the current weather of a given city.
    """
    API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather_data(self, city_name: str) -> dict:
        """
        Fetch the current weather details for a given city.

        Args:
            city_name (str): The name of the city to fetch weather for.

        Returns:
            dict: A dictionary containing weather details.
                  If city not found or an error occurs, it returns an empty dict.
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "imperial"  # Using imperial units for temperature (Fahrenheit)
        }

        try:
            response = requests.get(self.API_BASE_URL, params=params)
            data = response.json()
           
            return {
                "city": data.get("name"),
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        except (requests.RequestException, KeyError):
            # Any network or data parsing error leads to an empty dictionary.
            return {}