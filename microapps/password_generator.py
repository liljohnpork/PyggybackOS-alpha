def password_generator():
    import random

    print("----Password Generator----")
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
                  "v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","£","%","&","*","?"]

    password_length = random.randint(16, 24)
    for i in range(password_length):
        letter = random.randint(0, 41)
        print(characters[letter], end="")
