class Route:
    def __init__(self, id, name, region, start_lat, start_lon, end_lat, end_lon, length_km, elevation_gain, difficulty, terrain_type, tags):
        self.id = id
        self.name = name
        self.region = region
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
        self.length_km = length_km
        self.elevation_gain = elevation_gain
        self.difficulty = difficulty
        self.terrain_type = terrain_type
        self.tags = tags
        self.comfort_index = None

    def calculate_center(self):
        return ((self.start_lat + self.end_lat) / 2, (self.start_lon + self.end_lon) / 2)

    def estimate_time(self):
        base_time = self.length_km / 5
        elevation_time = self.elevation_gain / 600
        difficulty_multiplier = 1.0 + (self.difficulty * 0.2)
        terrain_multiplier = 1.0
        return (base_time + elevation_time) * difficulty_multiplier * terrain_multiplier

    def match_preferences(self, preferences):
        if preferences.max_length and self.length_km > preferences.max_length:
            return False
        if preferences.max_difficulty and self.difficulty > preferences.max_difficulty:
            return False
        return True

    def calculate_comfort_index(self, temperature, precipitation):
        self.comfort_index = max(0, min(100, 100 - abs(temperature - 20) * 2))