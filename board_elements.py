import random
import user_input
import time



def fight(player_health):


    """
    Function responsible for the player's game against the enemy, 
    returns true and player_health when the player has won, otherwise returns False, player_health
    
    """
    enemy_health = random.randint(1, 100)
    print(f"Your state of health before the fight: {player_health}, and your enemy: {enemy_health}")
    print("Fight till someone will be destroyed!")
    while enemy_health>0 and player_health>0: 
        damage_enemy=random.randint(5, 15)
        time.sleep(1)
        print(f"Fight!")
        
        enemy_health -= damage_enemy
        player_health -= damage_enemy
        
        if enemy_health<0:
            enemy_health=0
        if player_health<0:
            player_health=0
        print(f"State of health:\nYou: {player_health}\nEnemy: {enemy_health}")  
        
     
    if player_health>0:
        time.sleep(2)
        print(f"Your health after the fight is {player_health}, the enemy has {enemy_health}. You won")
        return True, player_health
    elif enemy_health>0:
        time.sleep(2)
        print(f"Your health after the fight is {player_health}, the enemy has {enemy_health}. You lost")
        return False, player_health
    elif enemy_health==player_health:
        coin = user_input.get_positive_int("It´s a tie. We flip a coin: 1 for head or 2 for tail\nYour guess: ")
        while coin != 1 and coin != 2:
            coin = user_input.get_positive_int("It´s a tie. We flip a coin: 1 for head or 2 for tail\nYour guess: ")
        coin_flip = random.randint(1,2)
        if coin == coin_flip:
            #if enemy and player has 0 health, then if coin flip is guessed, player needs a recovery health to still play a game
            player_health=random.randint(50,100)   
            
            print(f"True, you won and earn health points! Your state of health now is: {player_health}")
            return True, player_health
        else:
            print("Wrong, you lost.")
            return False, player_health


def drop():

    """
    the function used if the chest is found on the board. The chest is opened: 
    it can be empty, or the player can gain additional health
    """

    print("You found a chest! Let's open it!")
    time.sleep(1.5)
    health = 0
    drop_set=["health","nothing"]
    prize=random.choice(drop_set)
    if prize==drop_set[0]:
        health=random.randint(20,50)
        print(f"You've gained {health} additional health! ")
    else:
        print("The chest was empty!")
    return health




#

        