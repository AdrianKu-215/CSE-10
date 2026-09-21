#newwork
import random
import sys
import time
def slow(text):
    print(text)
    time.sleep(1.2)
health = 1000
attack = 100
coins =  random.randint(100,150)
monster1 = False
strongmonster = False
toll = 0
potion = random.randint(1,99)
sword = int(attack + 1000)
demonking = 0
shop = 0
sword = False
potion = False

if health == 0:
    slow("you've ran out of health, better luck next time")
    sys.exit()

name = input("Welcome traveler, you are now in a magical land. Your objective is to defeat the demon king, what is your name : ")
print("Alright " ,name, " your journey begins now, you have ",health," health, ",attack," attack power, and ",coins," coins.")
choice1 = input("You encounter a monster, do you want to fight it or run away? (fight/run) : ")
if name == "adrian":
    health += 10000
    attack += 10000
    coins += 10000
    slow("You have been given a special boost for being the creator of this game! You now have " + str(health) + " health, " + str(attack) + " attack power, and " + str(coins) + " coins.")
    
if choice1.lower() == "fight":
    monster1 = True
    slow("You have chosen to fight the monster!")
    slow("The monster has 500 health and 50 attack power.")
    while monster1:
        choice2 = input("Do you want to attack or use a potion? (attack/potion) : ")
        if choice2.lower() == "attack":
            slow("You attack the monster!")
            monster_health = 500 - 100
            slow("The monster now has " + str(monster_health) + " health left.")
            slow("The monster attacks you back!")
            health -= 50
            slow("You now have " + str(health) + " health left.")
            if monster_health <= 0:
                slow("You have defeated the monster!")
                coins += random.randint(10,50)
                slow("You have gained some coins! You now have " + str(coins) + " coins.")
                monster1 = False
        elif choice2.lower() == "potion":
            if potion > 0:
                health += 100
                potion -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        else:
            slow("Invalid choice, please choose again.")
if choice1.lower() == "run":
    slow("You have chosen to run away from the monster.")

choicestrongmonster = input("You encounter a strong monster, do you want to fight it or run away? (fight/run) : ")
if choicestrongmonster.lower() == "fight":
    strongmonster = True
    slow("You have chosen to fight the strong monster!")
    slow("The strong monster has 1000 health and 100 attack power.")
    while strongmonster:
        choice3 = input("Do you want to attack or use a potion? (attack/potion) : ")
        if choice3.lower() == "attack":
            slow("You attack the strong monster!")
            strong_monster_health = 1000 - attack
            slow("The strong monster now has " + str(strong_monster_health) + " health left.")
            slow("The strong monster attacks you back!")
            health -= 100
            slow("You now have " + str(health) + " health left.")
            if strong_monster_health <= 0:
                slow("You have defeated the strong monster!")
                coins += random.randint(50,100)
                slow("You have gained some coins! You now have " + str(coins) + " coins.")
                strongmonster = False
        elif choice3.lower() == "potion":
            if potion > 0:
                health += 100
                potion -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        else:
            slow("Invalid choice, please choose again.")
if choicestrongmonster.lower() == "run":
    slow("You have chosen to run away from the strong monster.")

toll = random.randint(101,125)
slow("You encounter a toll bridge, you need to pay " + str(toll) + " coins to cross it.")
if coins >= toll:
    coins -= toll
    slow("You have paid the toll and crossed the bridge. You now have " + str(coins) + " coins left.")
else:
    slow("You don't have enough coins to pay the toll. You cannot cross the bridge.")
    sys.exit()

shop = input("You encounter a shop, do you want to buy a potion for 50 coins or a sword for 100 coins? (potion/sword/none) : ")
if shop.lower() == "potion":
    if coins >= 50:
        coins -= 50
        health += 500
        slow("You have bought a potion! You now have " + str(potion) + " potions and " + str(coins) + " coins left.")
    else:
        slow("You don't have enough coins to buy a potion.")
elif shop.lower() == "sword":   
    if coins >= 100:
        coins -= 100
        attack += 1000
        sword = True
        slow("You have bought a sword! Your attack power is now " + str(attack) + " and you have " + str(coins) + " coins left.")
    else:
        slow("You don't have enough coins to buy a sword.")
elif shop.lower() == "none":
    slow("You have chosen not to buy anything from the shop.")

if sword == True:
    slow("You have a sword, your attack power is now " + str(attack) + ".")
if potion == True:
    slow("You have a potion, your health is now " + str(health) + ".")

demonking = input("You encounter the demon king, do you want to fight it or run away? (fight/run) : ")
if demonking.lower() == "fight":
    slow("You have chosen to fight the demon king!")
    slow("The demon king has 2000 health and 200 attack power.")
    while True:
        choice4 = input("Do you want to attack or use a potion? (attack/potion) : ")
        if choice4.lower() == "attack":
            slow("You attack the demon king!")
            demon_king_health = 2000 - attack
            slow("The demon king now has " + str(demon_king_health) + " health left.")
            slow("The demon king attacks you back!")
            health -= 200
            slow("You now have " + str(health) + " health left.")
            if demon_king_health <= 0:
                slow("You have defeated the demon king! Congratulations, you have completed your journey!")
                break
        elif choice4.lower() == "potion":
            if potion > 0:
                health += 100
                potion -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        else:
            slow("Invalid choice, please choose again.")
if demonking.lower() == "run":
    slow("You have failed your journey, better luck next time.")
