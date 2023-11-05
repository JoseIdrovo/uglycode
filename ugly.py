"""
Created on November 4 2023
@author: cringeinducing 
"""


import sys
import math 

def Next_Letter(number, array):
    next_number = number
    if number == len(array):
        return array[next_number]
    return array[next_number]

def main():
    number = 0
    ListOfWords = ['w','e','c','h','a','n','g','e','d','t','h','e','w','o','r','l','d']
    # First Line 
    for y in range(12):
        if  y == 4 or y == 5 or y == 6 or y == 7 or y == 8:
            print(" " + Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        elif y == 10:
            print(" ")
        else:
            print(" ",end=" ")

    # Second Line 
    for y in range(12):
        if y == 2:
            print(" "+ Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        if y == 8:
            print("           " + Next_Letter(number,ListOfWords) +  " ",end="")
            number += 1
        elif y == 10:
            print("")
        else:
            print("",end=" ")

    # Third Line 
    for y in range(12):
        if y == 1: 
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 9: 
            print("                " + Next_Letter(number,ListOfWords) +  " ",end="")
            number += 1
        elif y == 10:
            print("")
        else:
            print("",end=" ")
        

 # Next Lines
    for y in range(12):
        if y == 0:
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 11:
            print("                          " + Next_Letter(number,ListOfWords) +  " ")
            number += 1
        
 

    for y in range(12):
        if y == 0:
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 11:
            print("                            " + Next_Letter(number,ListOfWords) +  " ")
            number += 1

    for y in range(12):
        if y == 0:
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 11:
            print("          I                 " + Next_Letter(number,ListOfWords) +  " ")
            number += 1

    for y in range(12):
        if y == 0:
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 11:
            print("           changed          "+ Next_Letter(number,ListOfWords) + " ")
            number += 1

    for y in range(12):
        if y == 0:
            if number == 17:
                number = 0
            print(Next_Letter(number,ListOfWords),end="")
            number += 1
        elif y == 11:
            if number == 17:
                number = 0
            print("       the                  " + Next_Letter(number,ListOfWords) +  " ")
            number += 1


    for y in range(12):
        if y == 0:
            print(" " + Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        elif y == 11:
            print("       world              " + Next_Letter(number,ListOfWords) +  " ")
            number += 1

    # Third to last Line 
    for y in range(12):
        if y == 1: 
            print(" " + Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        elif y == 9: 
            print("                " + Next_Letter(number,ListOfWords) +  " ",end="")
            number += 1
        elif y == 10:
            print("")
        else:
            print("",end=" ")

    # Second to last Line 
    for y in range(12):
        if y == 2:
            print(" "+ Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        if y == 8:
            print("             " + Next_Letter(number,ListOfWords) +  " ",end="")
            number += 1
        elif y == 10:
            print("")
        else:
            print("",end=" ")

    # Last Line 
    for y in range(12):
        if  y == 4 or y == 5 or y == 6 or y == 7 or y == 8:
            print(" " + Next_Letter(number,ListOfWords) + " ",end="")
            number += 1
        elif y == 10:
            print(" ")
        else:
            print(" ",end=" ")
if __name__ == "__main__":
    main()

