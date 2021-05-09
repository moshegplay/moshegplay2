from time import  sleep
def menu():
    true="true"
    while(true=="true"):
        choise=input("Menu:\n-------------\na.IP System?\nb.DNS System?\n")
        if(choise=="a" or choise=="A"):
            IP()
        elif(choise=="b" or choise=="B"):
            DNS()
        else:
            print("Enter a or b only!!!\n")
            continue
        true="done"


def IP():
    true="true"
    while(true=="true"):
        choise=(input("\nIP Menu\n========\n1.search for IP address from a list\n2.add IP address to a list\n3.Delete IP address to a list\n4.Print all the IPs to the screen\n"))
        if(choise=="1"):
            ip_search()
        elif(choise=="2"):
            ip_add()
        elif(choise=="3"):
            ip_del()
        elif(choise=="4"):
            ip_print()
        else:
            print("Enter 1-4 only!\n")
            continue
        true=input("\ndo you want back to menu? enter m\ndo you want to exit? enter e\n")
        if (true == "m"):
            menu()
        elif (true == "e"):
            print("Bye Bye...")
        else:
            print("press m or e only!\n")


def DNS():
    true = "true"
    while (true == "true"):
        choise=(input("\nDNS Menu\n========\n1.search for URL from a dictionary\n2.add URL + IP address to a dictionary\n3.Delete a URL from a dictionary\n4.Update the IP address of specific URL\n5.Print all the URL:IP to the screen\n"))
        dict1={"www.google.com":"8.8.8.8" , "www.facebook.com":"9.9.9.9" , "www.youtube.com" : "7.7.7.7"}
        if(choise=="1"):
            URL_search(dict1)
        elif(choise=="2"):
            add_url_ip(dict1)
        elif(choise=="3"):
            del_url(dict1)
        elif(choise=="4"):
            print_url_ip(dict1)
        elif(choise=="5"):
            print_all(dict1)
        else:
            print("Enter 1-5 only!")
            continue
        true = input("\ndo you want back to menu? enter m\ndo you want to exit? enter e\n")
        if (true == "m"):
            menu()
        elif (true == "e"):
            print("Bye Bye...")
        else:
            print("press m or e only!")
            continue

def ip_search():
    new_ip=input("\nEnter IP: ")
    file=open("C:/Users/moshe/PycharmProjects/IPs.txt", "r+")
    f=str(file.read())
    lists=f.splitlines()
    if(new_ip in (lists)):
        print("\n" + new_ip + " is in the list")
    else:
        print("\n" + new_ip + " is not in the list")
    file.close()


def ip_print():
    file=open("C:/Users/moshe/PycharmProjects/IPs.txt" , "r")
    print(file.read())
    file.close()

def ip_add():
    ip_new=input("\nEnter new ip: ")
    file = open("C:/Users/moshe/PycharmProjects/IPs.txt", "a+")
    file.write("\n" + ip_new)
    file.close()
    file = open("C:/Users/moshe/PycharmProjects/IPs.txt", "r")
    print("your new ip list:\n")
    print(file.read())
    file.close()

def ip_del():
    filename=("C:/Users/moshe/PycharmProjects/IPs.txt")
    file = open(filename, "r+")
    print("your ip list:\n" + file.read())
    file.close()
    filename = ("C:/Users/moshe/PycharmProjects/IPs.txt")
    file = open(filename, "r+")
    lists=(file.read().splitlines())
    del_ip=int(input("Enter the line number of the want to delete: "))
    del_ip=del_ip-1
    lists.pop(del_ip)
    new_list="\n".join(lists)
    print(new_list)
    file.close()
    filename = ("C:/Users/moshe/PycharmProjects/IPs.txt")
    file = open(filename, "w")
    file.write(new_list)
    print("the ip was deleted")
    file.close()
    filename = ("C:/Users/moshe/PycharmProjects/IPs.txt")
    file = open(filename, "r+")
    print("\nyour new ip list:\n" + file.read())
    file.close()

def URL_search(dict1):

    url=input("Enter the URL you want to find: ")
    if url in (dict1):
        print(url +" is already here")
    else:
        print("the URL " + url + " is not in the dictionary")

def add_url_ip(dict1):
    dict1.update({input("Enter New URL: "):input("Enter new IP: ")})
    print(dict1)

def del_url(dict1):
    print(dict1)
    url=input("Enter the URL you want to delete: ")
    del dict1 [url]
    print("your updated dictionary:\n" + str(dict1))

def print_url_ip(dict1):
    print(dict1)
    url=input("Enter the URL you want to update: ")
    ip=input("Enter the ip: ")
    dict1.update({url:ip})
    print("your updated dictionary:\n" + str(dict1))

def print_all(dict1):
    print("your dictionary:\n" + str(dict1))
