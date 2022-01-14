#Name: Maheen Khan
#Date: 3/4/2021
#Lab 6
#Summary:Functions, Modules, Input, While, return values, counters

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/4/2021"
lab_num = "Lab 6"
eoff = "EOF Message"
summ = "Functions, Modules, Input,IF's While, return values, counter "

import random

#headr function
def hdr():
    print(my_name,date,c_num,lab_num, '\n')

#This random number module creates a random number of developer's choice
#Example (1, 40) and (41, 60) as well as (61, 88)
def rdex():
    print('This code will print a random number between 1 and 88')
    for count in range(10):
        #Get a random number
        number = random.randint(1,88)
        #display the number. And Count how many numbers we print.
        count+=1
        print("This is number", count, number)

#Average Calculation
def acalc():

    avg=((88)/2)
    print("This is the average of 88/2 =", avg)
    
#footer functoin
def ftr():
    print(summ, '\n')

#end of file
def eof():
    print(eoff,my_name,date,c_num,lab_num, '\n')

#main function
def main():
    hdr()
    rdex()
    acalc()
    ftr()
    eof()
main()
