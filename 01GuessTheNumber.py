import random

def guess1(x):
    random_number= random.randint(1,x)
    guess, no_of_attempts = 0,1

    while guess!=random_number:
        guess= int(input(f'Guess a number between 1 and {x}: '))
        if guess<random_number:
            no_of_attempts+=1
            print('Sorry, guess again. Too low.')
        elif guess>random_number:
            no_of_attempts+=1
            print('Sorry, guess again. Too high')
    print(f"Congrats!! You have guessed the number {random_number} corrtectly in {no_of_attempts} attempts.")


def guess2(x):
    low,high = 1,x
    feedback = ""
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback = input(f'Is {guess} high(h), low(l) or correct(c)')
        feedback=feedback.lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'The computer has guessed {guess} correctly!')
guess2(100)