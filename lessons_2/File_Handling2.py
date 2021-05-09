'''
filename="C:/Users/moshe/PycharmProjects/IPs.txt"
    file=open(filename, "r")
    for line in file:
        print(line)
        file.close()
'''

filename = "C:/Users/moshe/PycharmProjects/hello.txt"
file =open(filename,"r")
my_string=file.read()
file.close()
print(my_string)
my_list=my_string.split(",")
print(type(my_list))
print(my_list)
