# Weighted Scoring System for Activity Recommendation
def activity_recommender(feeling, time_of_day):
    feeling = feeling.lower().strip()
    time_of_day = time_of_day.lower().strip()
    scores = {"read": 0, "walk": 0, "nap": 0, "music": 0}

    # Based on feeling
    if feeling == "tired":
        scores["nap"] += 3; scores["music"] += 1
    elif feeling == "stressed":
        scores["walk"] += 2; scores["music"] += 2
    elif feeling == "bored":
        scores["read"] += 2; scores["walk"] += 1
    elif feeling == "energetic":
        scores["walk"] += 3; scores["read"] += 1

    # Based on time
    if time_of_day in ("morning", "afternoon"):
        scores["walk"] += 1; scores["read"] += 1
    elif time_of_day == "evening":
        scores["music"] += 2; scores["walk"] += 1
    elif time_of_day in ("night"):
        scores["nap"] += 2; scores["read"] += 1
    
    best = max(scores, key=scores.get)
    return best, scores

def read_choice(prompt, choices):
    low = [c.lower() for c in choices]
    while True:
        s = input(f"{prompt} ({'/'.join(choices)}): ").strip().lower()
        if s in low:
            return s
        print(f"Please choose one of {choices}.")

while True:
    print("\nRecommend an activity (type 'exit' to stop)")
    nxt = input("Continue (yes/exit): ").strip().lower()
    if nxt == "exit":
        print("Stopped Task 3.")
        break
    
    feeling = read_choice("Your feeling?", ["tired", "stressed", "bored", "energetic"])
    time_of_day = read_choice("Time of day?", ["morning", "afternoon", "evening", "night"])

    rec, sc = activity_recommender(feeling, time_of_day)
    print(f"Recommendation: {rec}", f"| Scores: {sc}")