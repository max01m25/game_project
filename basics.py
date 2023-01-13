import random

name=str(input("Write yout name: "))

print(f"Hello, {name}")

f=open("beginning.txt","r")
text=f.read()
print(text)
f.close()

   
key1=0
key2=0
key3=0
lastkey=0   
health=0             
drop_set=["health","nothing","health","nothing","Forest key"]

def drop():
    prize=random.randint(0,len(drop_set))
    if(prize-1=="Forest key"):
        drop.pop(-1)
    if(prize-1=="health"):
        health+=1   
    return drop_set[prize-1]

def haul():
    f=open("ending.txt","r")
    text=f.read()
    print(text)
    f.close()

def house():
    print("Your have discovered a house. What area do you want to explore:")
    decision=int(input("0: East, 1: North: "))
    while (decision!=0 and decision!=1):
        decision=int(input("1: East, 2: North: "))
    
    if(decision==0):
        print("You sourround the house")
        print(f"You find a chest: with {drop()} \n")
        decision=1
    
    if(decision==1):
        print("You open the door")
        print("You found an enemy, you must fight!")
        
        print("You won this fight!")
    
    
    return starting_point()


def starting_point():
    selection=int(input("Select options 1, 2, 3 or 4: "))
    
    if(selection==1 and key1==0):
        house()
    elif(selection==4 and lastkey==1):
        haul()
        exit()


starting_point()
