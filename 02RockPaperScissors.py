import random

def play():
    user= input('rock/paper/scissor: ')
    user=user.lower()
    computer = random.choice(['rock', 'paper', 'scissor'])

    if user == computer:
        return "It's a tie!"

    if win(user, computer):
        return "Congrats, You won."

    return "You lost! Better Luck Next Time."
    
def win(player, opponent):
    if (player == 'rock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True 

print(play())