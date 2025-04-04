from functools import reduce

def filter_trails(trails, min_length=0, max_length=0, difficulty=0, region="", sunshine_hours=0, weather_data=None):
    return list(filter(
        lambda trail: ((trail['length_km'] >= min_length if min_length else True) and(trail['length_km'] <= max_length if max_length else True) and(trail['difficulty'] == difficulty if difficulty != 0 else True) and(trail['region'] == region if region else True) and(sunshine_hours == 0 or any(item['sunshine_hours'] >= sunshine_hours for item in weather_data if item['region'] == region))
        ), trails))

def compute_weather_statistics(weather_data, region):
    filtered_weather = list(filter(lambda x: x['region'] == region, weather_data))
    num_records = len(filtered_weather)

    if num_records == 0:
        return 0, 0, 0

    avg_temp = sum(item['avg_temp'] for item in filtered_weather) / num_records
    total_precip = sum(item['precipitation'] for item in filtered_weather)
    sunny_days = len([1 for item in filtered_weather if item['sunshine_hours'] > 8])

    return avg_temp, total_precip, sunny_days

def calculate_avg_temperature(region, weather_data):
    region_weather = filter(lambda x: x['region'] == region, weather_data)
    region_weather = list(region_weather) 

    if region_weather:
        avg_temp = sum(item['avg_temp'] for item in region_weather) / len(region_weather)
    else:
        avg_temp = 0

    return avg_temp

def total_precipitation_in_region(region, weather_data):
    region_weather = filter(lambda x: x['region'] == region, weather_data)
    total_precip = reduce(lambda x, y: x + y['precipitation'], region_weather, 0)
    return total_precip
