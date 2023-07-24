from api_service import APIService
import requests
import json
import sys


class Model():
    def __init__(self) -> None:
        self._champions , self._all_champions = self._load_champions()
        self._api_service = APIService()
        self._champions_in_rotation = self._api_service.get_champions()

    def _load_champions(self) -> tuple[list[str], list[str]]:
        with open('champions.txt', 'r') as f:
            self._champions = f.readlines()
        self._champions = self._sort(self._champions)

        with open('all_champions.txt', 'r') as f:
            self._all_champions = f.readlines()
        self._all_champions = self._sort(self._all_champions)

        return self._champions, self._all_champions
   
    def _sort(self, champions: list[str]) -> list[str]:
        champions = [champion.strip().title() for champion in champions]
        champions.sort()
        return champions


    def _get_not_played_champions(self) -> list[str]:
        with open('champions.txt', 'r') as f:
            champions = f.readlines()

        with open('all_champions.txt', 'r') as f:
            all_champions = f.readlines()

        champions = [champion.strip().title() for champion in champions]
        all_champions = [champion.strip().title() for champion in all_champions]

        list_of_not_played_champions = [] # type: list[str]
        for champion in all_champions:
            if champion not in champions:
                list_of_not_played_champions.append(champion)

        return list_of_not_played_champions
    
    def save_to_file(self):
        with open('champions.txt', 'w') as f:
            for champion in self._champions:
                f.write(champion + "\n")

    @property
    def champions(self) -> list[str]:
        return self._champions
    
    @property
    def all_champions(self) -> list[str]:
        return self._all_champions
    
    @property
    def champions_in_rotation(self) -> list[str]:
        return self._champions_in_rotation
    
    @champions.setter
    def champions(self, champions: list[str]) -> None:
        self._champions = champions