'''
filename = "C:/Users/moshe/PycharmProjects/hello.txt"
file =open(filename,"r")
my_string=file.read()
file.close()
print(my_string)
my_list=my_string.split(",")
print(type(my_list))
print(my_list)
'''

'''
filename = "C:/Users/moshe/PycharmProjects/hello.txt"
file =open(filename,"r")
new_list=[]
new_list=file.read().splitlines()
print(type(new_list))
print(new_list)
file.close()
for i in new_list:
    print(i)
'''

filename = "C:/Users/moshe/PycharmProjects/hello.txt"
file = open(filename, "r")
print(file.read())
file.close()
