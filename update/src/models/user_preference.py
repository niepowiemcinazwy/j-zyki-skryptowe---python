class UserPreference:
    def __init__(self, max_length, max_difficulty, preferred_temp, max_precipitation, region):
        self.max_length = max_length
        self.max_difficulty = max_difficulty
        self.preferred_temp = preferred_temp
        self.max_precipitation = max_precipitation
        self.region = region

    def update_preferences(self, max_length, max_difficulty, preferred_temp, max_precipitation, region):
        self.max_length = max_length
        self.max_difficulty = max_difficulty
        self.preferred_temp = preferred_temp
        self.max_precipitation = max_precipitation
        self.region = region


    def comfort_match(self, weather_data):
        return abs(self.preferred_temp - weather_data.avg_temp) <= 5