# -*- coding: utf-8 -*-
"""
Student: Lior Silberman
ID: 316456623
Assignment no. 2
Program: num_sums.py
"""

def num_sum(n,lst):
    """
    get number and list
    return all combination to sum number
    """
    # check if list is legal
    if check_lst(lst) == False:
        return False
    if n < 0:
        return []
    if n == 0:
        return [[]]

    # collect all combinations to sum "n" as numbers in list
    all_comb = []
    for num in lst:
        for combine in num_sum(n-num,lst):
            all_comb.append(combine+[num])

    return all_comb

def check_lst(lst):
    """
    get list and check if legal
    """
    if len(lst) < 1:
        return False
    # check each number in lst if legal
    for i in lst:
        if lst.count(i) > 1:
            return False
        if i == 0:
            return False
        if type(i) == str:
            return False

    return True

def main(): 
    with open("input_ex2.txt") as f:
        row = f.read().split("\n")

    all_nums = [line.split() for line in row]
    n_lst = []
    # convert numbers in lst from str to int
    for num in all_nums:
        for j in range(len(num)):
            if num[j].isdigit():
                num[j] = int(num[j])
        n_lst.append([num[0], num[1:]])

    with open("output_ex2.txt", "w") as w:
        # call num_sum and paste len in new txt file
        for i in n_lst:
            if num_sum(i[0], i[1]) == False:
                w.write("Error\n")
            else:
                w.write("{}\n".format(len(num_sum(i[0], i[1]))))

main()