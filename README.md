# **⚾ BoxscoreBagger ⚾**

- Creating a TeamData object for a website:

    * team = TeamData("https://www.mlb.com/gameday/red-sox-vs-orioles/2023/04/26/718416/preview",718416) 

    - The link will provide the name for the JSON file
    - The 6 digit code is the game id, and is crucial for getting the correct data

**Accessing data:**

- print(team.batters) --> prints the ids of the players
- print(team.pitchers) --> prints the ids of the pitchers
- print(team.codes) --> prints the team codes
