import random

def damage_system():
    base_health = 100
    damage = random.randint(0,100)
    new_health = base_health - damage

    print("\nDamage taken: " + str(damage))
    print("Health remaining: " + str(new_health))


answer = input("Would you like to take damage? (y/n) ")

if answer == "y":
    damage_system()
else:
    exit()
