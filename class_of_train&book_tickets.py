'''class of train which has methods to book a ticket, get statics(NO OF SEATS)and get fare info 
of trains running under indian railway'''




class Train:
  
    def __init__(self, name, fare, seats):
      self.name = name  
      self.seats = seats
      self.fare = fare
      self.seatnumber = 0
  
  
    
    def getstatus(self):
      print("_____________________________________")
      print(f"The name of the train is {self.name}")
      print(f"The number of seats is available in the train are {self.seats}")
      print("_____________________________________")
   
  
    
    def fareinfo(self):
      print(f"Price of the ticket is {self.fare}")

  
    
    def bookticket(self):
      if(self.seats>0):
        self.seatnumber+=1
        print(f"Your ticket has been booked and your seat number is {self.seatnumber}")
        self.seats = self.seats - 1

      else:
        print("Sorry this train is full kindly try in tatkal")
  
  
    
    def cancelticket(self, canceled_ticket):
       self.seats+= canceled_ticket
       print(f"Number of seats {self.seatnumber} canceled")


intercity = Train("intercity express : 14055",99,300)
intercity.getstatus()
intercity.fareinfo()
intercity.bookticket()
intercity.bookticket()
intercity.cancelticket(2)
intercity.getstatus()