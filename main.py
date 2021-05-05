
print("WELCOME TO THE EDYODA MOVIE BOOKING!!")
print("WE BELIEVE YOU ENJOY THIS BOOKING PROCESS")



class Theatre:
    def options(self):
        print("Please make the below choices:")       ##CHOICES WHICH HELPS IN CALLING FUNCTION REPECTIVE OF CHOICES
        self.choice=int(input("\n1.Show seats:\n2.Buy a ticket:\n3.Statistics\n4.Show booked ticket user information:\n5.Exit1"))
        
        if self.choice==1:                          ##OBJECT METHODS
            self.show_seats()
        elif self.choice==2:
            self.Buy_tickets()
        elif self.choice==3:
            self.Statistics()
        elif self.choice==4:
            self.Info()
        elif self.choice==5:
            self.exit()
        else:
            print("Please make a valid choice:")
    def __init__(self):
        self.row=int(input("Enter the no. of rows:")) ##OBJECT METHODS FOR CALLING ROWS AND COLS OF THEATRE TO SHOW
        self.col=int(input("Enter the no. of cols:"))
        self.matrix=[]                                 ##OBJECT METHOD
        self.no_of_seats=self.row*self.col              ##TOTAL SEATS
        self.seat_count=0
        self.y_dict={}
        self.ticket=[0]
        
       
    def show_seats(self):                            ## SHOWS SEATS WHICH ARE VACANT
        self.st=['s']
        self.matrix=[0]*self.row
        for j in range(self.row):
            self.matrix[j]=self.st*self.col
        for l in self.matrix:
            print(l)
    
    
    def Buy_tickets(self):                      ##SHOWS BOOKING PROCEDURE TO FOLLOW TO BOOK THE TICKETS
        y_dicts={}
        self.R=int(input("Enter the row you want to book:"))
        self.T=int(input("Enter the column of seat you want to book:"))
        if self.row*self.col<=60:
            print("Price of seat will be $10")
        elif self.row<=self.col/2:
            print("Price of this seat will be $10")
        else:
            print("Print price of ticket is $8")
            
        self.Row1=self.R-1
        self.Col1=self.T-1
           
        self.X=input("Do you want to book ticket??\n1.Press Y for yes\n2. Press any other key for no") 
        if self.X=='Y':
            v=input("Enter your name:")
            r=input('Enter your gender:')
            s=int(input("Enter age:"))
            g=int(input("Enter mobile no.:"))
            
        
       
            self.pick=["B"]                                 
            self.matrix[self.Row1][self.Col1]=self.pick
            for p in self.matrix:
                print(p)
            self.matrix[self.Row1][self.Col1]="B"
            self.seat_count=self.seat_count+1
    
          
            y_dict[(self.row+1),(self.col+1)]=list((v,r,s,g))  #TAKING THE INFORMATION INTO DICTIONARY DATA TYPE
            self.y_dict.update(y_dicts)
            print("Booked sucessfully enjoy your movie!!\n\n")
            print("ok proceeding\n\n")
        else:
            print("Thanks visit again\n\n")
            
        
        
        
    
    
    def Statistics(self):                           ##STATISTICS 
        
        print("1.No. of tickets purchased:",self.seat_count)
                
        self.percentage=(self.seat_count/self.no_of_seats)*100
        print("2.Percentage tickets booked:",self.percentage)
        
        
        if self.row*self.col<=60:
            self.price=10*self.seat_count
        elif self.row<=self.row/2:
            self.price=10*self.seat_count
        else:
            self.price=8*self.seat_count
        
        print("3.Current income is:$",self.price)
        
        
        
        if self.row*self.col<=60:
            self.income=(self.row*self.col)*10
        else:
            self.income=((self.row/2)*(self.col))*10+((self.row/2)*(self.col))*8
        print("4.Total income",self.income)
        
        print("Make another choice if you want",self.options())
   

    def Info(self): 
        self.Buy_tickets()                                            #INFORMATION OF SEAT BOOKED
        self.check_a=int(input("enter the row you booked:"))
        self.check_b=int(input("enter the col you booked:"))
        if self.matrix[self.check_a][self.check_b]=='B':
            c=self.y_dicts[(self.check_a,self.check_b)]
            print('Name:',c[0])
            print('age:',c[1])
            print('gender:',c[2])
            print('Phone no.:',c[3])
        else:
            print("this seat is not booked yet:")
            
    def exit(self):
        return None
hey=Theatre()
hey.options()