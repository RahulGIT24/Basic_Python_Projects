while(True):
    import random

    def gamewin(comp, you):
        if you == comp:
            return None

        elif comp == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True

        elif comp == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True

        elif comp == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True

    print("Comp turn Snake(s) Water (w) Gun(g)")
    randno = random.randint(1, 3)
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'w'
    elif randno == 3:
        comp = 'g'

    you = input("Your turn:  Chose Snake(s) Water (w) or Gun (g)\n")
    print(f"Comp chose {comp}")
    print(f"You chose {you}")

    a = gamewin(comp, you)
    if a == None:
        print("Tie!")
    elif a == True:
        print("You won")
    else:
        print("you lose")
