#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‫‪Assignmen‫‪t no. 3
Program: logo.py‬‬
"""

from turtle import *

def snake():
    c = 0
    while c <= 1:
        if c == 1:
            penup()
            goto(-35,208)
            pendown()
            setheading(180)
            pensize(3)
            pencolor("#306998")
            fillcolor("#4B8BBE")
            begin_fill()
         
        else:
            pensize(3)
            pencolor("#FFD43B")
            fillcolor("#FFE873")
            begin_fill()
            
        backward(20)   
        left(90)   
        forward(10)
        right(90)
        forward(160)
        left(45)
        circle(140,90)  
        left(45)
        forward(40)
        left(90)
        forward(80)
        
        for i in range(10):
            right(9)
            forward(5)

        forward(160)

        for n in range(10):
            left(9)
            forward(5)

        forward(141)
        left(45)
        circle(152,90)
        left(45)
        forward(77)
        left(90)
        forward(95)
        end_fill()
        penup()
        backward(40)
        left(90)
        forward(60)
        
        pensize(3)
        fillcolor("white")
        pendown()
        begin_fill()
        circle(15)
        end_fill()
        c += 1
snake()