#import the stuff
#quote of the update: "java is just C but no"

# todo: add more microapps

import termios
import select
import psutil
import sys
import calculator_microapp
import randomnumber_microapp
import tty
import os
import random

temp3 = "0"
text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%^&*()-_+=[];:'@#~/?.>,<`¬"


#i will learn what this means later...
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr

#get username
try:
    with open("usr.dat", "r") as usrn:
        usr = usrn.read()
except FileNotFoundError:
    with open("usr.dat","w+") as usrn:
        usrn.write(input("Enter username: "))
        usr = usrn.read()

#get password
try:
    with open("pas.dat", "r") as pasw:
        passw = pasw.read()
except FileNotFoundError:
    with open("pas.dat", "w+") as pasw:
        temp = input("Enter password: ")
        for pop in temp:
            for i in range(3):
                bib = random.choice(text)
                temp2 = pop + bib
            del bib
            pasw.write(temp2)
        passw = pasw.read()
with open("pas.dat", "r") as pasw:
    passw = pasw.read()

#create password function
def createpassword(password):
    with open("pas.dat", "w") as pasw:
        for cak in password:
            for i in range(3):
                bib = random.choice(text)
                temp2 = cak + bib
            del bib
            pasw.write(temp2)

#decrypting password
print(f"Entering as {usr}")
for i in passw[::2]:
            temp3 = temp3 + i

#authentification
while True:
    temp = input(f"Enter password for {usr} or type 'change' to change it: ")
    if temp.lower() == "change":
        tr = input("Enter password first:")
        if "0" + tr == temp3:
            change = str(input("What do you want to change your password to?: "))
            createpassword(change)
            break
        else:
            print("Incorrect password")
            next
    else:
        if "0" + temp == temp3:
             break
        else:  
            print("Incorrect password")

#list of commands for cleaner code
helplist = [
    "ver",
    "raminf",
    "esc",
    "cpuinf",
    "help" ,
    "whoami" ,
    "liveram" ,
    "ls microapp" ,
    "run microapp"
    ""
]

print("booted")
#main loop
while True:
    print('')
    cmd =  input(f"{usr}@pyggy:~$ ")
    if cmd == "ver":
        print("alpha_0.14")
    elif cmd == "raminf":
        mem = psutil.virtual_memory()
        print(str(mem.percent)+"%" " in use of", mem.total)
      
    elif cmd == "esc":
        sys.exit()
    elif cmd == "ls microapp":
        print("Calculator")
        print("Random Number Generator (name is rng)")
    elif cmd == "cpuinf":
        print(psutil.cpu_count(), "cores")
    elif cmd == "help":
        for word in helplist:
            print(word)
    elif cmd == "whoami":
        print(usr)
    elif cmd == "run microapp":
        print("Which microapp do you want to run or type esc to exit")
        while True:
            MATR = input("<run microapp>:~$ ")
            if MATR.lower() == "calculator":
                break
                calculator_microapp.calculation(usr)
            elif MATR.lower() == "esc":
                break
            elif MATR.lower() == "rng":
                break
                randomnumber_microapp.getrandnum(usr)
            else:
                print(f"Unkown microapp: {MATR}")
    elif cmd == "liveram":
        while True:
            tty.setcbreak(fd)
            #this really damn annoyed me: its finally fixed: probably
            mem = psutil.virtual_memory()
            print(f"\rram: {mem.percent}%", end="")
            if select.select([sys.stdin], [], [], 0)[0]:
               sys.stdin.read(1)  # consume the key (om nom nom)
               break
    else:
        print(f"Unkown command: {cmd}")
# i have to add these cos everyone likes comments