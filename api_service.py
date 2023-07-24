import requests

class APIService():
    def __init__(self) -> None:
        self._api_key = "RGAPI-348f62e8-b766-48ec-9cee-81ae75699047"
        self._api_champions_url = "http://ddragon.leagueoflegends.com/cdn/13.14.1/data/en_US/champion.json"
        self._api_rotation_url = "https://eun1.api.riotgames.com/lol/platform/v3/champion-rotations"

    def get_champions(self) -> list[str]:
        champions_response = requests.get(self._api_champions_url)
        rotation_response = requests.get(self._api_rotation_url, headers={"X-Riot-Token": self._api_key})
        rotation_ids = rotation_response.json()['freeChampionIds']
        champions_in_rotation = [] # type: list[str]
        for id in rotation_ids:
            for champion in champions_response.json()['data'].values():
                if champion['key'] == str(id):
                    champions_in_rotation.append(champion['name'])
        return champions_in_rotation



if __name__ == "__main__":
    api_service = APIService()
    print(api_service.get_champions())