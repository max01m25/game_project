import random
import board_elements
import user_input
import time


# Create the constants .
BOARDWIDTH = 5  # number of columns in the board
BOARDHEIGHT = 5 # number of rows in the board
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
board =[]
player = [BOARDHEIGHT-1,round(BOARDWIDTH/2)] #initial position of the player
MOVES = "Move: w-up, s-down, a-left, d-right. \nChoice: "

#Lists of elements on the board
ENEMIES = [] #list of enemies
CHESTS = []


STAT = 1 # variable dependent on a status of the player - can play, or has lost




def create_board():
    board = []
    for x in range(BOARDHEIGHT):
        board.append(['0'] * BOARDWIDTH)
    return board


def initialize_board(num_of_enemies,num_of_chests):
    """
    Initializes the board for every stage of the game
    """
    global player
    global board
    ENEMIES.clear()
    CHESTS.clear()
    board.clear()
    board = create_board()
    starting_position()
    player= player_position()
    place_elements(board,num_of_enemies,ENEMIES,ENEMIES)
    if num_of_chests!=0:
        place_elements(board,num_of_chests,CHESTS,ENEMIES)
    return board


def print_board(board):
    for row in board:
        print (" ".join(row))


def change_stat():
    """
    Changes player state to lost
    """
    global STAT
    STAT = 0


def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)



def place_element(board):
    """
    Gives a random position of one enemy/chest on the board
    """
    element_row = random_row(board)
    element_col = random_col(board)
    position= [element_row,element_col]
    
    return position



def place_elements(board,num,elements_list,to_check):
    """
    The function places the number of elements: enemies/chests on the board corresponding to the stage the player is in.    
    """
    for i in range(num):
        while True:
            x= place_element(board)
            if x not in elements_list and x not in to_check and x!=player:
                position = x
                elements_list.append(position)
                break


def starting_position():
    """
    Every time the new stage begins,function places the player in the middle of the last row 
    """
    global player
    global board
    player=[BOARDHEIGHT-1,round(BOARDWIDTH/2)]
    board[player[0]][player[1]] = 'X'


def place_player(row,col, player):
    player[0]=row
    player[1]=col
    return [row,col]


def player_position():
    """ 
    Returns the row and column of  the board coordinates of the player
    """
    return player



def is_valid_move(board, move):
    """ 
    Checks if a player has chosen a good and valid option
    """
    pos_x, pos_y = player_position()
    return (move == RIGHT and pos_y != len(board[0]) - 1) or \
           (move == LEFT and pos_y != 0) or \
           (move == DOWN and pos_x != len(board) - 1) or \
           (move == UP and pos_x != 0)


def give_move():
    """
    reads input of a player's inteded move
    """
    moves =  [UP,DOWN,RIGHT,LEFT]
    while True:
        print()
        move =  input(MOVES)
        move=move.lower()
        if move in moves:
            break
    return move



def write_show(board, p_x,p_y):
    board[p_x][p_y]='0'
    print_board(board)



def enemy_case(next_pos,player_health):
    
    print("YOU HAVE TO DESTROY THE ENEMY")  
    result,health = board_elements.fight(player_health)
    if result:
        ENEMIES.remove(next_pos)
        player_health=health
    else:
        change_stat()
    return player_health



def make_move(board, move,player_health):
    """
    The function is responsible for moving the player around the board 
    and calling the appropriate functions depending on the player's position
    """
    global player
    
    p_row, p_col = player_position()
    while True:
        if move == UP and is_valid_move(board,move):
            next_pos =place_player(p_row-1,p_col, player)
            if next_pos in ENEMIES:

                player_health= enemy_case(next_pos,player_health)


            if next_pos in CHESTS:
                x = board_elements.drop()
                CHESTS.remove(next_pos)
                player_health+=x

            board[p_row-1][p_col]='X'  #marking a player's position 
            write_show(board,p_row,p_col)
            
            break


        elif move == DOWN and is_valid_move(board,move):
            next_pos =place_player(p_row+1,p_col, player)
            if next_pos in ENEMIES:
                player_health=  enemy_case(next_pos,player_health)


            if next_pos in CHESTS:
                x = board_elements.drop()
                CHESTS.remove(next_pos)
                player_health+=x

            board[p_row+1][p_col]='X'
            write_show(board,p_row,p_col)
            
            break


        elif move == LEFT and is_valid_move(board,move):
            next_pos =place_player(p_row,p_col-1, player)
            if next_pos in ENEMIES:
                player_health=  enemy_case(next_pos,player_health)


            if next_pos in CHESTS:
                x = board_elements.drop()
                CHESTS.remove(next_pos)
                player_health+=x    

            board[p_row][p_col-1]='X'
            write_show(board,p_row,p_col)
            #return player_health
            break


        elif move == RIGHT and is_valid_move(board,move):
            next_pos =place_player(p_row,p_col+1, player)
            if next_pos in ENEMIES:
                player_health=  enemy_case(next_pos,player_health)

            if next_pos in CHESTS:
                x = board_elements.drop()
                CHESTS.remove(next_pos)
                player_health+=x 
            
            board[p_row][p_col+1]='X'
            write_show(board,p_row,p_col)
            break

        else:
            print("invalid move")
            break

    return player_health    



"""
w- forward(up)
a- left
d- right
s- backwards(down)
"""
def create_stage(num_enemies,player_health,num_chests):
    """
    Preprares each stage of the game: board initialization, enemies and chests (if needed) placement, 
    and then conducts the whole stage
    """

    global board
    board= initialize_board(num_enemies,num_chests)
    


    # for i in range(num_enemies):
    #     board[ENEMIES[i][0]][ENEMIES[i][1]]="E"+str(i+1)
    # if num_chests!=0:
    #     for i in range(num_chests):
    #         board[CHESTS[i][0]][CHESTS[i][1]]="C"+str(i+1)
    


    print()
    print_board(board)
    
    while True:
        if len(ENEMIES)==0:
            print("you destroyed every enemy!")
            break
        
        mo = give_move()
        print()
        player_health=make_move(board,mo,player_health)
        if STAT==0:
            print("You lost a game!")
            break 
    return player_health




def riddle():

    """Chooses randomly one riddle to be answered by the player after he succeeded in every stage of the game"""

    riddles= [["Write down the next number in the pattern: 2, 5, 10, 17, 26…","37"], 
    ["When my dad was 31, I was just 8 years old. Now his age is twice as old as my age. What is my present age?","23"],
    ["There is a three-digit number. The second is four times as big as the third number, while the first is three less than the second digit. What is the number?","141"],
    ["When Miguel was 6 years old, his little sister, Leila, was half his age. If Miguel is 40 years old today, how old is Leila?","37"],
    ["X is a three-digit number. The tens digit is 5 more than the ones digit. The hundreds digit is 8 less than the tens digit. What is X?","194"]]

    to_guess= random.randint(0,len(riddles)-1)
    riddl = riddles[to_guess]
    time.sleep(1)
    print("You have a riddle to guess if you want to win the whole game!")

    print(riddl[0])
    time.sleep(1)
    answ = user_input.give_non_empty_str("Your answer: ")
    answ=answ.strip()
    
    if answ == riddl[1]:
        print("You're right!")
        return True
    print("Wrong answer! You've failed!")
    return False




def starting(keys,player_health):

    """
    The Starting Point of the game, where player comes back after each stage won and goes to another stage
    """

    print("You are welcome in the Neutral Zone: the place where you can enter mysterious places.")
    #call here a method with the beginning file with short introduction about a game :)
    if keys==[0,0]:
            #Stage 1
            print("You enter the first stage: the Forest!")
            health =create_stage(1,player_health,0)
            return STAT,health 
    
    print()
    
    while True:

        stage = user_input.get_key("Select a number corresponding to key possesed:"+
        "\n1: forest  \n2: house \n3: cave \nAnswer: ")
        if stage==2 and keys==[1,0]:
            #Stage 2
            print("You enter second stage: the House")
            health=create_stage(1,player_health,2)
            break

        if stage==3 and keys==[1,1]:
            #Stage 3
            print("You enter the Cave, your last stage!")
            health=create_stage(3,player_health,0)

            break

        else:
            print("You cannot enter a stage which you have already visited or do not have a key to access it!")
            print()

    return STAT, health







