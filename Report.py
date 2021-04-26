name = input("Enter first and last name ")
userName = input("What is your username ")
while True:
    level = int(input("Enter level "))
    if level > 500:
        print("Enter a valid level")
    else:
        break
favoriteRoles = []
while True:
    roles = input("List favorite roles ")
    if roles == "Q":
        break
    else:
        favoriteRoles.append(roles)
favoriteChampions = []
while True:
    champions = input("List favorite champions ")
    if champions == "Q":
        break
    else:
        favoriteChampions.append(champions)


def player_report(player_name, user_name, player_level, player_role, player_favorite_champions):
    print("=== LEAGUE PLAYER REPORT ===")
    print(f"Full name is {player_name}")
    print(f"Username is {user_name}")
    print(f"Level is {player_level}")
    print(player_role)
    print(player_favorite_champions)


player_report(name, userName, level, favoriteRoles, favoriteChampions)
