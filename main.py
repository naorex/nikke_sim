from src.character import Character
from src.service import CharacterDataFromAPI, Service


def main():
    url = "http://127.0.0.1:5000"
    character_data = CharacterDataFromAPI(url)

    service = Service(character_data)
    character = Character(name="SoldierEG", service=service)

    print(character.name, character.combat_power)


if __name__ == "__main__":
    main()
