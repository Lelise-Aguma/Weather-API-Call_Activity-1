import requests

class OpenWeatherService:
    """
    A service class to interact with the OpenWeather API and get current weather data for a city.
    """
    API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather_data(self, city_name: str) -> dict:
        """
        Get the current weather for a city.

        Args:
            city_name (str): The name of the city.

        Returns:
            dict: Weather details, or an empty dictionary if there's an error.
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "imperial"  # Temperature in Fahrenheit
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
            # Return an empty dictionary if there's a problem.
            return {}