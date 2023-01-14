import game_board


def game():
    keys=[0,0]
    player_health = 100
    while True:

    #STAGE1 
        print('========================STAGE I========================')
        one,health = game_board.starting(keys,player_health)
        if one==1:
            bonus=25
            player_health=health+bonus
            print(f"You've earned a key to the second stage and you recover! You gain additional {bonus} health!")
            print()
            keys[0]=1 
            
        else:
            break

    #STAGE2
        print('========================STAGE II========================')
        two,health = game_board.starting(keys,player_health)
        if two==1:
            bonus=50
            player_health=health+bonus
            print(f"You've earned a key to the third stage and you recover! You gain additional {bonus} health!")
            print()
            keys[1]=1  
            
        else:
            break

    #STAGE3
        print('========================STAGE III========================')
        three,health = game_board.starting(keys,player_health)

        if three==1 :
            x= game_board.riddle()
            if x:
                print("You have won the game!")
            else:
                print("GAME OVER")
            
        break


game()
#.