import sys

def ft_score_analytics():
    print("=== Player Score Analytics ===")
    
    try:
        score = [int(x) for x in sys.argv[1:]]
        
        total = sum(score)
        Average = total / (len(score))
        mx = int(max(score))
        mn = int(min(score))
        r = int(mx - mn)
        
        print(f"Scores processed: {score}")
        print(f"Total players: {len(sys.argv)-1}")
        print(f"Total score: {total}")
        print(f"Average score: {Average}")
        print(f"High score: {mx}")
        print(f"Low score: {mn}")
        print(f"Score range: {r}")
    except :
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

ft_score_analytics()