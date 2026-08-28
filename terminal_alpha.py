#import the stuff
#quote of the update: "ngl i kinda want a better psu"
#todo: add something to save to actually use the user system for

import select
import psutil
import sys
from microapps import calculator_microapp, randomnumber_microapp, astronomy_calculator
import os
import random
from datetime import datetime
if os.name == "posix":
    import tty, termios
else:
    import msvcrt
temp3 = ""
text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%^&*()-_+=[];:'@#~/?.>,<`¬"
folder = os.path.expanduser("~/Documents/pyggylogs")
os.makedirs(folder, exist_ok=True)


#i will learn what this means later...
if os.name == "posix":
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr

#get username
try:
    with open(os.path.expanduser("~/Documents/usr.dat"), "r") as usrn:
        usr = usrn.read()
except FileNotFoundError:
    with open(os.path.expanduser("~/Documents/usr.dat"),"w+") as usrn:
        usrn.write(input("Enter username: "))
        usr = usrn.read()

#get password
try:
    with open(os.path.expanduser("~/Documents/pas.dat"), "r") as pasw:
        passw = pasw.read()
except FileNotFoundError:
    with open(os.path.expanduser("~/Documents/pas.dat"), "w+") as pasw:
        temp = input("Enter password: ")
        for pop in temp:
            for i in range(3):
                bib = random.choice(text)
                temp2 = pop + bib
            del bib
            pasw.write(temp2)
        passw = pasw.read()
with open(os.path.expanduser("~/Documents/pas.dat"), "r") as pasw:
    passw = pasw.read()

#create password function
def createpassword(password):
    with open(os.path.expanduser("~/Documents/pas.dat"), "w") as pasw:
        for cak in password:
            for i in range(3):
                bib = random.choice(text)
                temp2 = cak + bib
            del bib
            pasw.write(temp2)

def writeout(location, write):
    with open(os.path.expanduser(location), "w") as file:
        file.write(write)

#decrypting password
print(f"Entering as {usr}")
for i in passw[::2]:
            temp3 = temp3 + i

#authentification
while True:
    #print(temp3)
    temp = input(f"Enter password for {usr} or type 'change' to change it: ")
    if temp.lower() == "change":
        tr = input("Enter password first:")
        if tr == temp3:
            change = str(input("What do you want to change your password to?: "))
            createpassword(change)
            break
        else:
            print("Incorrect password")
            next
    else:
        if temp == temp3:
             break
        else:  
            print("Incorrect password")

#list of commands for cleaner code
helplist = [
    "ver - output version",
    "raminf - show some ram info",
    "esc - exit the system",
    "cpuinf - show some cpu inf",
    "help - show some useful commands" ,
    "whoami - show what user you are" ,
    "liveram - show live ram until a key press" ,
    "ls microapp - list some microapps" ,
    "run microapp - run a microapp",
    "diskinf - show some disk info"
    "osinf - show some basic info about your computer's operating system"
    ""
]

print("booted")
print("type help for commands")
#main loop
while True:
    print('')
    cmd =  input(f"{usr}@pyggy:~$ ")
    if cmd == "ver":
        print("alpha_0.20")

    elif cmd == "raminf":
        mem = psutil.virtual_memory()
        print(str(mem.percent)+"%" " in use of", str(round(mem.total/1000000)) + "MB")
        print(str(round(mem.available/1000000)) + "MB available")
        while True:
                    answ = input("Do you wish to write out to a file?\n           (y/n)\n             ")
        
                    if answ == "y":
                        nem = f"~/Documents/pyggylogs/raminf.log{datetime.now().strftime("%H:%M:%S")}.log"
                        tmp = f"RAM log for {datetime.now().strftime("%D.%m.%Y")} at {datetime.now().strftime("%H:%M:%S")}\n\n\n\n" + str(mem.percent)+"%" " in use of " + str(round(mem.total/1000000)) + "MB" + "\n" + str(round(mem.available/1000000)) + "MB were available" 
                        writeout(nem, tmp)
                        print(f"\nWrite successful to {nem}")
                        break
                    elif answ == "n":
                        break
                    else:
                        print(f"Invalid operation: {answ}")
      
    elif cmd == "esc":
        sys.exit()

    elif cmd == "ls microapp":
        print("Calculator")
        print("Random Number Generator (name is rng)")
        print("Astronomy Calculator")

    elif cmd == "cpuinf":
        print(psutil.cpu_count(), "cores")
        print(str(psutil.cpu_percent()) + "%" + " in use")
        while True:
            answ = input("Do you wish to write out to a file?\n           (y/n)\n             ")

            if answ == "y":
                nem = f"~/Documents/pyggylogs/cpuinf.log{datetime.now().strftime("%H:%M:%S")}.log"
                tmp = f"Cpu log for {datetime.now().strftime("%D.%m.%Y")} at {datetime.now().strftime("%H:%M:%S")}\n\n\n\n" + "Cores = " + str(psutil.cpu_count()) + "\n" + str(psutil.cpu_percent()) + "%" + " was in use"
                writeout(nem, tmp)
                print(f"\nWrite successful to {nem}")
                break
            elif answ == "n":
                break
            else:
                print(f"Invalid operation: {answ}")
                
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
                calculator_microapp.calculation(usr)
                break
            elif MATR.lower() == "esc":
                break
            elif MATR.lower() == "rng":
                randomnumber_microapp.getrandnum(usr)
                break
            elif MATR.lower() == "astronomy calculator":
                astronomy_calculator.astro_calculator()
                break
            else:
                print(f"Unkown microapp: {MATR}")

    elif cmd == "liveram":
        while True:
            tty.setcbreak(fd)
            #this really damn annoyed me: its finally fixed: probably
            mem = psutil.virtual_memory()
            print(f"\rram: {mem.percent}%", end="")
            if os.name == "posix":
                if select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.read(1)  # consume the key (om nom nom)
                    break
            else:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    break
    elif cmd == "diskinf":
        print(psutil.disk_io_counters())
        print(psutil.disk_partitions())
        print(psutil.disk_usage("/"))
    elif cmd == "osinf":
        print(os.name)
    else:
        print(f"Unkown command: {cmd}")
# i have to add these cos everyone likes comments