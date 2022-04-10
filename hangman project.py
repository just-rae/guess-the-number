import random
from words import words
from hangman_Visual import lives_visual_dict
import string
from messages import Emessages
from messages import Bmessages 


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word or 'rai' in word or 'zimmerman' in word:
        word = random.choice(words)

    return word.upper()
 

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                mssg2=random.choice(Emessages)
                print(mssg2)

            else:
                lives = lives - 1  # takes away a life if wrong
                mssg=random.choice(Bmessages)
                print(mssg)

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

        
        

if __name__ == '__main__':
    hangman()
def playAgain():
    # This function returns True if the player wants to play again;otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
if playAgain():
    hangman()