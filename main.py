import random
import string
from Words import Randomwords

def get_valid_word(word):
    word = random.choice(Randomwords)
    while " " in word or "-" in word:
        word = random.choice(Randomwords)
    return word.upper()

def hangman():
    #I want the user to put a word then i need to check if the letter was used or not
    word = get_valid_word(Randomwords)
    word_letters = set(word)
    usedwords = set()
    alphabet = set(string.ascii_uppercase)

    while len(word_letters) != 0:
        worddash = [letter if letter in usedwords else '-' for letter in word]

        print("Current word: ",' '.join(worddash))
        usersinput = input("Enter word: ").upper
        if usersinput in alphabet-usedwords:
            usedwords.add(usersinput)
            word_letters.remove(usersinput)
        else:
            print("You already used that word")
print(hangman())
