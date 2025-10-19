from abc import ABCMeta, abstractmethod

import requests


class CharacterData:
    """インターフェース"""

    @abstractmethod
    def get_character_by_id(self, name: str) -> dict:
        pass


class CharacterDataFromAPI(CharacterData):
    def __init__(self, url: str) -> None:
        self.url = url

    def get_character_by_id(self, name: str) -> dict:
        res = requests.get(f"{self.url}/character/{name}")
        return res.json()


class Service:
    def __init__(self, character_data: CharacterData) -> None:
        self.character_data = character_data

    def get_hp(self, name: str) -> int:
        character = self.character_data.get_character_by_id(name)
        return character["hp"]

    def get_attack_power(self, name: str) -> int:
        character = self.character_data.get_character_by_id(name)
        return character["attack_power"]

    def get_defence_power(self, name: str) -> int:
        character = self.character_data.get_character_by_id(name)
        return character["defence_power"]
