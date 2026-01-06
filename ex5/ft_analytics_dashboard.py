
def display_analitic():
    print("=== Game Analytics Dashboard ===\n")


    achievements = {
            "alice": {
                'first_kill', 'level_10', 'treasure_hunter', 'speed_demon', 'serial_killer'
                },
            "bob": {
                'first_kill', 'level_10', 'boss_slayer'
                },
            "charlie": {
                'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                'perfectionist', 'collector', 'serial_killer'
                }
            }
    players = {
            "alice": {"score": "2300", "status": "active"} ,
            "charlie": {"score": "2150", "status": "active"},
            "bob": {"score": "1800", "status": "active"},
            "diana": {"score": "2001", "status": "inactive"} 
            }
    score_categorie = {"high": "3", "medium": "2", "low": "1"}
    player_scores = {'alice': 2300, 'bob': 1800, 'charlie': 2150}
    total_achievements = {'alice': 5, 'bob': 3, 'charlie': 7}
    print("=== List Comprehension ===")
    double = [4600, 3600, 4300, 4100]
    high_score = []
    active_players = []
    for i,z in list(players.items()):
        if (int(z["score"])) > 2000:
            high_score.append(i)
        if z["status"] == "active":
            active_players.append(i)
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {double}")
    print(f"Active players: {active_players}")
    
    print("\n=== Dict Comprehension ===") 
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categorie}")
    print(f"Achievement counts: {total_achievements}")
    print("\n=== Set Comprehension ===")


display_analitic()
