from service import OpenWeatherService


OPENWEATHER_API_KEY='f8294b2888cfffdaf93c2da833b42aec'


def show_weather_details(weather_data_set: dict):
    """
   Display weather details in an easy-to-read format.
    Args:
        weather_data_set (dict): Includes city, temperature, description, humidity, and wind speed.
    """
    if not weather_data_set:
        print("Weather data unavailable. The city name might be incorrect.")
        return

    print(f"\nWeather details for {weather_data_set['city']}:")
    print(f" - Temperature: {weather_data_set['temperature']}°F")
    print(f" - Description: {weather_data_set['description']}")
    print(f" - Humidity: {weather_data_set['humidity']}%")
    print(f" - Wind Speed: {weather_data_set['wind_speed']} m/s\n")


def main():
    # Get API key from environment or hardcode the key if needed.
    api_key = OPENWEATHER_API_KEY
    print('API KEY:', api_key)
    weather_service = OpenWeatherService(api_key)

    favorites = []  # Store your favorite cities in memory, with a maximum of three.

    while True:
        print("======================================")
        print("        Display current weather       ")
        print("======================================")
        print("1. Check Weather for a City")
        print("2. Add a City to My favorites")
        print("3. View My Favourite Cities")
        print("4. Modify My Favourite Cities")
        print("5. Exit")
        print("======================================")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Inquire weather information of a city
            city_name = input("Provide the name the city: ").strip()
            weather_data_set = weather_service.get_weather_data(city_name)
            show_weather_details(weather_data_set)

        elif choice == '2':
            # Add a city to your favorites list if there's available space.
            if len(favorites) >= 3:
                print("The favorites list is at capacity. Please remove a city to add a new one.")
            else:
                city_name = input("Please enter the city name to add to your favorites: ").strip()
                weather_data_set = weather_service.get_weather_data(city_name)
                if weather_data_set:
                   # Add the city only if it was found successfully
                   # In addition , ensure no duplicates are added
                    if city_name.lower() not in [c.lower() for c in favorites]:
                        favorites.append(city_name)
                        print(f"{city_name} added to favorites.")
                    else:
                        print("This city is already in your favorites list.")
                else:
                    print("The city is not recognized. Unable to add to favorites.")

        elif choice == '3':
            # Display favorite cities and their current weather
            if not favorites:
                print("No favorite cities found in your list.")
            else:
                print("\nWeather of Favourite Cities:")
                for fav_city in favorites:
                    weather_data_set = weather_service.get_weather_data(fav_city)
                    show_weather_details(weather_data_set)

        elif choice == '4':
            # Modify favorite cities: remove an existing one and add a new one
            if not favorites:
                print("No cities in your favorites to change. Add the cities first.")
            else:
                print("Current favourite cities list:")
                for i, city in enumerate(favorites, start=1):
                    print(f"{i}. {city}")

                remove_choice = input("Select the number of the city to remove: ").strip()
                if remove_choice.isdigit():
                    remove_index = int(remove_choice) - 1
                    if 0 <= remove_index < len(favorites):
                        removed_city = favorites.pop(remove_index)
                        print(f"{removed_city} removed. You may now add a new city.")
                        # Add a new city
                        new_city = input("Type the name of the city to add to favorites: ").strip()
                        weather_data_set = weather_service.get_weather_data(new_city)
                        if weather_data_set:
                            if new_city.lower() not in [c.lower() for c in favorites]:
                                favorites.append(new_city)
                                print(f"{new_city} added to favorites.")
                            else:
                                print("The city is already a favourite. cannot be added.")
                        else:
                            print("City not located. No new favourite added.")
                    else:
                        print("Invalid option. No city has been removed.")
                else:
                    print("Invalid option. Please enter a correct number.")

        elif choice == '5':
            # Exit the application
            print("Closing the program. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a number from the menu.")

        # Optional: Wait for user input to proceed.
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()