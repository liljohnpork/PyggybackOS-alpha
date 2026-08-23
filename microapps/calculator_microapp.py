#todo : add an "ans" feature and possibly more

def calculation(usr):
    while True:
        print("Add")
        print("Subtract")
        print("Multiply")
        print("Divide")
        print("What calculation type do you want to do?")
        type = input(f"{usr}@pyggy:~$ ")
        if type.lower() in ["add", "subtract", "divide", "multiply"]:
            break
        else: print("Unkown calculation type")
    print("What is the first number?")
    while True:
        try:
            numberone = int(input(f"{usr}@pyggy:~$ "))
        except ValueError:
            print("That is not a number")
        else: break
    print("What is the second number?")
    while True:
        try:
            numbertwo = int(input(f"{usr}@pyggy:~$ "))
        except ValueError:
            print("That is not a number!")
        else: break
    if type.lower() == "add":
        print(numberone + numbertwo)
    if type.lower() == "subtract":
        print(numberone - numbertwo)
    if type.lower() == "multiply":
        print(numberone * numbertwo)
    try:
        if type.lower() == "divide":
            print(numberone / numbertwo)
    except ZeroDivisionError:
        print("idk probably infinity. go ask a mathematician")