#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‫‪Assignment‬‬ ‫‪no. 1
Program: triangle.py‬‬
"""

import math

def draw_triangle(user_input, triangle_height):
    triangle = ""
    # take string slice
    prev_place = 0
    for row_index in range(triangle_height):
        # handle first row
        if row_index == 0:
            triangle += "{}*\n".format((triangle_height+1)*" ")

        next_place = (row_index+1)**2
        row_str = user_input[prev_place : next_place]
        prev_place = next_place
    
        # fill missing spaces on last row
        if row_index == triangle_height-1 and len(row_str) < 2*triangle_height-1:
            row_str += " "*(2*triangle_height-1-len(row_str))
        
        # fill triangle
        triangle += "{}*{}*\n".format(((triangle_height-row_index)*" "), row_str)
    
        # handle last row
        if row_index == triangle_height-1:
            triangle += "{}".format((2*triangle_height+3)*"*")
    
    # finish
    return triangle

if __name__ == "__main__":
    # get user input and count it
    user_input = input("Enter a srting: ")
    count_letters = len(user_input)

    # find height of triangle
    height = math.ceil((math.sqrt(count_letters)))
    
    print(draw_triangle(user_input, height))