import random
import user_input
import time



def fight(player_health):
    enemy_health = random.randint(10, 101)
    print(f"Your state of health before the fight: {player_health}, and your enemy: {enemy_health}")
    
    while enemy_health>0 and player_health>0: 
        damage_enemy=random.randint(1, 101)
        
        print("Fight till someone will be destroyed!")
        print(f"Damage: {damage_enemy}")
        time.sleep(1.5)
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
        #player_health = fight_result_person
        return True, player_health
    elif enemy_health>0:
        time.sleep(2)
        print(f"Your health after the fight is {player_health}, the enemy has {enemy_health}. You lost")
        return False, 0
    elif enemy_health==player_health:
        coin = user_input.get_positive_int("It´s a tie. We flip a coin: 1 for head or 2 for tail\nYour guess: ")
        while coin != 1 and coin != 2:
            coin = user_input.get_positive_int("It´s a tie. We flip a coin: 1 for head or 2 for tail\nYour guess: ")
        coin_flip = random.randint(1,3)
        if coin == coin_flip:
            #if enemy and player has 0 health, then if coin flip is guessed, player needs a recovery health to still play a game
            player_health=random.randint(50,101)   
            
            print(f"True, you won and earn health points! Your state of health now is: {player_health}")
            return True, player_health
        else:
            print("Wrong, you lost.")
            return False, 0


def drop():
    print("You found a chest! Let's open it!")
    time.sleep(1.5)
    health = 0
    drop_set=["health","nothing"]
    prize=random.choice(drop_set)
    if prize==drop_set[0]:
        health=random.randint(15,41)
        print(f"You've gained {health} additional health! ")
    else:
        print("The chest was empty!")
    return health






        