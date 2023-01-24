import requests
from urllib3.exceptions import InsecureRequestWarning
import random

# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_url, verify=False)
WORDS = response.text.split()

def playHangman():
    # get random word to use (at least 5 letters)
    randomWord = ''
    while len(randomWord) < 5:
        randomWord = random.choice(WORDS).upper()

    # keep track of letters in word which are quessed
    wordLetters = set(randomWord)
    # keep track of guessed letters not in word
    usedLetters = set()

    while len(wordLetters) > 0:
        # print current display word
        displayWord = []
        for letter in randomWord:
            if letter in usedLetters:
                displayWord.append(letter)
            else:
                displayWord.append('-')
        print(f'Word: {" ".join(displayWord)}')
        
        guessLetter = input("Guess a letter: ").upper()

        if guessLetter in usedLetters:
            print(f"Letter already guessed")
        elif guessLetter in wordLetters:
            # remove the letter from the wordLetters (correct Letter)
            usedLetters.add(guessLetter)
            wordLetters.remove(guessLetter)

        else: 
            # letter not in word and not used
            usedLetters.add(guessLetter)

        #print letters used
        print(f"You've used these letters: {' '.join(usedLetters)}")
    
    print(f"CONGRATS! You guessed the word {randomWord} correctly!")

playHangman()