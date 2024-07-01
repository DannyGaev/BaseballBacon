import requests
from requests.exceptions import ConnectionError

class TeamData:
    def __init__(self, link, gameId):
        self.batters = []
        self.pitchers = []
        self.codes = []
        self.link = link
        self.gameId = gameId
        self.getData()

    def getData(self):
        dests = ["away", "home"]
        boxscore_url = f"https://statsapi.mlb.com/api/v1/game/{self.gameId}/boxscore"
        print(boxscore_url)
        try:
            boxscore_response = requests.get(boxscore_url)

            if boxscore_response.status_code == 200:
                boxscore_data = boxscore_response.json()

                for dest in dests:
                    self.codes.append(
                        boxscore_data["teams"][dest]["team"]["abbreviation"])
                    self.pitchers += boxscore_data["teams"][dest]["pitchers"]
                    self.batters += boxscore_data["teams"][dest]["batters"]

                self.batters = [
                    str(batter) for batter in self.batters if batter not in self.pitchers]

            else:
                raise Exception(
                    "Unable to retrieve data at the moment, please try again later")

        except ConnectionError:
            raise ConnectionError(
                "\033[1mThere appears to be no connection to the Internet. Please check your connection, or wait a few minutes and try again :3\033[0m") from None
