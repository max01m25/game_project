import game_board


def game():
    keys=[0,0]
    player_health = 100
    while True:

    #STAGE1 
        print('========================STAGE I========================')
        one,health = game_board.starting(keys,player_health)
        if one==1:
            print("You've earned a key to second stage!")
            print()
            keys[0]=1 
            player_health=health
        else:
            break

    #STAGE2
        print('========================STAGE II========================')
        two,health = game_board.starting(keys,player_health)
        if two==1:
            print("You've earned a key to third stage!")
            print()
            keys[1]=1  
            player_health=health
        else:
            break

    #STAGE3
        print('========================STAGE III========================')
        three,health = game_board.starting(keys,player_health)
        if three==1:
            print("You have won the game!")

        break


game()