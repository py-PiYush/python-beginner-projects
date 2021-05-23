import math
import random
import time
from typing import Sequence

class Player:
    def __init__(self, letter):
        self.letter= letter
    
    def get_move(self,game):
        pass

class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter+'\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.\n')
            return val


class smartComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves())==9:
            square = random.choice(game.available_moves())

        else:
            square = self.minimax(game, self.letter)['position']
        
        return square

    def minimax(self, state, player):
        max_player = self.letter        #yourself
        other_player = 'o' if player =='x' else 'x'

        if state.current_winner == other_player:
            return {'position': None
                   , 'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)
                   }
                
        elif not state.empty_squares():
            return {'position':None, 'score': 0}

        if player == max_player:
            best = {'position':None, 'score': -math.inf}

        else:
            best = {'position':None, 'score': math.inf}

        for possible_move in state.available_moves():
            #1. make a move, try that spot
            state.make_move(possible_move, player)

            #2. recurse using minimax to simulate the game
            sim_score =self.minimax(state, other_player)

            #3. undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #4. update the dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best

    

#Game
class game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None          #Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')
    
    @staticmethod
    def print_number_board():       #number corresponding to box
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def winner(self, square, letter):
        #check row
        row_ind = square//3
        row=self.board[row_ind*3: (row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True 
        
        #check column
        col_ind = square%3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot==letter for spot in col]):
            return True 

        #check diagonal
        if square%2==0:
            dia1 = [self.board[i] for i in [0,4,8]]     #left to right diagonal
            if all([spot == letter for spot in dia1]):
                return True
            dia2 = [self.board[i] for i in [2,4,6]]     #right to left diagonal
            if all([spot == letter for spot in dia2]):
                return True
            
        return False

    def make_move(self,square,letter):
        if self.board[square]==' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    

        



def play(game, x_player, o_player, print_game=True):
    letter = 'x'        #starting letter
    
    #iterate while the game has empty squares left

    while game.empty_squares():
        if letter=='o':
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(letter+ f' makes a move to square {square}')
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter, 'wins')
                return letter

            if letter =='x':
                letter = 'o'
            else: 
                letter ='x'

        game.print_board()
        print('\n')   

        time.sleep(1)

    if print_game:
        print('It\'s a tie.')

if __name__ == '__main__':
    x_player = Human('x')
    o_player = smartComputer('o')
    t=game()
    #t.print_board()
    t.print_number_board()
   # print(t.board, t.available_moves(), t.empty_squares(),t.num_empty_squares(), sep='\n')

    play(t, x_player,o_player)