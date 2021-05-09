from time import  sleep
def menu():
    while(True):
        choice1 = input("Menu:\n--------------\na.IP System \nb.DNS System\n")
        if(choice1=="a"):
            choice2=input("Menu IP System:\n--------------\n1.search for ip address list\n2.add ip address to a list\n3.delete address to a list\n4.print all the IPs to the screen\n")
            if(choice2=="1"):
                search_ip()
            elif(choice2=="2"):
                add_ip()
            elif (choice2=="3"):
                delete_ip()
            elif(choice2=="4"):
                print_IPs()
        elif(choice1=="b"):
            choice3=input("Menu DNS System:\n--------------\n1.search for URL from dictionary\n2.add URL + IP address to a dictionary\n3.delete URL from dictionary\n4.update IP address\n5.print all IPs to the screen\n")
            if (choice3=="1"):
                search_URL()
            elif (choice3=="2"):
                add_URL()
            elif (choice3=="3"):
                delete_URL()
            elif (choice3=="4"):
                update_IP()
            elif (choice3=="5"):
                print_dict()
        else:
            print("Enter a or b only!")
            continue
        exit=input("Do you want exit? y/n\n")
        if(exit=="y"):
            print("Bye Bye...")
            break

def search_ip():
    print("1")
def  add_ip():
    print("2")
def  delete_ip():
    print("3")
def print_IPs():
    print("4")

def search_URL():
    print("1")

def add_URL():
    print("2")

def delete_URL():
    print("3")

def update_IP():
    print("4")

def print_dict():
    print("5")

