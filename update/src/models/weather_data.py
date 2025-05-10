class WeatherData:
    def __init__(self, date, location_id, avg_temp, min_temp, max_temp, precipitation, sunshine_hours, cloud_cover):
        self.date = date
        self.location_id = location_id
        self.avg_temp = avg_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.precipitation = precipitation
        self.sunshine_hours = sunshine_hours
        self.cloud_cover = cloud_cover

    def is_sunny(self):
        return self.sunshine_hours > 8

    def is_rainy(self):
        return self.precipitation > 5

    def comfort_index(self):
        return max(0, min(100, 100 - abs(self.avg_temp - 20) * 2))