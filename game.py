import random
import sys
import os
from models import *
from incidents import incident_generator
name=input("Type Your Name..")
print("Hello,",name,"!")
weapons=[
    Weapon("Dart",10,10),
    Weapon("Cannon",25,20),
    Weapon("Gun",30,30)
]
armours=[
    Armour("Leather",5,5),
    Armour("Chain",10,10),
    Armour("Plate",15,15)
]
enemies=[
    Enemy("Goblin",health=100,damage=10,precision=5),
    Enemy("Skeleton",150,15,10), 
    Enemy("Zombie",200,20,15),
    Enemy("Dragon",300,50,20)
]
#事件
#事件列表
def shop():
    print("Welcome to the Shop!")
    print("We have the following items for sale:")
    for i in range(len(weapons)):
        print(i+1,".",weapons[i].name,"for",weapons[i].damage,"points of damage")
    for i in range(len(armours)):
        print(i+1,".",armours[i].name,"for",armours[i].defense,"points of defense")
    choose=input("Which item do you want to buy? ")
    if(choose=="1"):
        
        return {"Desp":"You bought a new weapon!", "Battle":False, "Shop":True, "Item":weapons[0]}
    elif(choose=="2"):
        return {"Desp":"You bought a new armour!", "Battle":False, "Shop":True, "Item":armours[0]}
    else:
        choose=input("built your weapon?")
        if(choose=="1"):
            pass
def battle():
    pass
incident=[
    shop,
    battle
]
import copy
armour_u=random.choice(Armour)
weapon_u=random.choice(weapons)
health=1000
days=0
while True:
    i=incident[random.randint(0,1)]
    print(i['Desp'])
    if(i['Battle']):
        Enemy=copy.deepcopy(random.choice(enemies))
        print("Enemy",Enemy['name'],"is here! It has",Enemy['health'],"HP and ",Enemy['damage'],"points of damage")
        print("Your",weapon_u['name'],"is",weapon_u['damage'],"points of damage!")
        print("Your",armour_u['name'],"is",armour_u['defense'],"points of defense!")
        print("Now Battle...")
        while Enemy["health"]>=0 and health>=0:
            Enemy['health']=Enemy['health']-weapon_u['damage']
            health=health-Enemy['damage']/(1+armour_u['defense']/200)
        if(Enemy['health']<=0 and health>=0):
            print(health,"HP left!")
            print("Win! Next day...\n")
            os.system("pause")
        else:
            print("Lose... End Exploring!")
            print(name,",You survived for ",days," Days.")
            break
    elif(i["Shop"]):
        print("Your",weapon_u['name'],"is",weapon_u['damage'],"points of damage!")
        print("Your",armour_u['name'],"is",armour_u['defense'],"points of defense!")
        print("You can get a new weapon! Will you choose?")
        choose=input("[y/...]")
        if(choose=="y"):
            weapon_u=random.choice(weapons)
            print("Your",weapon_u['name'],"is",weapon_u['damage'],"points of damage!")
        print("You can get a new armour! Will you choose?")
        choose=input("[y/...]")
        if(choose=="y"):
            armour_u=random.choice(Armour)
            print("Your",armour_u['name'],"is",armour_u['defense'],"points of defense!")
    days=days+1
        