#import the stuff
#quote of the update: "wait what, this is C#?"

# todo: add more microapps

import termios
import select
import psutil
import sys
import calculator_microapp
import randomnumber_microapp
import tty

#i will learn what this means later...
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr

try:
    with open("usr.dat", "r") as usrn:
        usr = usrn.read()
except FileNotFoundError:
    with open("usr.dat","w+r") as usrn:
        usrn.write(input("Enter username: "))
        usr = usrn.read()
    
try:
    with open("pas.dat", "r") as pasw:
        passw = pasw.read()
except FileNotFoundError:
    with open("pas.dat", "w+") as pasw:
        pasw.write(input("Enter password: "))
        passw = pasw.read()

print(f"Entering as {usr}")
while True:
    temp = input(f"Enter password for {usr}: ")
    if temp == passw:
         break
    else:  
        print("Incorrect password")

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
#get it working
#loop for it
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