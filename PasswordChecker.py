# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:02:11 2026

@author: bentn
"""
#password security checker

def passwordcheck():
#Input for password and initialization of variables
    password = input("Enter your password here: ")
    specialchar = "!@#$%^&*()_+-=.?"
    charcount = 0
    uppercount = 0
    lowercount = 0
    numcount = 0
    specialcount = 0
#For loop checks each character and accumulates character values
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
#Input Validation of accumulated values. Checks if password meets the standard requirements
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
#If input fails to meet requirements, this while loop will iterate until a valid password is entered.
        while charcount < 15 or uppercount < 1 or lowercount < 1 or numcount < 1 or specialcount < 1:
            password = input("Enter your password here: ")
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
            else:
                print("Valid password entered.")
passwordcheck()

