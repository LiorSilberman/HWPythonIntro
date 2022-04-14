#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‪Assignmen‫‪t no. 2
Program: stats.py‬‬
"""

def is_float(str_float):
    '''
    check if string is legal float number
    '''
    legal_float_chars = "+-.0123456789"

    # check all chars in str_float are legal
    for char in str_float:
        if char not in legal_float_chars:
            return False
    
    # +- only on start of string
    sign_found = False
    if "+" in str_float:
        sign_found = True
        
        # + is at beginning of string?
        if str_float[0] != "+":
            return False

    if "-" in str_float:
        sign_found = True
        
        # - is at beginning of string?
        if str_float[0] != "-":
            return False
        
    if sign_found:
        # length of string is longer then one?
        if len(str_float) < 2:
            return False

        # next char after sign is digit?
        if not str_float[1].isdigit():
            return False
        
        # "0" in beginning? next char is "."
        if str_float[1] == "0" and len(str_float) > 2:
            if str_float[2] != ".":
                return False
    
    # last char is digit?
    if not str_float[-1].isdigit():
        return False
        
    # more then one dot?
    if str_float.count('.') > 1:
        return False
    
    # "0" in beginning? next char is "." 
    if str_float[0] == "0" and len(str_float) > 1:
        if str_float[1] != ".":
            return False
        
    # dot in first char?
    if str_float[0] == ".":
        return False
        
    # string is float!
    return True
 
def string_to_list(str_of_floats):
    '''
    return legal list or None
    '''
    # enter string to list
    lst = str_of_floats.split()
    # check numbers if legal
    for char in lst:
        if not is_float(char):
            return None
       
    return lst

 
def mean(float_list):
    '''
    check list of numbers and return average
    '''
    # str list to int list
    float_list = [float(i) for i in float_list]
    lst_sum = sum(float_list)
    
    # claculate list average 
    return lst_sum/len(float_list)
            
def sd(float_list):
    '''
    get list of numbers and calculate sd
    '''
    float_list = [float(i) for i in float_list]
    sum_sd = 0
    for num in float_list:
        count = (num - mean(float_list))**2 
        sum_sd += count
    return ((1/len(float_list))*sum_sd)**0.5
    
def median(float_list):
    '''
    get list of numbers and claculate median
    '''
    # str list to int list
    float_list = [float(i) for i in float_list]
    float_list.sort()
    x = len(float_list)
    
    # check if len is even or odd
    if x % 2 != 0:
        return float_list[(x//2)]
    else:
        return (float_list[(x//2)-1]+float_list[(x//2)])/2
    
if __name__ == "__main__":
     
    # read from txt
    f = open("numbers.txt", "r")
    read_nums = f.read()
    f.close
    
    stat = open("stats.txt", "w")
    
    # copy text to list
    lst = string_to_list(read_nums)
    
    if lst is None:
        stat.write("illegal input")
    else:

        # calculate with functins
        mean_lst = mean(lst)
        sd_lst = sd(lst)
        median_lst = median(lst)
    
        # paste sums to new txt file
        stat.write("mean:{:22.2f}\nstandard deviation:{:8.2f}\nmedian:{:20.2f}".format(mean_lst,sd_lst,median_lst))
    stat.close()
        
    
    