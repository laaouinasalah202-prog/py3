

def AchievementTracker():
    """Achievement Tracker: track unique, shared, and rare achievements,
    see missing ones, and find player
    communities based on shared accomplishments."""

    print("=== Achievement Tracker System ===\n")

    players = {
            "alice": {
                'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
                },
            "bob": {
                'first_kill', 'level_10', 'boss_slayer', 'collector'
                },
            "charlie": {
                'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                'perfectionist',
                }
            }

    print(f"Player alice achievements: {players['alice']}")
    print(f"Player bob achievements: {players['bob']} ")
    print(f"Player charlie achievements: {players['charlie']}\n")
    b = set.union(players["alice"], players["bob"], players["charlie"])
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {b}")
    print(f"Total unique achievements: {len(b)}\n")
    f = set.intersection(players["alice"], players["bob"], players["charlie"])
    print(f"Common to all players: {f}")

    """ convert the dict to a set that contain all the values
    in order to loop and find the rarest """

    all_achievements = set().union(*players.values())
    rare = {
        a for a in all_achievements
        if sum(a in s for s in players.values()) == 1
    }
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: "
          f"{set.intersection(players['alice'], players['bob'])}")
    print(f"Alice unique: {set.difference(players['alice'], players['bob'])}")
    print(f"Bob unique: {set.difference(players['bob'], players['alice'])}")


AchievementTracker()
