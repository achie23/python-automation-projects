import math
import random

class Player:
    def __init__(self, letter):
        # letter is 'X' or 'O'
        self.letter = letter
    
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # get a random valid spot for our next move
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # use minmax algorithm to get square
            square = self.minmax(game, self.letter)['position']
        return square

    def minmax(self, game_state, player):
        max_player = self.letter # player1
        genius_player = 'O' if player == 'X' else 'X' # genius AI player.
        
        # check if the previous move is a winner
        # this is our base case
        if game_state.current_winner == genius_player:
            # return position AND
            # keep track of score for minmax to work
            return {'position': None,
                    'score': 1 * (game_state.num_empty_squares() + 1) if genius_player == max_player else -1 * (
                        game_state.num_empty_squares() + 1)
            }
            
        elif not game_state.empty_squares():  # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            # best saves the best position to move and the best score
            best = {'position': None, 'score': -math.inf} # maximize each score
        else:
            best = {'position': None, 'score': math.inf} # minimize each score        
        
        for possible_move in game_state.available_moves():
            # make a move for the spot
            game_state.make_move(possible_move, player)
            # recurse using minmax to simulate a game after making that move
            simulated_score = self.minmax(game_state, genius_player) # alternate the players
            # undo the move
            game_state.board[possible_move] = ' '
            game_state.current_winner = None
            simulated_score['position'] = possible_move # otherwise it will get messed up from the recursion
            # update the dictionaries if necessary
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score # replace best
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score # replace best
        
        return best    
                
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            if self.letter == 'X':
                self.letter = 'Player1'
            elif self.letter == 'O':
                self.letter = 'Computer'
                
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then hurray!
            except:
                print('Invalid square. Please try again.')
                
        return val        