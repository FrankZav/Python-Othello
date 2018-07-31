directionals = [[1,1],[1,0],[1,-1],[0,1],[0,0],[0,-1],[-1,1],[-1,0],[-1,-1]]

NONE = 0
BLACK = 1
WHITE = 2
class Othello:
    'Will hold all the information regarding the Othello game state'
    def __init__(self, rows, columns, turn, org, method):
        self._column = rows
        self._row = columns
        self._board = []
        self._turn = turn
        self._setup_choice = org
        self._method = method
        
    def new_board(self):
        ''' Creates a new board based off the specifications given'''
        for rows in range(self._row):
            self._board.append([])
            for columns in range(self._column):
                self._board[-1].append(NONE)
        
    def initial_setup(self):
        '''sets up the first 4 pieces'''
        letter_choice = self._setup_choice
        if letter_choice == 'B':
            first_player = BLACK
            second_player = WHITE
        elif letter_choice == 'W':
            first_player = WHITE
            second_player = BLACK
        else:
            print("INVALID")
            return self.initial_setup()
        self._board[int(self._row/2)-1][int(self._column/2)-1] = first_player
        self._board[int(self._row/2)][int(self._column/2)] = first_player
        self._board[int(self._row/2)-1][int(self._column/2)] = second_player
        self._board[int(self._row/2)][int(self._column/2)-1] = second_player
        
        
    def first_turn(self):
        ''' choose a color'''
        turn = str(input()).upper()
        if turn == 'B':
            self._turn = turn
            return self._turn
        elif turn == 'W':
            self._turn = turn
            return self._turn
        else:
            InvalidMoveError()
    def choose(self):
        ''' choose a color'''
        turn = str(input()).upper()
        if turn == 'B':
            self._turn = turn
            return self._turn
        elif turn == 'W':
            self._turn = turn
            return self._turn
        else:
            InvalidMoveError()

    def method_to_win(self):
        '''user decides what is the method to win'''
        method = str(input())
        if method == '>':
            self._method = method
            return self._method
        elif method == '<':
            self._method  = method
            return self._method
        else:
            InvalidMoveError()

    def opposite_turn(self):
        '''Returns the opposite color'''
        if self._turn == 'B':
            return "W"
        elif self._turn == 'W':
            return "B"
    
    def switchturn(self):
        ''' Switches turns within the object'''
        if self._turn == 'B':
            self._turn = 'W'
            return self._turn
        else:
            self._turn = 'B'
            return self._turn
    def move(self, row, column):
        ''' Process the users move and determines if its valid and acts on it'''
        if self._turn == "B":
            tile = 1
        if self._turn == "W":
            tile = 2
        if valid_move(self._turn,self._board, row, column) == True:
            flipped_tiles = captured_tiles(self._turn, self._board, row, column)
            for x,y in flipped_tiles:
                self._board[x][y] = tile
            self.switchturn()
            return self._board
            
            
    
    
    def scoreboard(self):
        ''' displays the scoreboard of the game'''
        black_score = 0
        white_score = 0
        for column in range(self._column):
            for row in range(self._row):
                if self._board[column][row] == 1:
                    black_score+=1
                elif self._board[column][row] == 2:
                    white_score +=1
        scoreboard = "B: {} W: {}".format(black_score, white_score)
        return black_score, white_score
    
    def winner_determine(self):
        ''' determines the winner'''
        black_score = 0
        white_score = 0
        for column in range(self._column):
            for row in range(self._row):
                if self._board[row][column] == 1:
                    black_score+=1
                elif self._board[row][column] == 2:
                    white_score +=1
                else:
                    pass
        if black_score == white_score:
            return 'None'
        if self._method == '>':
            if black_score > white_score == True:
                return 'B'
            else:
                return 'W'
        elif self._method == '<':
            if black_score < white_score == True:
                return 'B'
            else:
                return 'W'
        else:
            InvalidMoveError()
            
    def visualboard(self):
        '''presents the board in a user frindly manner'''
        for row in range(self._row):
            for column in range(self._column):
                if self._board[row][column] == 0:
                    print('.', end = ' ')
                elif self._board[row][column] == 1:
                    print('B', end= ' ')
                elif self._board[row][column] == 2:
                    print ('W', end= ' ')
            print()
    def valid_moves(self, turn):
        '''provides list of valid moves for the player'''
        moves = []
        for row in range(self._row):
            for column in range(self._column):
                if valid_move(turn,self._board, row, column) == True:
                    moves.append([row, column])
        return moves



def initial_error(Exception):
    print('Invalid Setup!')

def _move_is_on_board(board, row:int, col:int):
    row+=1
    col+=1
    if row >= 0 and row <= len(board) and col>=0 and col <= len(board[0]):
        return True
    else:
        return False
def _on_corner(o: Othello, row:int, col:int):
    if (row == 0 and col == 0) or (row == o._row and col == 0) or (row == 0 and col == o.col) or (row == o._row and col == o._col):
        return True
    else:
        return False


def valid_move(turn,board,row,column):
    ''' determines whether a move is valid or not according to the Othello rules'''
    if turn == "B":
        tile = 1
    elif turn == "W":
        tile = 2
    if tile == 1:
        opposite_tile = 2
    elif tile == 2:
        opposite_tile = 1
    else:
        InvalidMoveError()
    try:
        if board[row][column] != 0:
            return False        
        for x,y in directionals:
            row2 = row
            column2 = column
            row2 += x
            column2 += y
            if _move_is_on_board(board, row2, column2)==True:
                if board[row2][column2] == opposite_tile:
                    while board[row2][column2]== opposite_tile:
                        row2 += x
                        column2 += y
                        if _move_is_on_board(board, row2, column2)==True:
                            if board[row2][column2] == tile:
                                return True
        else:
            return False
    except:
        return False
            

def captured_tiles(turn, board, row, column):
    ''' collects all tiles which need to be flipped'''
    if turn == "B":
        tile = 1
    elif turn == "W":
        tile = 2
    captured_tiles = [(row,column)]
    if tile == 1:
        opposite_tile = 2
    elif tile == 2:
        opposite_tile = 1
        
    for x,y in directionals:
        column2 = column
        row2 = row
        row2 += x
        column2 += y
        if _move_is_on_board(board, row2, column2)==True:
            try:
                if board[row2][column2] == opposite_tile:
                    while board[row2][column2] == opposite_tile:
                        row2 += x
                        column2 += y
                        if _move_is_on_board(board, row2, column2)==True:
                            if board[row2][column2] ==  tile:
                                while True:
                                    row2 -= x
                                    column2 -= y
                                    if row2 == row and column2 == column:
                                        break
                                    captured_tiles.append([row2, column2])
            except:
                pass
    return captured_tiles
