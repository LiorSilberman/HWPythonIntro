#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student: Lior Silberman
id: 316456623
‫‪Assignmen‫‪t no. 1
Program: ‫‪primes‬‬ ‫‪_density‬‬.py‬‬
"""
from random import randint
import math
import numpy as np

def is_prime(num):
    '''return True if num is a prime number '''
    if(num%2 == 0):
        if (num != 2):
            return  False
    for i in range(3,int(math.sqrt(num))+1, 2):
        if (num%i == 0):
            return False
    return True

max = 10**9
check_range = 100000

def main():
    # count numbers of primes in range
    primes_counter = 0
    for x in range(check_range):
        rand_number = randint(max/2, max)
        if is_prime(rand_number):
            primes_counter += 1
            
    # check primes density
    print("‫‪density‬‬ ‫‪of‬‬ ‫‪primes‬‬: {:0.4f}".format(primes_counter/check_range))
    
    # compare with prime number theorem
    print("expected density: {:0.4f}".format(1/np.log(max)))
main()