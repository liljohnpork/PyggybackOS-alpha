import random

def getrandnum(usr):
    print("What is the first parameter?")
    while True:
        try:
            firstpar = int(input(f"{usr}@pyggy:~$ "))
        except ValueError:
            print("That isn't a number.")
        else: break
    print("What is the second parameter?")
    while True:
        try:
            secpar = int(input(f"{usr}@pyggy:~$ "))
        except ValueError:
            print("That isn't a number.")
        else: break
    try:
        randnum = random.randint(firstpar, secpar)
        print(f"Your random number between {firstpar} and {secpar} is {randnum}")
    except ValueError:
        print("Dude how've you done this. Probably the first parameter is bigger than the second? idk")