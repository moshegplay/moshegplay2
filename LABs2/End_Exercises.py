'''
 "Twinkle, twinkle, little star, How I wonder what you are! Up
above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star,
How I wonder what you are"
'''


 ###print('''Twinkle, twinkle, little star,
###  How I wonder what you are!
###      Up above the world so high,
###  Like a diamond in the sky.
###Twinkle, twinkle, little star,
###    How I wonder what you are''')

'''
color_list = ["Red","Green","White","Black"]
print("the first cell: " + color_list[0] + "\nthe last cell: " + color_list[-1])
'''

'''
n=int(input("Enter a number: "))
print(n +(n*10+n) + (n*100+n*10+n))
'''

'''
from datetime import date
f_date = date(2014, 7, 2)
print(f_date)
l_date = date(2014, 7, 11)
print(l_date)
delta = l_date - f_date
print(delta.days)
'''

'''
def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
'''

'''
num=7
sum= 1**3 + 2**3 + 3**3 + 4**3 + 5**3 + 6**3
def positive(num):
    sum=0
    for i in range(1,num):
        sum=sum+(i**3)
    print("The Summary is: " + str(sum))
    return sum
new_sum=positive(int(input("Enter a positive number: ")))
'''

'''
def sum_of_cubes(n):
    n=n-1
    total=0
    while n>0:
        total = total+(n*n*n)
        n=n-1
    return total
print("Sum of cubes: " + str(sum_of_cubes(7)))
'''
