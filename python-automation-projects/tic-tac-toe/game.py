import time
import random
from player import AverageComputerPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board.
        self.current_winner = None # keep track of winner!
        
    def print_board(self):
        # getting the rows
        game_board = [self.board[i*3:(i+1)*3] for i in range(3)]
        for row in game_board:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # | 0 | 1 | 2 | (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['X', 'X', 'O'] --> [(0, 'X'), (1, 'X'), (2, 'O')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves 
        # # OR
        moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
       
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move
        # return true if valid, else: false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
     
    #  checking for a winner
    def winner(self, square, letter):
        # player wins if player letter fills 3 in a row anywhere for all possibilities.
        # checking row
        row_index = square // 3
        row = self.board[row_index*3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # checking column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # checking diagnols
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # return false if all checks fail
        return False
                
def play(game, player_x, player_o, print_game=True):
    # returns the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = random.choice(['X', 'O']) # randomly chooses a player to start game
            
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = player_o.get_move(game)
        else:
            square = player_x.get_move(game)
            
        # making a move
        if game.make_move(square, letter):
            if print_game:
                if letter == 'O':
                    print('Computer\'s turn.')
                    print(f'Computer makes a move to square {square}')
                else:
                    print(f'Player1 makes a move to square {square}')
                game.print_board()
                print('') # just an empty line
                
            if game.current_winner:
                if print_game:
                    if letter == 'O':
                        print('Computer wins!')
                        print(' ') # to create a space between two games
                    elif letter == 'X':
                        print('Player1 wins!')
                        print(' ') # to create a space between two games
                        
                return letter
                
            # # alternate letters after making a move
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
            # # OR
            letter = 'O' if letter == 'X' else 'X'
            
        # adding a time break between player1 and computer moves
        if print_game:
            time.sleep(0.6)
     
    # when it's a tie       
    if print_game:
        print('It\'s a tie! Play again.')
        print(' ') # to create a space between two games 
                   
if __name__ == '__main__':
    o_wins = 0
    x_wins = 0
    draws = 0
    for _ in range(3):
        print('New Game')
        tictactoe = TicTacToe()
        player_o = AverageComputerPlayer('O')
        player_x = HumanPlayer('X')
        game_result = play(tictactoe, player_x, player_o, print_game=True)
        if game_result == 'O':
            o_wins += 1
        elif game_result == 'X':
            x_wins += 1
        else:
            draws += 1
            
    print(f'Player1 won {x_wins}, Computer won {o_wins} and {draws} games were a tie.')
    
    # quitting game
    user_input = input("Enter 'q' to quit game: ").lower()
    if user_input == 'q':
        quit()