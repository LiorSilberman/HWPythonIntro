# -*- coding: utf-8 -*-
"""
Student: Lior Silberman
ID: 316456623
Assignment no. 1
Program: vigenere.py
"""

from string import ascii_lowercase
dic = {}
value = 0
for c in ascii_lowercase:
    dic[c] = value
    value += 1    

def key_by_value(val):
    '''
    get value and return appropriate key from dic
    '''
    for key, value in dic.items():
        if val == value:
            return key
        
def add_letters(lhs, rhs):
    '''
    get two strings and return key of the sum lhs+rhs
    '''
    add_result = None
    
    is_legal_args = lhs.isalpha() and rhs.isalpha()
    
    # calculate value
    if len(lhs) == 1 and len(rhs) == 1 and is_legal_args:
        add_result = key_by_value((dic[lhs.lower()] + dic[rhs.lower()]) % 26)

    return add_result

def depress_letters(lhs, rhs):
    '''
    get two strings and return key of the sum lhs-rhs
    '''
    depress_result = None
    
    is_legal_args = lhs.isalpha() and rhs.isalpha()
    
    # calculate value
    if len(lhs) == 1 and len(rhs) == 1 and is_legal_args:
        depress_result = key_by_value((dic[lhs.lower()] - dic[rhs.lower()]) % 26)

    return depress_result

def add_strings(lhs, rhs):
    '''
    get two strings and return encrypted string
    '''
    encrypted_string = ""
    result = None
    
    # run on min len and calculate lhs+rhs
    for i in range(min(len(lhs) , len(rhs))):
        new_encrypted = add_letters(lhs[i], rhs[i])
        
        if new_encrypted is None:
            encrypted_string = ""
            break
        encrypted_string += new_encrypted
    
    if len(encrypted_string):
        result = encrypted_string
    
    return result

def vigenere_encrypt(lhs, k):
    '''
    get string and secret word and return encryped string
    '''
    # create only alpha letters string
    new_lhs = "".join([i.lower() for i in lhs if i != " " and i != "ג" and i.isalpha()])
    t = k*((len(new_lhs)//len(k)) + 1)
    
    return add_strings(new_lhs, t)
 
def vigenere_decreypt(w, k):
    '''
    get string and secret word and return decryped string
    '''
    # check if key is legal
    for j in k:
        if not j.isalpha():
            return None
    t = k*((len(w)//len(k)) + 1)
    orig_string = ""
    
    # create original string
    for i in range(min(len(w) , len(t))):
        orig_string += depress_letters(w[i], t[i])
        
    return orig_string
   
def main():
    
    while True: 
        input_user = input("enter e or d: ")
        if input_user != "e" and input_user != "d":
           break
        if input_user == "e":
            key_encrypt = input("enter key encrypt: ")
            file_name = input("enter file name: ")
             
            try:
                f = open(file_name, "r")
                s = f.read()
                f.close()
                n_f = open(file_name.replace("txt", "vig"), "w")
                n_f.write(vigenere_encrypt(s, key_encrypt))
                n_f.close()
                
            except IOError:
                print("File not accessible")
                
        if input_user == "d":
            key_encrypt = input("enter key encrypt: ")
            file_name = input("enter file name: ")
            
            try:
                de_f = open(file_name, "r")
                dec = de_f.read()
                de_f.close()
                print(vigenere_decreypt(dec, key_encrypt))
            except IOError:
                print("File not accessible")
          
main()       