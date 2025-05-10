import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.route import Route
from models.weather_data import WeatherData
from models.user_preference import UserPreference
from recommenders.route_recommender import RouteRecommender
from data_handlers.weather_data_manager import WeatherDataManager
from data_handlers.route_data_manager import RouteDataManager
from ui.user_interface import UserInterface

def main():
    route_data_manager = RouteDataManager() 
    weather_data_manager = WeatherDataManager()

    routes = route_data_manager.load_routes('data/routes/routes.json')
    weather_data = weather_data_manager.load_weather('data/weather/weather.json')

    ui = UserInterface()
    preferences = ui.get_user_input()

    recommender = RouteRecommender(route_data_manager, weather_data_manager) 
    recommendations = recommender.recommend_routes(preferences, routes, weather_data)

    ui.display_recommendations(recommendations)

if __name__ == "__main__":
    main()