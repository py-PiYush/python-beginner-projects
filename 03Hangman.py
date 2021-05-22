from words import words
import random
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word=get_valid_word(words)
    word_letters= set(word)                 #Letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()                     #User guess

    no_of_letters = len(word)
    chances = 5

    print('Welcome to Hangman!!'.center(50))
    print('Correctly guess letters of the word to win.\nYou have 5 incorrect chances.')
    print('Length of the word: ',no_of_letters,'\n')
   
    while len(word_letters):

        if chances==0:
            print('Game Over! Better Luck Next Time.\n The word was:',word)     #chances over
            break

         #User input
        print('Chances remaining: ', chances)
        user_letter = input('Guess a letter: ').lower()
        print('\n')
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                chances-=1
                print(f'Your letter {user_letter} is not in the word.')
        
        elif user_letter in used_letters:
            print('Already guessed. Please try again.')

        else:
            print('Invalid Character')


        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current Word: ',' '.join(word_list))          #Current word
        if '_' not in word_list:
            print('Congrats, You have successfully guessed the word.')
        print('You have used these letters: ', ','.join(used_letters), '\n') #list of used letters
        


hangman()
    



