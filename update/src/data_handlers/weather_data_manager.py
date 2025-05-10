import json

class WeatherDataManager:
    @staticmethod
    def load_weather(file_path):
        with open(file_path, 'r') as file:
            weather_data = json.load(file)
        return weather_data