# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:50:00 2026

@author: benjamin.nguyen
"""

def charcounter(password):
    specialchar = "!@#$%^&*()_+-=.?"
    charcount = 0
    uppercount = 0
    lowercount = 0
    numcount = 0
    specialcount = 0
    for char in password:
        charcount += 1
        if char.isupper():
            uppercount += 1
        elif char.islower():
            lowercount += 1
        elif char.isdigit():
            numcount += 1
        elif char in specialchar:
            specialcount += 1
    return charcount, lowercount, numcount, specialcount, uppercount
def passcheck(password):
    charcount, lowercount, numcount, specialcount, uppercount = charcounter(password)
    if charcount < 15:
        print("Password must be at least 15 characters long. Try again")
    if uppercount < 1:
        print("Password must contain at least one uppercase character. Try again")
    if lowercount < 1:
        print("Password must contain at least one lowercase character. Try again")
    if numcount < 1:
        print("Password must contain at least one numeric character. Try again")
    if specialcount < 1:
        print("Password must have one special character among the following: !@#$%^&*()_+-=?. Try again")
    if charcount <15 or uppercount < 1 or lowercount <1 or numcount < 1 or specialcount < 1:
        return False
    else:
        return True
def validation(password):
    while passcheck(password) == False:
        password = input('try another password: ')
        charcounter(password)
        passcheck(password)
    else: 
        print("valid password entered")
def bruteforcecalc(password):
    charcount, lowercount, numcount, specialcount, uppercount = charcounter(password)
    guessPerSecond = int(input('enter the amount of guesses per second: '))
    keypool = 0
    for num in range(0,lowercount):
        keypool += 26
    for num in range(0,uppercount):
        keypool += 26
    for num in range(0,numcount):
        keypool += 10
    for num in range(0,specialcount):
        keypool += len('!@#$%^&*()_+-=.?')
    combinations = keypool **charcount
    timetocrack = combinations / (2* guessPerSecond)
    print(f'The amount of combinations is {combinations}. Time to crack the password at {guessPerSecond} guesses per second is {timetocrack} seconds')
password = input("password: ")
validation(password)
bruteforcecalc(password)
    
    
        