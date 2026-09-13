import random

activities = {
    "happy": [
        "Listen to your favorite music.",
        "Go for a walk.",
        "Call a friend.",
        "Work on a fun coding project."
    ],

    "sad": [
        "Watch a comedy movie.",
        "Talk to someone you trust.",
        "Take a short walk.",
        "Listen to relaxing music."
    ],

    "tired": [
        "Take a short break.",
        "Drink some water.",
        "Take a 20 minute nap.",
        "Do some light stretching."
    ],

    "bored": [
        "Learn something new.",
        "Try a Python project.",
        "Read a book.",
        "Play a game."
    ],

    "angry": [
        "Take a few deep breaths.",
        "Go for a walk.",
        "Listen to calm music.",
        "Take some time away from the situation."
    ]
}

print("===== MOOD ACTIVITY SUGGESTER =====")

while True:

    print("\nAvailable moods:")
    print("happy")
    print("sad")
    print("tired")
    print("bored")
    print("angry")
    print("exit")

    mood = input("\nHow are you feeling? ").lower().strip()

    if mood == "exit":
        print("Goodbye!")
        break

    if mood in activities:
        suggestion = random.choice(activities[mood])

        print("\nYour suggested activity:")
        print(suggestion)

    else:
        print("Sorry, I don't recognize that mood.")
