import random
# Update this dictionary with questions and answers:
flashcards = {
    "question": "answer",
    "2^2": "4",
    "2^3": "8",
    "2^4": "16",
    "2^5": "32",
    "2^6": "64",
    "2^7": "128",
    "2^8": "256",
    "2^9": "512",
    "2^10": "1024",
    "2^11": "2048",
    "2^12": "4012"
}

# Get a list of keys (questions) from the dictionary
print(flashcards.keys())

# Randomly sample one question
ant=random.choice(list(flashcards.keys()))
# Use the `input` function to ask the user the question and get their response
#random.choice(flashcards.keys())
userinput = input(f"What is {ant}?")
# Use the question as a key to look up the answer in the dicitonary
flashcards[ant]
# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
if flashcards[ant] == userinput:
    print("That is correct!")
else:
    print(f"You're wrong, the answer is {flashcards[ant]}")