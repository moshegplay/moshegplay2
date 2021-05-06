'''
f =open("C:/Users/moshe/PycharmProjects/hello2.txt", "x")
f.close()
'''

filename = "C:/Users/moshe/PycharmProjects/hello2.txt"
file = open(filename, "r")
print(file.readlines()[0])
file.close()
