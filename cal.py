''' BUS PASSANGERS,  TICKETS AND FARE CALCULATOR'''

class bus:
    def __init__(self,pas,tic,fare,fare_deduction,net_profit):
        self.pas=pas
        self.tic=tic
        self.fare=fare
        self.fare_defuction=fare_deduction
        self.net_profit=net_profit
        
    def calculation(self):
        print(f"Total passengers are: {self.pas}")
        print(f"Total tickets available are: {self.tic}")
        print(f"Total fare is : {self.fare}")
        self.fare=self.fare-self.fare_defuction
        leave=int(input("Enter the passengers leabing the bus: "))
        enter=int(input("Enter the passengers onboarding the bus: "))
        if(leave>self.pas):print("Invalid input program terminated!!")
        elif(leave==self.pas):
            print("All passengers left the bus!!!")
            print(f"Now new fare is {self.fare}")
        elif(leave<self.pas):
            self.pas=(self.pas-leave)+enter
            self.tic=30-self.pas
            print(f"Now the new fare is {self.fare}")
            self.net_profit+=enter*self.fare
            print("Net Profit is ",self.net_profit)
            
    def stop1(self):
        print("\nEntering the first destination!!!\n")
        self.calculation()
        
    def stop2(self):
        print("\nEntering the second destination!!!\n ")
        self.calculation()
        
    def stop3(self):
        print("\nNow entering the second last destination!!!\n")
        self.calculation()
        
    def last(self):
        print("\nFinal Destination reached!!! ")
        print(f"Total passengers left are: {self.pas}")
     
    
    
pas=int(input("Enter the total number of passangers :"))
tic=int(input("Enter the remaining tickets available: "))
fare=int(input("Enter the fare ammount: "))
fare_deduction=int(input("Enter the fare deduction amount: "))

popo=bus(pas,tic,fare,fare_deduction,fare*pas)
popo.stop1()
popo.stop2()
popo.stop3()
popo.last()
