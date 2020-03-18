import csv
import xlrd
from statistics import mean
from statistics import stdev
import matplotlib.pyplot as lplt

class Applicant:    #class for applicant type object

    def get_data(self,Date,Month,Year):     #function to get data from the user
        print("____________________________________________________________________________")
        print("\t \t WELCOME TO RAILWAY RESERVATION SYSTEM")
        self.date=int(Date)
        self.month=int(Month)
        self.year=int(Year)
        self.name=input("Enter your name:")
        self.age=int(input("enter your age:"))
        self.sex=input("enter your sex:")
        self.id=input("please do enter your Unique ID no:")
        self.seats_required=1
        print("____________________________________________________________________________")
        print("""\nyou have successfully applied for the train tickets
please do wait for further updates and your request will be processed soon
                    THANK YOU!!!""")
              
              
class Passenger:            #class for Passenger type object
    def __init__(self):     #constructor for Passenger class
        self.pdetails=None
        self.p_id=None
        self.right=None
        self.left=None        
            
    def data_copy(self,applicant):          #function to copy data from applicant to pdetail attribute in passenger
        self.p_id=train[i].total_p_count
        self.pdetails.name=applicant.name
        self.pdetails.age=applicant.age
        self.pdetails.sex=applicant.sex
        self.pdetails.id=applicant.id
        self.pdetails.seats_required=int(applicant.seats_required)
        self.pdetails.date=int(applicant.date)
        self.pdetails.month=int(applicant.month)
        self.pdetails.year=int(applicant.year)

    def copy_without_p_id(self,applicant):      #function to copy data from applicant type object to pdetail attribute
                                                #in passenger type object(in the case of inserting in a cancelled ticket)
        self.pdetails.name=applicant.name
        self.pdetails.age=applicant.age
        self.pdetails.sex=applicant.sex
        self.pdetails.id=applicant.id
        self.pdetails.seats_required=applicant.seats_required
        self.pdetails.date=int(applicant.date)
        self.pdetails.month=int(applicant.month)
        self.pdetails.year=int(applicant.year)
        
    def data_erase(self):   #function to erase data stored in the passenger
        self.pdetails.name=None
        self.pdetails.age=None
        self.pdetails.sex=None
        self.pdetails.id=None
        self.pdetails.seats_required=None
        self.pdetails.date=None
        self.pdetails.month=None
        self.pdetails.year=None

        
    def display(self):          #function to print the deatils stored in each passenger type object
        print("""\n Your request have been successfully processed!!!
You have been alloted seats in the train
the details about the confirmation are as follows:""")
        print("\n name: ",self.pdetails.name,"\nP_ID: ",self.p_id)
        print("Unique_id:",self.pdetails.id,"\nSeats alloted:",self.pdetails.seats_required)
        print("Date of Journey:",self.pdetails.date,"\\",self.pdetails.month,"\\",self.pdetails.year)

class Train:    #class for train type object

    num=1432725
    
    def __init__(self):     #constructor for Train class
        self.p_head=None
        self.w_head=None
        self.t_name="CHERAN EXPRESS"
        Train.num+=1
        self.t_id=Train.num
        self.source="COIMBATORE"
        self.destination="CHENNAI"
        self.seat_capacity=4
        self.total_p_count=0
        

    def p_head_copy(self,passenger):      #function to link the head of the train to passenger
        self.p_head=passenger

    def w_head_copy(self,waiting_list):
        self.w_head=waiting_list

    def train_data_retrieve(self,T_NO,T_NAME,T_SOURCE,T_DEST,T_SC):
        self.t_id=T_NO
        self.t_name=T_NAME
        self.source=T_SOURCE
        self.destination=T_DEST
        self.seat_capacity=int(T_SC)

    def get_data(self):    #function to get data from the administrator regarding the train object creation
        print("____________________________________________________________________________")
        self.t_name=input("Enter the train name(SHOULD BE IN CAPS) : ")
        Train.num+=1
        self.t_id=Train.num
        self.seat_capacity=int(input("Enter the seat capacity of the train : "))
        self.source=input("Enter the source(SHOULD BE IN CAPS): ")
        self.destination=input("Enter the destination(SHOULD BE IN CAPS): ")

    def display_train_details(self):
        print("____________________________________________________________________________")
        print("TRAIN NAME : ",self.t_name)
        print("TRAIN NO : ",self.t_id)
        print("SEAT CAPACITY : ",self.seat_capacity)
        print("AVAILABLE SEATS : ",self.seat_capacity-self.total_p_count)

    def insert(self,applicant):         #inserting the passenger(node) to the trian(as a linked list with head in train)
        t=self.p_head
        if t is not None:          #insert at a middle or last
            while t is not None:
                if t.pdetails.id is not None:       
                    if t.right is None:         #gives a new ticket to the passenger
                        passenger=Passenger()
                        self.total_p_count+=1
                        passenger.pdetails=Applicant()
                        passenger.data_copy(applicant)
                        t.right=passenger
                        passenger.left=t
                        passenger.display()
                        break
                    elif t.right is not None:
                        t=t.right
               
                elif t.pdetails.id is  None:        #inserts at the middle in a passenger node where data are already erased i.e. the cancelled ticket is given to
                                                    #a applicant who is not in the waiting list
                    t.copy_without_p_id(applicant)
                    self.total_p_count+=1
                    t.display()
                    break
                    
        elif t is None:           #inserts at the beginning(give the new first ticket to a applicant)
            passenger=Passenger()
            self.total_p_count+=1
            passenger.pdetails=Applicant()
            passenger.data_copy(applicant)
            self.p_head_copy(passenger)
            passenger.display()


    def push(self,applicant):
        w=self.w_head
        if w is not None:          #inserts at the last
            while w is not None:
                if w.right is None:
                    waiting_list=Waiting_list()
                    waiting_list.pdetails=Applicant()
                    waiting_list.data_copy(applicant)
                    w.right=waiting_list
                    waiting_list.left=w
                    print("____________________________________________________________________________")
                    print("\tYOU HAVE BEEN SUCCESSFULLY INCLUDED IN THE WAITING LIST")
                    break
                elif w.right is not None:
                    w=w.right
                    
        elif w is None: #inserts at the beginning
            waiting_list=Waiting_list()
            waiting_list.pdetails=Applicant()
            waiting_list.data_copy(applicant)
            self.w_head_copy(waiting_list)
            print("____________________________________________________________________________")
            print("\tYOU HAVE BEEN SUCCESSFULLY INCLUDED IN THE WAITING LIST")
    

    def pop(self):          #function to pop from waiting_list(getting the first node from the waiting_list queue)
        w=self.w_head
        if w is not None:
                if w.right is not None:     
                    next_node=w.right
                    next_node.left=self.w_head
                    self.w_head=next_node
                elif w.right is None:
                    self.w_head=None
                return w.pdetails
        elif w is None:
            print("____________________________________________________________________________")
            print("\n \t\tWAITING LIST IS EMPTY")
            return None


    def remove_and_update(self):        #function to cancel and update the ticket which has been already been reserved     
            print("____________________________________________________________________________")
            print("\n\n WELCOME TO CANCELLATION PORTAL")
            r_pid=int(input("\nEnter your Passenger id(P_ID):"))
            t=self.p_head
            while t is not None:
                if t.p_id==r_pid:
                    if t.pdetails.id is not None:
                        t.data_erase()
                        self.total_p_count-=1
                        print("____________________________________________________________________________")
                        print("\n \t\tYou have CANCELLED your ticket!!!")
                    elif t.pdetails.id is None:
                        print("____________________________________________________________________________")
                        print("THIS TICKET ",t.p_id," HAS ALREADY BEEN CANCELLED")
                    first_waiter=self.pop()
                    if first_waiter is not None:
                        t.copy_without_p_id(first_waiter)
                        self.total_p_count+=1
                        t.display()
                    break
                    if first_waiter is None:
                        break
                else:
                    t=t.right
            if t is None:
                print("____________________________________________________________________________")
                print("Sorry the PID which you have entered is not found!!! \n ERROR!!! TICKET DOESN'T EXIST!!!")
        
                   
    def p_display(self):      #function to display  the details of the passenger (printing a linked list)
        print("____________________________________________________________________________")
        print("\n \t\t PASSENGER DETAILS")
        t=self.p_head
        while t :
            if t.pdetails.id is not None:
                print("\nname: ",t.pdetails.name,"\nP_ID: ",t.p_id)
                print("Unique_id:",t.pdetails.id,"\nSeats alloted:",t.pdetails.seats_required)
                print("Date of Journey:",t.pdetails.date,"\\",t.pdetails.month,"\\",t.pdetails.year)                
            t=t.right

        if self.p_head is None:
             print("____________________________________________________________________________")
             print("PASSENGERS LIST IS EMPTY")


    def w_display(self):      #displays the content in the linked list called "Waiting_list"
        print("____________________________________________________________________________")
        print("\n \t\tWAITING LIST DETAILS")
        w=self.w_head
        while w:
            print("\nname: ",w.pdetails.name)
            print("Unique_id:",w.pdetails.id,"\nSeats Requested:",w.pdetails.seats_required)
            print("Date of Journey:",w.pdetails.date,"\\",w.pdetails.month,"\\",w.pdetails.year)
            w=w.right
        if self.w_head is None:
            print("____________________________________________________________________________")
            print("\n \t\tWAITING LIST IS EMPTY")

class Waiting_list ():
    
    def __init__(self):         #constructor for Waiting_list class
        self.pdetails=None
        self.right=None
        self.left=None  

    def data_copy(self,applicant):          #function to copy data from applicant type object to pdetail attribute in Waiting_list type object 
        self.pdetails.name=applicant.name
        self.pdetails.age=applicant.age
        self.pdetails.sex=applicant.sex
        self.pdetails.id=applicant.id
        self.pdetails.seats_required=applicant.seats_required
        self.pdetails.date=int(applicant.date)
        self.pdetails.month=int(applicant.month)
        self.pdetails.year=int(applicant.year)

def write_file(train):
    data=[train.t_id,train.t_name,train.source,train.destination,train.seat_capacity]
    with open("train details.csv",'a') as f:
        csvobj=csv.writer(f)
        csvobj.writerow(data)

def retrieve_from_file(train):
    with open("train details.csv",'r') as f:
        csvobj=csv.reader(f)
        for row in csvobj:
            if(len(row)!=0):                
                temp=Train()
                temp.train_data_retrieve(row[0],row[1],row[2],row[3],row[4])
                train.append(temp)

def search_train(train):
    print("____________________________________________________________________________")
    flag=False
    k=1
    s=input("Enter the source(SHOULD BE IN CAPS)")
    d=input("Enter the destination(SHOULD BE IN CAPS)")
    print("\n\nTRAIN NAMES")
    print("____________________________________________________________________________")
    for m in range(0,len(train)):
        if(s==train[m].source):
            if(d==train[m].destination):
                flag=True
                print(k,train[m].t_name)
                k+=1
    if flag==False:
        print("SORRY NO TRAINS MATCH WITH YOUR DESIRED SOURCE AND DESTINATION!!!")
    return flag


def train_or_location_matching():
    opt=int(input(""" Select an option:
        1.To check the hypothesis based on SOURCE AND DESTINATION
        2.To check the hypothesis for A PARTICULAR TRAIN"""))
    ann_mean=dataset_matching_for_hypothesis(opt)
    if ann_mean:
            hypothesis_testing(ann_mean)
        
    
def dataset_matching_for_hypothesis(opt):
    obj=xlrd.open_workbook("train dataset.xlsx")
    sheet=obj.sheet_by_index(0)
    ann_mean=[]
    flag=False
    if opt==1:
        opt_sr=input("ENTER THE REQUIRED SOURCE : ")
        opt_dn=input("ENTER THE REQUIRED DESTINATION : " )
        for i in range(sheet.nrows):
            if sheet.cell_value(i,1)==opt_sr:
                if sheet.cell_value(i,2)==opt_dn:
                    ann_mean.append(sheet.cell_value(i,16))
                    flag=True
        if flag:
            return ann_mean
    
        else:
            print("ENTERED SOURCE AND DESTINAATION DOESN'T EXIST")
            return False
    
    elif opt==2:
        opt_t=input("ENTER THE REQUIRED TRAIN NAME(SHOULD BE IN CAPS): ")        
        for i in range(sheet.nrows):
            if sheet.cell_value(i,0)==opt_t:
                ann_mean.append(sheet.cell_value(i,16))
                flag=True        
        if flag:
            return ann_mean        
        else:
            print("ENTERED TRAIN DOESN'T EXIST")
            return False        
        
    
def hypothesis_testing(ann_mean):
    mean1=mean(ann_mean)
    sd1=stdev(ann_mean)
    print("THE NULL HYPOSIS(H0): MEAN1= " ,round(mean1,4))
    mean2=float(input("THE ALTERNATIVE HYPOTHESIS(H1):MEAN2= "))
    z_cal=(mean1-mean2)/(sd1/(len(ann_mean)))
    print("Z calculated value is: zcal= ",round(z_cal,4))
    print("Z tabulated value(single tail) is: ztab=",1.645)
    if z_cal<1.645:
        print(" THE NULL HYPOTHESIS(H0) IS ACCEPTED \n i.e. the demand for train requirement by the passengers has been supplied by the railway" )
    else:
        print(" THE NULL HYPOTHESIS(H0) IS REJECTED \n i.e. the demand for train requirement by the passengers has not been supplied by the railway" )


def performance_graph():
    opt=int(input("""SELECT YOUR CHOICE
                  1.plot graph for the usage of a particular train by the passengers over the years
                  2.plot graph for the transportaion by the passengers between a source and destination
                  """))
    plot_graph(opt)


def plot_graph(opt):
    obj=xlrd.open_workbook("train dataset.xlsx")
    sheet=obj.sheet_by_index(0)
    ann_mean=[]
    years=[]
    flag=False
    if opt==1:
            opt_t=input("ENTER THE REQUIRED TRAIN NAME: ")
            for i in range(sheet.nrows):
                if sheet.cell_value(i,0)==opt_t:
                    ann_mean.append(sheet.cell_value(i,16))
                    years.append(sheet.cell_value(i,3))
                    flag=True

            if flag:
                lplt.plot(years,ann_mean,label=opt_t)
                lplt.xlabel("YEAR")
                lplt.ylabel("NUMBER OF PASSENGERS")
                lplt.title("USAGE OF TRAIN")
                lplt.bar(years,ann_mean,width=0.4)
                
            else:
                print("NO TRAIN MATCHED WITH THE NAME YOU ENTERED")
            
    if opt==2:
        opt_sr=input("ENTER THE REQUIRED SOURCE : ")
        opt_dn=input("ENTER THE REQUIRED DESTINATION : " )
        opt=int(input("""SELECT AN OPTION
                      1.PLOT USAGE GRAPH BETWEEN ALL THE TRAINS BETWEEN THESE LOCATIONS
                      2.PLOT A SIMPLE GRAPH FOR THE TRANSPORTATION BETWEEN THESE LOCATIONS
                      3.PIE CHART OF COTRIBUTION OF TRAINS ON THESE LOCATIONS"""))
        
        if opt==1 or opt==3:
            names=[]
            all_ann_mean=[]
            for i in range(sheet.nrows):
                if sheet.cell_value(i,1)==opt_sr:
                    if sheet.cell_value(i,2)==opt_dn:
                        if sheet.cell_value(i,0) not in names:                         
                            ann_mean=[]
                            years=[]
                            opt_t=sheet.cell_value(i,0)
                            names.append(opt_t)
                            for j in range(sheet.nrows):
                                if opt_t==(sheet.cell_value(j,0)):
                                    ann_mean.append(sheet.cell_value(j,16))
                                    years.append(sheet.cell_value(j,3))
                                    flag=True
                            all_ann_mean.append(sum(ann_mean))                                    
                            if flag:
                                if opt==1:
                                    lplt.plot(years,ann_mean,label=opt_t)                                
                                    lplt.xlabel("YEAR")
                                    lplt.ylabel("NUMBER OF PASSENGERS")
                                    lplt.title("USAGE GRAPH BETWEEN ALL THE TRAINS BETWEEN TWO LOCATIONS")
            if opt==3:
                if flag:
                    for i in range(len(all_ann_mean)):
                        all_ann_mean[i]/=1000                       
                    lplt.pie(all_ann_mean,labels=names,shadow=True,radius=1.0,autopct='%4.4f%%')
                    lplt.title("CONTRIBUTIONS OF TRAINS OVER THESE TWO LOCATIONS")
                    lplt.show()

                                    
        elif opt==2:
            for i in range(sheet.nrows):
                if sheet.cell_value(i,1)==opt_sr:
                    if sheet.cell_value(i,2)==opt_dn:
                        ann_mean.append(sheet.cell_value(i,16))
                        years.append(sheet.cell_value(i,3))
                        flag=True
                  
            if flag:
                    lplt.plot(years,ann_mean,label=[opt_sr,opt_dn])
                    lplt.ylabel("NUMBER OF PASSENGERS")
                    lplt.xlabel("YEARS")
                    lplt.title("TRANSPORTATION BETWEEN TWO SOURCE AND DESTINATION")
            
        if flag==False:
            print("THE ENTERED SOURCE AND DESTINATION DOESN'T MATCH")
    if flag:                
        if opt!=3:    
            lplt.legend()
            lplt.show()


#DRIVER CODE            
train=[]
a=1
b=0
while a>b:
    if len(train)==0:
        retrieve_from_file(train)
    print("\t\tWELCOME TO INDIAN RAILWAY")
    print("____________________________________________________________________________")#getting the user mode  
    user_mode=int(input("""\n\nplease enter the mode of User
    1.Adminstrator
    2.User"""))
    if (user_mode==1):      #adminstrator mode
        a1=1
        b1=0
        while a1>b1:
            print("____________________________________________________________________________")
            choice=int(input("""\n CHOOSE AN OPTION
1.ENTER DETAILS FOR NEW TRAINS
2.MODIFY DETAILS FOR ALREADY EXISTING TRAIN
3.DISPLAY THE TRAIN AND IT'S PASSENGER AND WAITING LIST'S DETAILS ABOUT A PARTICULAR TRAIN
4.PERFORM HYPOTHESIS TESTING
5.PLOT GRAPHS ON USAGE OF TRAINS"""))

            if choice==1:           #to create new trains
                a2=1
                b2=0
                while a2>b2:
                    print("\n____________________________________________________________________________")
                    n=int(input("enter the no.of trains for which the details had to be newly feeded : "))
                    for m in range (n):
                        temp=Train()
                        temp.get_data()
                        train.append(temp)
                        write_file(temp)
                        temp.display_train_details()
                    print("____________________________________________________________________________")
                    choice=int(input("""Do you want to continue this portal or not
1.yes
2.no"""))
                    if choice==1:
                        a2+=1                         
                    b2+=1

            elif choice==2:     #modifying the data for already existing trains
                print("____________________________________________________________________________")
                for m in range(0,len(train)):
                    print(m+1,". ",train[m].t_name)
                print("____________________________________________________________________________")
                name=input("Enter the train name(SHOULD BE IN CAPS) : ")
                flag=True
                for m in range(len(train)):
                    if (train[m].t_name==name):
                        flag=True
                        if train[m].total_p_count!=0:
                            print("\n____________________________________________________________________________")
                            print("DETAILS CANNOT BE CHANGED AS THE PASSENGERS ARE ALREADY CONFIRMED")
                        if train[m].total_p_count==0:
                            new_sc=int(input("ENTER THE NEW SEAT CAPACITY(MUST BE GREATER THAN THE OLDER  ONE"))
                            if new_sc>train[m].seat_capacity:
                                train[m].seat_capacity=int(new_sc)
                            else:
                                print("ERROR!!!NEW SEAT CAPACITY MUST BE LARGER THAN THE OLDER ONE!!!")
                            train[m].display_train_details()
                if(flag==False):
                    print("INVALID TRAIN NAME ")
            
                        
            elif choice==3:         #to view the passenger and waiting list details of a particular train
                print("____________________________________________________________________________")
                for m in range(0,len(train)):
                    print(m+1,". ",train[m].t_name)
                print("____________________________________________________________________________")

                name=input("enter the train name")
                flag=False
                for m in range (len(train)):
                    if (train[m].t_name==name):
                        flag=True
                        train[m].display_train_details()
                        train[m].p_display()
                        train[m].w_display()
                        
                if flag==False:
                    print("INVALID TRAIN NAME")
                print("____________________________________________________________________________")
                
            elif choice==4:     #to perform hypothesis testing
                print("____________________________________________________________________________")
                train_or_location_matching()
            
            elif choice==5:
                print("____________________________________________________________________________")
                performance_graph()
            
            choice=int(input("""Do you want to  RETURN TO ADMINSTRATOR MODE'S MAIN MENU
1.YES
2.NO"""))
            if choice==1:
                a1+=1
            b1+=1
    
        
    elif (user_mode==2):        #user mode
        if len(train)!=0:
            x=1
            y=0
            while x>y:
                flag=search_train(train)
                print("____________________________________________________________________________")
                if(flag):
                    opt_train=input("Enter the train name : ")
                    for i in range (len(train)):
                        if train[i].t_name==opt_train:
                            train[i].display_train_details()
                            a3=1
                            b3=0
                            while a3>b3:
                                print("\n____________________________________________________________________________")
                                choice=int(input("""\n\n\t\t WELCOME TO INDIAN RAILWAY
                                Choose the option
                                1.applying for RESERVATION of tickets
                                2.CANCELLATION of tickets
                                3.EXIT"""))
                                if (choice==1):
                                    print("____________________________________________________________________________")
                                    print("\n\t\tWELCOME TO RESERVATION SYSTEM")
                                    date=int(input("Enter the date of journey: "))
                                    month=int(input("Enter the month of journey: "))
                                    year=int(input("Enter the year of journey: "))
                                    seats_req=int(input("\nEnter the Total No.of Seats Required:"))
                                    j=0
                                    while (j<seats_req):                
                                        applicant=Applicant()
                                        applicant.get_data(date,month,year)
                                        if (train[i].total_p_count<train[i].seat_capacity):     #if seats are available ticket is issued
                                            train[i].insert(applicant)
                                        elif(train[i].total_p_count>=train[i].seat_capacity):   #if seats aren't available applicant is pushed to waiting_list
                                            print("____________________________________________________________________________")
                                            print("\nSorry there are no seats avialble right now!!Please do check back later!!!Wait for further updates!!!")
                                            train[i].push(applicant)
                                        j+=1

                                elif (choice==2):       #cancellation of tickets
                                        train[i].remove_and_update()

                                elif choice==3:
                                    b3+=1
                                    print("____________________________________________________________________________")
                                    print("\n\n\t\t THANK YOU!!!! WELCOME AGAIN!!!")
                                    break    
                                print("____________________________________________________________________________")
                                choice=int(input("""\n\nDo you want to RETURN TO MAIN MENU OF THE SAME TRAIN
                        1.yes
                        2.No exit the portal \n"""))
                                if(choice==1):
                                       a3+=1
                                           
                                elif(choice==2):
                                    print("____________________________________________________________________________")
                                    print("\n\n\t\t THANK YOU!!!! WELCOME AGAIN!!!")
                                    b3+=1
                                    break
                                b3+=1
                choice=int(input("""do you want to RETURN TO USER MODE'S MAIN MENU
    1.yes
    2.no"""))
                if (choice==1):
                    x+=1
                y+=1
    choice=int(input("""DO you want to return to the USER MODE SELECTION MENU PORTAL
    1.YES
    2.NO"""))
    if choice==1:
        a+=1
    else:
        print("____________________________________________________________________________")
        print("\n\n\t\t THANK YOU!!!! WELCOME AGAIN!!!")
        b+=1
        break
    b+=1
print("____________________________________________________________________________")
ex=input("press any key to exit the portal")
