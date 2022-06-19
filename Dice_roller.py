import random
import time

while True:
    randnumber = random.randint(1, 6)
# print(randnumber)

    print("Press 'q' to Quit..")
    dice = input("Press 'd' to roll dice\n")

    if dice == "d".lower():
        pass
        if randnumber == 1:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 1")
        elif randnumber == 2:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 2")
        elif randnumber == 3:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 3")
        elif randnumber == 4:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 4")
        elif randnumber == 5:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 5")
        elif randnumber == 6:
            print("Rolling............")
            time.sleep(1)
            print("YOU GOT 6")
    elif dice == "Q".lower():
        print("********************************* Thanks for using *********************************")
        time.sleep(1)
        exit()
