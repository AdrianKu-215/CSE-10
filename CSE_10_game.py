#newwork
import random
import sys
import time
def slow(text):
    print(text)
    time.sleep(1.2)
health = 1000
attack = 100
coins =  random.randint(50,100)
monster1 = False
strongmonster = False
toll = 0
potion = random.randint(1,99)
sword = int(attack + 1000)
demonking = 0
if health == 0:
    slow("you've ran out of health, better luck next time")
    sys.exit()
slow("your health is ",health,", your attack power is ",attack,", and you currently have ",coins,"coins.")
