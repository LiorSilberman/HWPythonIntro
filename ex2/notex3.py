# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

user_string = str(input("enter a string: "))

for i in range(10):
    print(user_string[::-1])


string = input("Enter a string: ")
for i in string:
    if i.isalpha():
        print(i, end="")
    else:
        print(" ")


str = input("Enter a string: ")
str = str.lower()   
new_str = ""
for i in str:
    if i.isalpha:
        new_str += i

   
num = int(input("enter a number: "))

for i in range(num):
    for j in range(num):
        if i == j:
            print("1",end=(""))
        else:
            print("0",end=(""))
    print()
   """
string = input("Enter a string: ")


while string == "":
    print("There are {} @ in the string!".format(string.count("@")))
    if str == "quit":
        print("bye bye")
    