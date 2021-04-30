import cassiopeia as kassadin
import keys
kassadin.set_riot_api_key(keys.dank_keys())
kassadin.set_default_region("NA")
name = input("Enter first and last name ")
userName = input("What is your username in game")
summoner = kassadin.get_summoner(name=userName)
level = summoner.level
rank = summoner.league_entries
this_mans_champion_masteries = summoner.champion_masteries
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


def player_report(player_name, user_name, player_level, player_role, player_favorite_champions, player_rank, this_mans_champion_masteries):
    print("=== LEAGUE PLAYER REPORT ===")
    print(f"Full name is {player_name}")
    print(f"Username is {user_name}")
    print(f"Level is {player_level}")
    print(player_role)
    print(player_favorite_champions)
    print(f"Current Solo/Duo rank: {player_rank.fives.tier}")
    print(f"Current Flex rank: {player_rank.flex.tier}")
    print(this_mans_champion_masteries)


player_report(name, userName, level, favoriteRoles, favoriteChampions, rank, this_mans_champion_masteries)
