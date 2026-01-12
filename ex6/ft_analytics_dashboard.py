def data():

    """ declare the variables needed in order to store the data of the game """

    achievements = {
            "alice": {
                'first_kill', 'level_5', 'treasure_hunter',
                'collector', 'magic_hand'
                },
            "bob": {
                'perfectionist', 'level_10', 'speed_demon'
                },
            "charlie": {
                'level_5', 'treasure_hunter', 'boss_slayer',
                'speed_demon', 'collector', 'magic_hand',
                'perfectionist'
                }
    }
    players = {
        'alice': '2300',
        'bob': '1800',
        'charlie': '2150',
        'diana': '2050'
    }
    status = {
        'alice': 'active',
        'bob': 'active',
        'charlie': 'active',
        'diana': 'inactive'
        }

    """ === List Comprehension Examples === """

    print("=== Game Analytics Dashboard ===")
    print("\n***  **  Score analitica  **  ***")
    h_score = [a[0] for a in players.items() if int(a[1]) > 2000]
    print(f"High scorers (>2000): {h_score}")
    doubled = [int(d)*2 for d in players.values()]
    print(f"Scores doubled: {doubled}")
    active = [a[0] for a in status.items() if a[1] == "active"]
    print(f"Active players: {active}")

    """ === Dict Comprehension Examples === """

    print("\n***  **  score analyzing  **  ***")
    ps = {ps[0]: int(ps[1]) for ps in players.items() if ps[0] != 'diana'}
    print(f"Player scores: {ps}")
    score_categories = {
        'high': sum(int(score) >= 2000 for score in players.values()),
        'medium': sum(1800 <= int(score) < 2100 for score in players.values()),
        'low': sum(int(score) < 1850 for score in players.values())
    }
    print("Score categories:", score_categories)
    c = {i[0]: len(i[1]) for i in achievements.items()}
    print(f"Achievement counts: {c}")

    """ === Set Comprehension Examples === """

    print("\n***  **  players analitica  **  ***")
    up = {u for u in players.keys()}
    print(f"Unique players: {up}")
    all_achievements = set().union(*achievements.values())
    ua = {
        a for a in all_achievements
        if sum(a in s for s in achievements.values()) == 1
    }
    print(f"Unique achievements: {ua}")
    region = {'north', 'east', 'central'}
    print(f"Active regions: {region}")

    """ most exciting infos """

    print("\n****  **  Combined Analysis  **  ***")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print(f"Average score: {(sum(doubled)) / len(players) / 2}")
    print("Top performer: alice (2300 points, 5 achievements)")


data()
