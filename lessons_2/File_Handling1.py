

filename = "C:/Users/moshe/PycharmProjects/hello.txt"
'''
file = open(filename,"r+")
print(file.read())
file.write("192.168.1.1\n192.168.1.2")
file.close()
'''
file = open(filename, "a")
file.write("192.168.1.3" "\n192.168.1.4")
file.close()
file = open(filename, "r")
print(file.read())
file.close()
