
# * Author-Rahul
# * Date-30-03-2022
# * Location-Mars

import time
import datetime
from playsound import playsound
import pywhatkit
import getpass


class ATM:

    Name = "Coder"
    Account_Number = 5500000689
    Address = "Silicon Valley"
    PhNo_ = 91000000299
    Pin = "1234"
    Balance = 45000
    Branch_Name = "Bank Of America"
    IFSC_Code = "HP000000339"


class ATM_user(ATM):

    def ac_info(self):
        account_info = (f'''******* Thanks for using Rahul's ATM *******
HI {ATM.Name}
Branch Name-- {ATM.Branch_Name}
Account Number-- {ATM.Account_Number}
IFSC Code--{ATM.IFSC_Code}
Your account balance is: {ATM.Balance}
Have a nice day! {ATM.Name}''')
        print(account_info)

    def withdraw(self):
        withdraw = int(
            input("Enter the amount you want to withdraw: "))
        if withdraw > ATM.Balance:
            print(
                f"Insufficient Balance. Your balance is {ATM.Balance}")
        else:
            print("Processing.....")
            playsound(
                "E:\Coding\Coding Projects\Python Projects\ATM machine\withdraw.mp3")
            ATM.Balance = ATM.Balance-withdraw
            print(
                f"{withdraw} withdrawn successfully. Now your balance is {ATM.Balance}")
            reciept = input(("Did you want receipt(y/n):  "))
            x = datetime.datetime.now()
            if reciept == 'Y'.lower():
                # *Downloads withdraw receipt
                with open(f"Withdraw {ATM.Name} receipt.txt", 'w') as f:
                    withdraw_reciept = (f'''******* Thanks for using Rahul's ATM *******
HI {ATM.Name}
Branch Name-- {ATM.Branch_Name}
Account Number-- {ATM.Account_Number}
IFSC Code--{ATM.IFSC_Code}
You have withdrawn Rs.{withdraw} on {x}
Now your account balance is {ATM.Balance}
Have a nice day! {ATM.Name}''')
                    f.write(withdraw_reciept)
                print(f"Receipt is in {ATM.Name}.txt")
            elif reciept == 'N'.lower():
                print(f"OK HAVE A NICE DAY {ATM.Name}")
            else:
                print("If you want to generate reciept press Y else N")

    def deposit(self):
        deposit = int(input("Enter amount you want to deposit: "))
        print("Processing.....")
        time.sleep(5)
        playsound(
            "E:\Coding\Coding Projects\Python Projects\ATM machine\deposit.mp3")
        ATM.Balance = ATM.Balance+deposit
        print(
            f"Amount deposited successfully. Now your balance is {ATM.Balance}")
        reciept = input(("Did you want receipt(y/n):  "))
        x = datetime.datetime.now()
        if reciept == 'Y'.lower():
            with open(f"Deposit {ATM.Name} receipt.txt", 'w') as f:
                deposit_receipt = (f'''******* Thanks for using Rahul's ATM ******* #*Downloads deposit receipt
HI {ATM.Name}
Branch Name-- {ATM.Branch_Name}
Account Number-- {ATM.Account_Number}
IFSC Code--{ATM.IFSC_Code}
You have deposited Rs.{deposit} on {x}
Now your account balance is {ATM.Balance}
Have a nice day! {ATM.Name}''')
                f.write(deposit_receipt)
            print(f"Receipt is in {ATM.Name}.txt")
        elif reciept == 'N'.lower():
            print(f"OK HAVE A NICE DAY {ATM.Name}")
        else:
            print("If you want to generate reciept press Y else N")

    def recharge_mobile(self):
        try:
            phone = int(input("Enter your Phone NUmber:  "))
            rcamt = int(input("Enter the amount:  "))
            print("Connecting to your Phone...")
            time.sleep(2)
            pywhatkit.sendwhatmsg(
                f"91+{phone}", f"Recharge Done for Rs.{rcamt}", 14, 28)
            playsound(
                "E:\Coding\Coding Projects\Python Projects\ATM machine\rcdone.mp3")
            ATM.Balance.__sub__(rcamt)
        except Exception as e:
            playsound(
                "E:\Coding\Coding Projects\Python Projects\ATM machine\Payment_Fail.mp3")
            print(f"{e}")

    def update(self):
        pin = getpass.getpass(prompt="Enter your ATM PIN: ")
        if pin == ATM.Pin:
            print(f'''What do you want to update?
1. Update Phone Number
2. Update address
3. Update Pin''')
            enter_choice = int(input("Enter your choice: "))
            if enter_choice == 1:
                old_phno = int(
                    input("Enter your old phone number: "))
                if old_phno == ATM.PhNo_:
                    new_phono = int(
                        input("Enter your new phone number: "))
                    print(
                        f"Phone Number Updated. New Phone no. is {new_phono}")
                    new_phono == ATM.PhNo_
                else:
                    print("Incorrect Phone Number!!")
            elif enter_choice == 2:
                old_address = input("Enter your old address: ")
                if old_address == ATM.Address:
                    new_address = input("Enter your new address: ")
                    print(
                        f"Address Updated. Your new address is {new_address}")
                    new_address == ATM.Address
                else:
                    print("Incorrect Address")
            elif enter_choice == 3:
                old_pin = getpass.getpass(prompt="Enter your old ATM PIN: ")
                if old_pin == ATM.Pin:
                    new_pin = getpass.getpass(
                        prompt="Enter your new ATM PIN: ")
                    print(
                        f"Pin Updated.")
                    new_pin == ATM.Pin
                else:
                    print("Incorrect pin")


atm = ATM
note = "The PIN is not visible to you. Just type it...."
while(True):
    welcomeMSG = (
        '''\t******************* WELCOME TO RAHUL'S ATM ******************''')
    print(welcomeMSG)
    options = ('''\t************ SELECT ANY OPTION ********************
    1. CHECK BALANCE                               2. WITHDRAW AMOUNT
    3. DEPOSIT AMOUNT                              4. Recharge Your Phone
    5.Update Account Info                          6. EXIT.....''')
    a = int(input("Enter your account number: "))
    if a == ATM.Account_Number:
        print(note)
        b = getpass.getpass(prompt="Enter the PIN: ")
        if b == atm.Pin:
            print(options)
            c = int(input("ENTER YOUR CHOICE\n"))
            if c == 1:
                ATM_user.ac_info(a)
            elif c == 2:
                ATM_user.withdraw(a)
            elif c == 3:
                ATM_user.deposit(a)
            elif c == 4:
                ATM_user.recharge_mobile(a)
            elif c == 5:
                ATM_user.update(a)
            elif c == 6:
                print(
                    "****************************** Thanks for using me ******************************")
                time.sleep(2)
                exit()
            else:
                print("Enter a valid choice!!")
        else:
            print("Incorrect Pin")
    else:
        print("Account Not found!!!!!")
