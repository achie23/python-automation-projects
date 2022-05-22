import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) 
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    # user lives allowed
    lives = 6
    
    # getting user input
    # continue to until len(word_letters) == 0
    while len(word_letters) > 0 and lives > 0:
        # letters already used
        print('You have', lives, 'lives remaining and you have used these letters: ', ' '.join(used_letters))
        
        # what the current word is (i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # takes away a life if user is wrong
                print('Letter is not in word. Keep guessing.')
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')
    
    # gets here when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(f'Oops! You died, The word was {word}.')
    else:
        print(f'Hurray! You guessed the word {word} correctly.')
    
            
hangman()