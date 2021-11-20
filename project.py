# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 19:56:17 2021

@author: Kashish
"""

'PROGRAM TO COUNT FREQUENCY OF A CHAR IN A LIST CONVERTED TO A STRING'


#function definition that will accept


#a string paameter, count the no. of times a character is present inside it

#Function that returns frequency of a character
def countchar(list, ch):
    count = 0
    for char in list:
        for i in char:
            if i == ch:
                count = count+1
    return count


def createlist(list):
    number_of_elements = int(
        input("Enter the number of elements you want in the list: ")) #Asks the user to enter number of elements
    for i in range(number_of_elements):
        str_input = str(input("Enter the element: ")) #Asks the user to enter the elements
        list.append(str_input)
    print(list) #Prints the list
    print("N O W    C O N V E R T I N G    T H E    A B O V E    L I S T   T O    S T R I N G")    


# main code
# function calls
choice="yes" #repeats if user enters yes
while(choice=="yes"):
    list = []
    createlist(list)
    ch1 = input("Enter the character to count : ") #Asks user to enter character to count
    result = countchar(list, ch1)
    if result == 0:
        print(ch1, "does not exist in the list")
    else:
        print(ch1, "exist", result, "times in the string")
    choice=input("type yes to repeat")

