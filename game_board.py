from random import randint

def create_board():
    board = []
    for x in range(BOARDHEIGHT):
        board.append(['0'] * BOARDWIDTH)
    return board

# Create the constants 
BOARDWIDTH = 5  # number of columns in the board
BOARDHEIGHT = 5 # number of rows in the board
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'q'
player = [BOARDHEIGHT-1,round(BOARDWIDTH/2)]
MOVES = "Move: w-up, s-down, a-left, d-right,q-exit.\nChoice: "
board = create_board()
marked = []  # it contains all the fields which were visited by the player.

"""
ENEMIES ARE PLACED AND SEEN ONLY FOR VISUAL PURPOSES, as it is a starting point to develop the board. 
Chests will be put also in the similar way as enemies (keep in mind that we cannot put
chests and enemies in places occupied by something else, or in the player's initial position.)

They won't be seen on the board. Only the position of the player will be seen, can be indicated 
by the symbol X(right now) or anything else. It can be also a symbol indicated by the player at the beginning of the game ;) 





to do:
1) when there is a fight:
-> win : delete enemy from ENEMIES list
-> lose : end the game

2) finding a chest case

3) all fields explored, key found, going to the "starting point" or winning the game.
4) exit the stage by the player. ( EXIT )
"""



def print_board(board):
    for row in board:
        print (" ".join(row))



#print_board(board)


def player_position():
    # Return the row and column of board coordinates of the player
    return player



def is_valid_move(board, move):
    pos_x, pos_y = player_position()
    return (move == RIGHT and pos_y != len(board[0]) - 1) or \
           (move == LEFT and pos_y != 0) or \
           (move == DOWN and pos_x != len(board) - 1) or \
           (move == UP and pos_x != 0)

def give_move():
    moves =  [UP,DOWN,RIGHT,LEFT,EXIT]
    while True:
        move =  input(MOVES)
        if move in moves:
            break
    return move

def append_write_show(marked, board, p_x,p_y):
    x= [p_x,p_y]
    if x not in marked:
        marked.append(x)
    board[p_x][p_y]='0'
    print_board(board)


def make_move(board, move,player):
    
    p_row, p_col = player_position()
    while True:
        if move == UP and is_valid_move(board,move):
            next_pos =place_player(p_row-1,p_col, player)
            if next_pos in ENEMIES:
                print("YOU HAVE TO DESTROY THE ENEMY")  #only to indicate that player is on a field with the enemy.

               #place to do the fight or opening a chest, etc.
                
            board[p_row-1][p_col]='X'
            append_write_show(marked,board,p_row,p_col)
            break
        elif move == DOWN and is_valid_move(board,move):
            next_pos =place_player(p_row+1,p_col, player)
            if next_pos in ENEMIES:
                print("YOU HAVE TO DESTROY THE ENEMY")
            #place to do the fight or opening a chest, etc.
            board[p_row+1][p_col]='X'
            append_write_show(marked,board,p_row,p_col)
            break
        elif move == LEFT and is_valid_move(board,move):
            next_pos =place_player(p_row,p_col-1, player)
            if next_pos in ENEMIES:
                print("YOU HAVE TO DESTROY THE ENEMY")
            
            # place to do the fight or opening a chest, etc.
            board[p_row][p_col-1]='X'
            append_write_show(marked,board,p_row,p_col)
            break
        elif move == RIGHT and is_valid_move(board,move):
            next_pos =place_player(p_row,p_col+1, player)
            if next_pos in ENEMIES:
                print("YOU HAVE TO DESTROY THE ENEMY")
             #place to do the fight or opening a chest, etc.

            
            board[p_row][p_col+1]='X'
            append_write_show(marked,board,p_row,p_col)
            break
        else:
            print("invalid move")
            break


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def place_enemy():
    enemy_row = random_row(board)
    enemy_col = random_col(board)
    position= [enemy_row,enemy_col]
    
    return position

ENEMIES = []



def place_enemies(ENEMIES):
    while True:
        x=place_enemy()
        if x not in ENEMIES and x!=player:
            position_enemy = x
            ENEMIES.append(position_enemy)
            break
    return position_enemy



def starting_position(player,board):
    board[player[0]][player[1]] = 'X'


def place_player(row,col, player):
    player[0]=row
    player[1]=col
    return [row,col]
    


"""
w- forward(up)
a- left
d- right
s- backwards
q- exit

"""
starting_position(player,board)


e1 = place_enemies(ENEMIES)
#print("enemy 1",e1)
e2 = place_enemies(ENEMIES)
#print("enemy 2", e2)
e3 = place_enemies(ENEMIES)
#print("enemy 3", e3)

board[e1[0]][e1[1]] = 'E1'
board[e2[0]][e2[1]] = 'E2'
board[e3[0]][e3[1]] = 'E3'

print('\n')
print_board(board)

while True:
    mo = give_move()
    if mo!=EXIT:
        make_move(board,mo,player)
    elif mo==EXIT:
        break




