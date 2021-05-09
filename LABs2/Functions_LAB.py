from random import randint
from time import sleep
def menu():
    while(True):
        choice=input("Menu:\n---------------\n1.dog details\n2.friends list\n3.N azzeret\n")
        if (choice=="1"):
            Dogs()
        elif(choice=="2"):
            Friends()
        elif(choice=="3"):
            Azzeret()
        else:
          print("Enter 1-3 only!\n")
          continue
        exit=input("Do you want to exit? yes/no\n")
        if(exit=="yes"):
            break
        else:
            print("Welcome back\n")
    print("Bye Bye...\n")
def Dogs():
    name=input("Enter Dog's name: ")
    age=int(input("Enter Dog's age: "))
    print("\nDog's name: " + name + "\nDog's age:" + str(age*7) +"\n")
def Friends():
    list_Friends=[]
    for i in range(5):
        list_Friends.append(input("Enter Friend's name: "))
    name=input(" new Friend's name: ")
    if(name in list_Friends):
        print(name + " is inside the list!\n")
    else:
        print(name + " isn't inside the list\n")
def Azzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print(str(num) + " Azzeret is: " + str(sum) + "\n")
menu()

