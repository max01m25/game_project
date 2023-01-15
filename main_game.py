import game_board
import user_input
import files
import time
import Won
import Lose
def game():
    keys=[0,0]
    player_health = 100

    name = user_input.give_non_empty_str("What's your name?:\n")
    print(f"Hello {name}! Welcome in the game <Lost Forest>!")
    files.read_file("rules.txt")

    while True:

    #STAGE1 
        
        print('========================STAGE I========================')
        

        one,health = game_board.starting(keys,player_health)
        if one==1:
            bonus=25
            player_health=health+bonus
            
            print(f"You've earned a key to the second stage and you recover! You gain additional {bonus} health!")
            time.sleep(1)
            print()
            keys[0]=1 
            
        else:
            Lose.lose()
            break
        time.sleep(1.5)    
    #STAGE2
        print('========================STAGE II========================')
        two,health = game_board.starting(keys,player_health)
        if two==1:
            bonus=50
            player_health=health+bonus
            print(f"You've earned a key to the third stage and you recover! You gain additional {bonus} health!")
            time.sleep(1)
            print()
            keys[1]=1  
            
        else:
            Lose.lose()
            break

    #STAGE3
        print('========================STAGE III========================')
        three,health = game_board.starting(keys,player_health)

        if three==1 :
            x= game_board.riddle()
            if x:
                print("You have won the game!")
                Won.won()
            else:
                print("GAME OVER")
                Lose.lose()
            
        break


game()
#.
