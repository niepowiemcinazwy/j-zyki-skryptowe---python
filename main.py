import os
from file_operations import load_file, save_to_file
from data_processing import filter_trails, calculate_avg_temperature, total_precipitation_in_region

def display_recommendations(trails, weather_data):
    if not trails:
        print("\nBłąd! Nie znaleziono tras bazując na twoich predyspozycjach!")
        return
    
    print("\nSukces! Wszystkie dostępne trasy bazowane na Twoich predyspozycjach:\n")
    
    all_trails_data = []
    
    for trail in trails:
        avg_temp = calculate_avg_temperature(trail['region'], weather_data)
        total_precipitation = total_precipitation_in_region(trail['region'], weather_data)
        sunshine_hours = sum(entry['sunshine_hours'] for entry in weather_data if entry['region'] == trail['region'])
        print(f"Trasa: {trail['name']}")
        print(f"» Region: {trail['region']}")
        print(f"» Długość trasy: {trail['length_km']} km")
        print(f"» Poziom trudności: {trail['difficulty']}")
        print(f"» Typ terenu: {trail['terrain_type']}")
        print(f"» Zysk wysokości: {trail['elevation_gain']} m")
        print(f"» Tagi: {trail['tags']}")
        print(f"» Średnia temperatura: {round(avg_temp)}°C")
        print(f"» Suma opadów: {round(total_precipitation, 2)} mm")
        print(f"» Liczba dni słonecznych: {sunshine_hours}\n")

        all_trails_data.append({
            "name": trail['name'],
            "region": trail['region'],
            "length_km": trail['length_km'],
            "difficulty": trail['difficulty'],
            "terrain_type": trail['terrain_type'],
            "elevation_gain": trail['elevation_gain'],
            "tags": trail['tags'],
            "avg_temp": round(avg_temp),
            "precipitation": total_precipitation,
            "sunshine_hours": sunshine_hours
        })
    
    if all_trails_data:
        save_to_file('info.json', all_trails_data)
        print(f"Sukces! Pomyślnie zapisano wszystkie informacje do pliku info.json!")

def main():
    trails_data = load_file('trails.json')
    weather_data = load_file('weather_data.json')
    
    available_regions = set(trail['region'] for trail in trails_data)
    print(f"\n============ INFORMACJA ============")
    print("\nW przypadku każdej informacji oznaczonej znakami [*], wpisanie '0' oznacza brak preferencji, co sprawi, że dana kategoria nie będzie brana pod uwagę podczas wyszukiwania tras, a wszystkie dostępne opcje zostaną uwzględnione.\n")
    print(f"============ INFORMACJA ============")
    print(f"\nInformacja! Wszystkie dostępne regiony: {', '.join(sorted(available_regions))}")

    region = input('- Podaj preferowany region: ').strip()
    while region not in available_regions:
        print("Błąd! Wpisano niepoprawny region! Spróbuj ponownie.")
        region = input(f"- Podaj preferowany region: ({', '.join(available_regions)}) ").strip()

    min_length = int(input('- [*] Podaj minimalną długość trasy (w km): '))
    max_length = int(input('- [*] Podaj maksymalną długość trasy (w km): '))

    difficulty = int(input('- [*] Podaj preferowany poziom trudności (1 - łatwy, 2 - średni, 3 - trudny): '))
    while difficulty not in [0, 1, 2, 3]:
        print("Błąd! Wybierz poprawny poziom trudności trasy od 0 do 3!")
        difficulty = int(input('- [*] Podaj preferowany poziom trudności (1 - łatwy, 2 - średni, 3 - trudny): '))

    sunshine_hours = int(input('- [*] Podaj minimalną liczbę godzin słonecznych (w minutach): '))

    filtered_trails = filter_trails(trails_data, min_length, max_length, difficulty, region, sunshine_hours, weather_data)
    
    display_recommendations(filtered_trails, weather_data)

if __name__ == '__main__':
    main()
