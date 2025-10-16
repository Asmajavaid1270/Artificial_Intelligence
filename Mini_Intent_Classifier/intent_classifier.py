# Task 1 
intent_keywords = {
    "greeting": ["hi", "hello", "salam", "assalam", "hey"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "shukriya"],
    "food": ["eat", "restaurant", "food", "lunch", "dinner"],
    "study": ["study", "exam", "assignment", "quiz", "lecture"]
}

def classify_intent(text):
    """Return an intent label for the given text using keyword rules.
    Priority: greeting > goodbye > thanks > food > study > unknown
    """
    t = text.lower().strip()
    for intent in ["greeting", "goodbye", "thanks", "food", "study"]:
        for kw in intent_keywords[intent]:
            if kw in t:
                return intent
    return "unknown"

print("Type messages (type 'exit' to stop):")
while True:
    msg = input("You: ").strip()
    if msg.lower() == "exit":
        print("Stopped Task 1.")
        break
    print(f"Intent: {classify_intent(msg)}")# Task 1 
intent_keywords = {
    "greeting": ["hi", "hello", "salam", "assalam", "hey"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "shukriya"],
    "food": ["eat", "restaurant", "food", "lunch", "dinner"],
    "study": ["study", "exam", "assignment", "quiz", "lecture"]
}

def classify_intent(text):
    """Return an intent label for the given text using keyword rules.
    Priority: greeting > goodbye > thanks > food > study > unknown
    """
    t = text.lower().strip()
    for intent in ["greeting", "goodbye", "thanks", "food", "study"]:
        for kw in intent_keywords[intent]:
            if kw in t:
                return intent
    return "unknown"

print("Type messages (type 'exit' to stop):")
while True:
    msg = input("You: ").strip()
    if msg.lower() == "exit":
        print("Stopped Task 1.")
        break
    print(f"Intent: {classify_intent(msg)}")