from models.user_preference import UserPreference

class UserInterface:
    print(f"\nOdpowiedz na poniższe pytania.\n")
    def get_user_input(self):
        region = input("Podaj preferowany region: ")
        max_length_input = input("Podaj maksymalną długość trasy w km (lub kliknij Enter, aby uwzględnić wszystkie): ")
        max_difficulty_input = input("Podaj maksymalny poziom trudności (lub kliknij Enter, aby uwzględnić wszystkie): ")
        preferred_temp_input = input("Podaj preferowaną temperaturę (lub kliknij Enter, aby uwzględnić wszystkie): ")
        max_precipitation_input = input("Podaj maksymalne opady (lub kliknij Enter, aby uwzględnić wszystkie): ")

        max_length = float(max_length_input) if max_length_input else float('inf')
        max_difficulty = int(max_difficulty_input) if max_difficulty_input else 3 
        preferred_temp = float(preferred_temp_input) if preferred_temp_input else None 
        max_precipitation = float(max_precipitation_input) if max_precipitation_input else float('inf')

        return UserPreference(max_length, max_difficulty, preferred_temp, max_precipitation, region)


    def display_recommendations(self, recommendations):
        print(f"\nInformacje o trasach według Twoich predyspozycji:\n")
        for i, recommendation in enumerate(recommendations):
            time = recommendation.estimate_time()
            print(f"{i+1}. {recommendation.name} ({recommendation.region})")
            print(f"   Długość: {recommendation.length_km} km")
            print(f"   Trudność: {recommendation.difficulty}/3")
            print(f"   Szacowany czas: {time:.0f}h {int((time % 1) * 60):02d}min")
            print(f"   Komfort pogodowy: {recommendation.comfort_index:.0f}/100")
            print(f"   Kategoria: {', '.join(recommendation.tags.split(', '))}\n")