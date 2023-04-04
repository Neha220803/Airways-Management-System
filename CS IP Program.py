import pickle
#To create Airlines Management system
def CREATE() :
    L = []
    while True :
        fcode = int(input("Enter the Flight Code : "))
        airline = input(("Enter the Name of the Airline : "))
        source = input("Enter the Starting place : ")
        desti = input("Enter the Destination : ")
        dist = int(input("Enter the Distance in kms: "))
        fare = float(input("Enter the Fare Amout per head : "))
        L.append([fcode,airline,source,desti,dist,fare])
        cnt = input("Do you want to Continue? Enter Y/N : ")
        if cnt not in "Yy":
                 break
    f = open("Airbus.dat","wb")
    pickle.dump(L,f)
    f.close()

#To Display all the contents in the File        
def DISPLAY():
    f = open("Airbus.dat","rb")
    L = pickle.load(f)
    print("Flight Details : ")
    print("FlightNo.  Airline \tStart \tDestination \t Distance\
\t FareAmount")
    for i in L :
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4],"\t",i[5])
    f.close()

#To Append Contents to the file
def APPEND():
    f = open("Airbus.dat","rb")
    a = pickle.load(f)
    f.close()
    while True :
        fcode = int(input("Enter the Flight Code : "))
        airline = input(("Enter the Name of the Airline : "))
        source = input("Enter the Starting place : ")
        desti = input("Enter the Destination : ")
        dist = int(input("Enter the Distance : "))
        fare = float(input("Enter the Fare Amout per head : "))
        a.append([fcode,airline,source,desti,dist,fare])
        cnt = input("Do you want to Continue? Enter Y/N : ")
        if cnt not in "Yy":
                 print("New Datas are successfully Appended!!!")
                 break
    f = open("Airbus.dat","wb")
    pickle.dump(a,f)
    f.close()

#To Search a Airline according to the given flight code
def SEARCH() :
    f = open("Airbus.dat","rb")
    sr = int(input("Enter the flight code to be searched : "))
    a = []
    a = pickle.load(f)
    count = 0
    for r in a:
        if r[0] == sr:
            count = 1
            print("\nFlightNo.  Airline \tStart \tDestination \t Distance\
\t FareAmount")
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t\t",r[4],"\t",r[5])
            break
    if count == 0:
            print("!!!Required Flight is not found!!!")
    f.close()

#To Copy Some Particular Flight Details to Another File
def COPY():
     c = input("Enter a Flight name to copy to a new file : ")
     f = open("Airbus.dat","rb")
     g = open(c,"wb")
     a = pickle.load(f)
     b = []
     for r in a :
         if r[1].upper() == c.upper() :
             b.append(r)
     pickle.dump(b,g)
     f.close()
     g.close()
     g = open(c,"rb")
     x = pickle.load(g)
     print("Flight Details of the Copied File : ")
     print("FlightNo.  Airline \tStart \tDestination \t Distance\
\t FareAmount")
     for i in x :
         print(i[0],"\t",i[1],"\t",i[2],"\t",i[3]," \t\t",i[4],"\t",i[5])
     g.close()

#To insert a Record at a particular position
def INSERT():
    f = open("Airbus.dat","rb")
    a = []
    a = pickle.load(f)
    f.close()
    posi = int(input("Enter the position to insert : "))
    if posi > len(a) :
        print("Position not found!")
    else:
        fcode = int(input("Enter the Flight Code : "))
        airline = input(("Enter the Name of the Airline : "))
        source = input("Enter the Starting place : ")
        desti = input("Enter the Destination : ")
        dist = int(input("Enter the Distance : "))
        fare = float(input("Enter the Fare Amout per head : "))
        r = [fcode,airline,source,desti,dist,fare]
        a.insert(posi-1,r)
        f = open("Airbus.dat","wb")
        pickle.dump(a,f)
        f.close()
        print("The insertion is Done!!!")

#To Delete a Particular Record
def DELETE():
    f = open("Airbus.dat","rb")
    a = pickle.load(f)
    f.close()
    dt = int(input("Enter the Flight Code that is to be deleted : "))
    b = []
    count = 0
    for r in a :
        if r[0] == dt :
            count = 1
        else :
            b.append(r)
    if count == 0 :
            print("Required Flight not found!!") 
    else :
            f = open("Airbus.dat","wb")
            a = pickle.dump(b,f)
            f.close()
            print("Deletd Successfully!") 

#Sorting the records 
def SORT():
    f = open("Airbus.dat","rb")
    a = pickle.load(f)
    f.close()
    n = len(a)
    for i in range(n-1):
        for j in range (n-i-1):
            if a[j][1] > a[j+1][1]:
                a[j],a[j+1] = a[j+1],a[j]
    print("Sorted Records : ")
    print("FlightNo.  Airline \tStart \tDestination \t Distance\
\t FareAmount")
    for r in a :
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t\t",r[4],"\t",r[5])

#Main Program :
print("\t\t Airlines Management System")
while True:
    print("\n1.To Create Airlines Management system and\
 Inputting Some Details")
    print("2.To Display all the Flight Details")
    print("3.To Add a New Flight Detail(s)")
    print("4.To Search for a Particular Flight's Detail")
    print("5.To Copy a Particular Flight's Details to Another File")
    print("6.To Insert a New Flight's Detail at a particular position")
    print("7.To Delete a Particular Flight Detail")
    print("8.To Sort the Details by Airline")
    print("9.Exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1 :
        CREATE()
    elif ch == 2 :
        DISPLAY()
    elif ch == 3 :
        APPEND()
    elif ch == 4 :
        SEARCH()
    elif ch == 5 :
        COPY()
    elif ch == 6 :
        INSERT()
    elif ch == 7 :
        DELETE()
    elif ch == 8 :
        SORT()
    elif ch == 9 :
        print("Exiting......\nSuccessfully Exited!")
        break  
    else :
        print("WRONG CHOICE! TRY AGAIN!!!")

