#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‫‪Assignmen‫‪t no. 2
Program: histogram.py‬‬
"""

counters = [0]*26
input_text = input("Enter a text: ")
input_text = input_text.lower()

# count number of apearences of each letter.
try:
    for l in input_text:
        if l.isalpha():
            counters[ord(l)-ord("a")] += 1
except IndexError:
    print("error")

# the bigest number.
max_letter_apearence = max(counters)

histogram = ""
for i in range(max_letter_apearence, 0 , -1):
    for j in counters:
        if j >= i:
           histogram += " x"
        else:
           histogram += "  "        
    histogram += "\n"

# print histogram
print(histogram)
print(" a b c d e f g h i j k l m n o p q r s t u v w x y z")        