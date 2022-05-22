import random

class Player:
    def __init__(self, letter):
        # letter is 'X' or 'O'
        self.letter = letter
    
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass
    
class AverageComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

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