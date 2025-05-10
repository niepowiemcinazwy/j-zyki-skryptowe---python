import json
from models.route import Route

class RouteDataManager:
    @staticmethod
    def load_routes(file_path):
        with open(file_path, 'r') as file:
            routes_data = json.load(file)
        
        routes = []
        for route_data in routes_data:
            route = Route(
                id=route_data['id'],
                name=route_data['name'],
                region=route_data['region'],
                start_lat=route_data['start_lat'],
                start_lon=route_data['start_lon'],
                end_lat=route_data['end_lat'],
                end_lon=route_data['end_lon'],
                length_km=route_data['length_km'],
                elevation_gain=route_data['elevation_gain'],
                difficulty=route_data['difficulty'],
                terrain_type=route_data['terrain_type'],
                tags=route_data['tags']
            )
            routes.append(route)
        
        return routes

    @staticmethod
    def filter_routes(routes, preferences):
        filtered_routes = []
        for route in routes:
            if (route.length_km <= preferences.max_length and
                route.difficulty <= preferences.max_difficulty):
                filtered_routes.append(route)
        
        return filtered_routes
