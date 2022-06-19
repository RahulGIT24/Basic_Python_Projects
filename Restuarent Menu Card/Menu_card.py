import datetime


class menu_card:
    def __init__(self, choice):
        self.choice = choice

    @staticmethod
    def displayMenu():
        with open("menu.txt", "r") as f:
            print(f.read())


class customer:
    def choiceCheck(self):
        try:
            for i in range(1, 10):
                if i == c:
                    pass
        except Exception:
            print("Please enter a valid choice!")
            # break

# 1. MARGHERITA
    def order1(self): 
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering MARGHERITA Regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MARGHERITA REGULAR SIZE PIZZA
    *AMOUNT IS: 99 Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering MARGHERITA Medium size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MARGHERITA MEDIUM SIZE PIZZA
    *AMOUNT IS: 195 Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering MARGHERITA large size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MARGHERITA LARGE SIZE PIZZA
    *AMOUNT IS: 395 Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

# 2. DOUBLE CHEESE MARGHERITA
    def order2(self):
        r=165
        m=305
        l=495
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering DOUBLE CHEESE MARGHERITA regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED DOUBLE CHEESE MARGHERITA REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering DOUBLE CHEESE MARGHERITA Medium size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED DOUBLE CHEESE MARGHERITA MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering DOUBLE CHEESE MARGHERITA large size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED DOUBLE CHEESE MARGHERITA LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

# 3. CHEESE & CORN
    def order3(self):
        r=165
        m=305
        l=495
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering CHEESE & CORN regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED DOUBLE CHEESE CHEESE & CORN REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering CHEESE & CORN Medium size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED CHEESE & CORN MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering CHEESE & CORN large size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED CHEESE & CORN LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

# 4. FRESH VEGGIE
    def order4(self):
        r=165
        m=305
        l=495
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering FRESH VEGGIE regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FRESH VEGGIE REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering FRESH VEGGIE Medium size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FRESH VEGGIE MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering FRESH VEGGIE large size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FRESH VEGGIE LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

# 5. PANNER MAKHANI
    def order5(self):
        r=205
        m=385
        l=595
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering PANNER MAKHANI regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PANNER MAKHANI REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering PANNER MAKHANI Medium size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PANNER MAKHANI MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering PANNER MAKHANI large size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PANNER MAKHANI LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

#6. FARMHOUSE
    def order6(self):
        r=205
        m=385
        l=595
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering FARMHOUSE regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FARMHOUSE REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering FARMHOUSE Medium size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FARMHOUSE MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering FARMHOUSE large size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED FARMHOUSE LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

#7.MEXICAN GREEN WAVE
    def order7(self):
        r=205
        m=385
        l=595
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering MEXICAN GREEN WAVE regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MEXICAN GREEN WAVE REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering MEXICAN GREEN WAVE Medium size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MEXICAN GREEN WAVE MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering MEXICAN GREEN WAVE large size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED MEXICAN GREEN WAVE LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

# 8. PEPPY PANEER
    def order8(self):
        r=205
        m=385
        l=595
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering PEPPY PANEER regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PEPPY PANEER REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering PEPPY PANEER Medium size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PEPPY PANEER MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering PEPPY PANEER large size pizza. Your bill is in {name}.txt")
                with open("Bill.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED PEPPY PANEER LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")

#9. VEGGIE PARADISE
    def order9(self):
        r=205
        m=385
        l=595
        print(selectionOfSize)
        select = int(input(("Enter the size\n")))
        if select == 1:
                print(
                    f"Thanks for odering VEGGIE PARADISE regular size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED VEGGIE PARADISE REGULAR SIZE PIZZA
    *AMOUNT IS: {r} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} **************************************
    ''')

        elif select == 2:
                print(
                    f"Thanks for odering VEGGIE PARADISE Medium size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED VEGGIE PARADISE MEDIUM SIZE PIZZA
    *AMOUNT IS: {m} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** 
    ''')
        elif select == 3:
                print(
                    f"Thanks for odering VEGGIE PARADISE large size pizza. Your bill is in {name}.txt")
                with open(f"{name}.txt", 'w') as f:
                    f.write(f'''******************* VEGGIE PIZZAS *******************
    *YOU HAVE ORDERED VEGGIE PARADISE LARGE SIZE PIZZA
    *AMOUNT IS: {l} Rs.
    *PAYMENT TYPE CASH
    *TIME-- {time}
************************************** THANKS FOR ODERING {name} ************************************** ''')
        else:
            print("Sorry only three sizes are availabe here!")



time = datetime.datetime.now()
menu_card.displayMenu()
while True:
    menu=menu_card
    # print("Press 00 to quit:")
    name = input("Enter your name\n")
    try:
        c = int(input("\nEnter Your order: "))
    except Exception:
        print("Enter a valid number")
    selectionOfSize = ('''\t*********************************** SELECT SIZE OF PIZZA ***********************************
    1. Regular
    2.Medium
    3. Large''')
    menu_card(c)
    try:
        if c==1:
            customer.order1(c)
        elif c==2:
            customer.order2(c)
        elif c==3:
            customer.order3(c)
        elif c==4:
            customer.order4(c)
        elif c==5:
            customer.order5(c)
        elif c==6:
            customer.order6(c)
        elif c==7:
            customer.order7(c)
        elif c==8:
            customer.order8(c)
        elif c==9:
            customer.order9(c)
    except Exception:
        print("Enter a valid Choice!")


