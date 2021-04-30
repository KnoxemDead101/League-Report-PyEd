import cassiopeia as kassadin
import keys
kassadin.set_riot_api_key(keys.dank_keys())
kassadin.set_default_region("NA")
name = input("Enter first and last name ")
userName = input("What is your username in game")
summoner = kassadin.get_summoner(name=userName)
level = summoner.level
rank_last_season = summoner.rank_last_season
champion_masteries = summoner.champion_masteries
match_history = summoner.match_history
# This is a command and i have no idea what this can lead to now
# current_match = summoner.current_match
favoriteRoles = []
while True:
    roles = input("List your favorite roles to play")
    if roles == "Q":
        break
    else:
        favoriteRoles.append(roles)
favoriteChampions = []
while True:
    champions = input("List your favorite champions to play as of late (just to make your profile up to date)")
    if champions == "Q":
        break
    else:
        favoriteChampions.append(champions)


def display_player_info(player_name, user_name, player_level, player_role, player_favorite_champions,
                        player_rank_last_season, champion_mastery, match_histroy):
    print("=== LEAGUE PLAYER REPORT ===")
    print(f"Full name is {player_name}")
    print(f"Username is {user_name}")
    print(f"Level is {player_level}")
    print(player_role)
    print(player_favorite_champions)
    print(player_rank_last_season)
    print(champion_mastery)
    print(match_histroy)


display_player_info(name, userName, level, favoriteRoles, favoriteChampions, rank_last_season,
                    champion_masteries, match_history)