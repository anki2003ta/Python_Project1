import random

# edit this list - get more from Chat GPT
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself"},
    {"spanish": "no", "english": "no"},
    {"spanish": "por", "english": "for"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his"},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "like"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},

]

def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word["spanish"]}'?")
        user_answer = input("Your answer: ").strip().lower()
        #correct_answer = word["english"]

        if (user_answer == word["english"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word["english"]}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
  main()