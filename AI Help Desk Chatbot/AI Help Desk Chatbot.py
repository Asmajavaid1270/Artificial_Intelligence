# --- AI Help Desk Chatbot (Complete Version) ---
# Tasks: 1 (Intent Classification), 2 (Response Logic), 3 (Activity Recommendation), 4 (Wrap-up)

history = []

# -------------------------------
# Task 1: Intent Classifier
# -------------------------------
def classify_intent(user_msg):
    msg = user_msg.lower()

    if any(word in msg for word in ["hi", "hello", "hey", "salam"]):
        return "greeting"
    elif any(word in msg for word in ["thank", "thanks", "thx"]):
        return "thanks"
    elif any(word in msg for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in msg for word in ["study", "learn", "exam", "homework"]):
        return "study"
    elif any(word in msg for word in ["food", "hungry", "eat", "snack", "meal"]):
        return "food"
    else:
        return "unknown"

# -------------------------------
# Task 3: Activity Recommender
# -------------------------------
def activity_recommender(feeling, time_of_day):
    # Simple rule-based suggestions
    if feeling == "stressed":
        if time_of_day == "evening":
            return "walk or meditate", "Relaxing activities can refresh your mind."
        else:
            return "deep breathing or short stretch", "Take small breaks to stay focused."
    elif feeling == "tired":
        return "power nap or tea break", "Rest helps improve focus."
    else:
        return "listening to calm music", "Music boosts productivity."
        
# -------------------------------
# Task 4: Wrap-Up (Interactive Chat)
# -------------------------------
def bot_reply(user_msg):
    intent = classify_intent(user_msg)
    reply = ""

    if intent == "greeting":
        reply = "Hello! How can I help you today?"
    elif intent == "thanks":
        reply = "You're welcome! Happy to help."
    elif intent == "goodbye":
        reply = "Goodbye! See you soon."
    elif intent == "study":
        rec, tip = activity_recommender("stressed", "evening")
        reply = f"A study tip: Try a 25-minute focus session and then {rec}. {tip}"
    elif intent == "food":
        reply = "Try a light, healthy meal to keep your energy up while studying."
    else:
        reply = "I'm not sure yet, but I can help with greetings, study tips, or food suggestions."

    return intent, reply


# -------------------------------
# Main Chat Loop
# -------------------------------
print("Chat with AI Help Desk (type 'exit' to finish).")
while True:
    u = input("You: ").strip()
    if u.lower() == "exit":
        print("Session ended. Summary below.")
        break
    
    intent, resp = bot_reply(u)
    history.append((u, resp, intent))
    print(f"[Bot]: {resp}")

print("\nConversation Summary:")
for i, (u, r, it) in enumerate(history, 1):
    print(f"{i}) Intent: {it} | User: '{u}' | Reply: '{r}'")
