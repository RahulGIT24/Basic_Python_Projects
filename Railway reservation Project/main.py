import random
import time

class Train:
    TrainName = "GUPTA EXPRESS"
    seats = 45
    Fare = "750 Rs."
    
    def __init__(self, uniqueid,destination):
          self.UniqueID = uniqueid
          self.Destination = destination
    
    def train_info(self):
           print(f'''************************ \tTRAIN INFORMATOIN IS SHOWN BELOW ************************
NAME OF THE TRAIN IS: {self.TrainName}
CURRENTLY SEATS AVILABLE IN TRAIN ARE: {self.seats}
FARE FOR 1 TICKET IS: {self.Fare}
DESTINATION: {self.Destination}''')
        
    def Book_ticket(self):
        bookTicket = int(input("Enter the number of tickets you want to book: "))
        '
    def cancel_ticket(self):
        pass
    @staticmethod
    def welcomeMsg():
        print('''\t******************************* WELCOME TO GUPTA EXPRESS ONLINE RESERVATION PORTAL *******************************
1) GET TRAIN INFROMATION                                                                                  2) BOOK TICKETS
3) CANCEL TICKETS                                                                                         4) EXIT PORTAL''')
        
Numbers = "1234567890"
length = 6
unique = "".join(random.sample(Numbers, length))
ID = "5510"+unique

guptaExpress = Train(ID,"DELHI TO PUNE")
guptaExpress.welcomeMsg()
time.sleep(2)



select = int(input("Enter your Choice\n"))
if (select == 1):
        print("Loading.....")
        time.sleep(2)
        guptaExpress.train_info()
elif (select == 2):
        guptaExpress.Book_ticket()
elif (select == 3):
        guptaExpress.cancel_ticket()
elif (select == 4):
        print("\t#############################################  Thanks for using our portal  #############################################")
        time.sleep(3)
        exit()
else: 
        print("Enter a valid number!!!!!") 
