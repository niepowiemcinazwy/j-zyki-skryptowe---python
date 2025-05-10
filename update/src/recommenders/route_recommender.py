from models.weather_data import WeatherData

class RouteRecommender:
    def __init__(self, route_data_manager, weather_data_manager):
        self.route_data_manager = route_data_manager
        self.weather_data_manager = weather_data_manager

    def recommend_routes(self, preferences, routes, weather_data):
        filtered_routes = self.route_data_manager.filter_routes(routes, preferences)
        
        recommendations = []
        
        for route in filtered_routes:
            if route.region.strip().lower() != preferences.region.strip().lower():
                continue

            matching_weather = [
                weather for weather in weather_data
                if weather['region'].strip().lower() == route.region.strip().lower()
            ]
            
            if matching_weather:
                weather_info = matching_weather[0]
                
                if (preferences.preferred_temp is None or weather_info['avg_temp'] <= preferences.preferred_temp) and \
                   (weather_info['precipitation'] <= preferences.max_precipitation):
                    weather_obj = WeatherData(
                        date=weather_info['date'],
                        location_id=route.region,
                        avg_temp=weather_info['avg_temp'],
                        min_temp=weather_info['min_temp'],
                        max_temp=weather_info['max_temp'],
                        precipitation=weather_info['precipitation'],
                        sunshine_hours=weather_info['sunshine_hours'],
                        cloud_cover=weather_info['cloud_cover']
                    )
                    route.comfort_index = weather_obj.comfort_index()

                    recommendations.append(route)
        
        return recommendations
