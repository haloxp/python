#Maheen Khan
#Date: 03/09/2021
#Test: Midterm
#Summary: LOOP, IF's, Modules, Input, Random number, AVG, Summary

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/9/2021"
Test = "Midterm"
eof = "EOF Message"
summ = "LOOP, IF's, Modules, Input, Random number, AVG, Summary"


import random

#main function
def main():
    HEADER()
    LOOP()
    #AVERG()
    IFF()
    SUMM()
    FOOTER()
    EOF()

#header function
def HEADER():
    print(my_name,date,c_num,Test, '\n' , '\n', '\n')
    
#this code will print a random episode number from a TV Show series to watch.
def LOOP():
    for episode in range(3):
        #get a random episode number
        episode = random.randint(1,60)
        #display the episode number
        print('Try watching episode', episode, '\n','\n','\n')

#Average calculation
def AVERG():
#enter minutes watched per episode
    episode1 = int(input('Enter minutes spent watching episode: '))
    episode2 = int(input('Enter minutes spent watching episode: '))
    episode3 = int(input('Enter minutes spent watching episode: '))
#calculate average of minutes watched per episode
    average = (episode1 + episode2 + episode3) /2
    return (average)



def IFF():
    #minutes spent watching season 1
    if AVERG() <= 70:
        print("You've watched season 1", "\n","\n","\n")
    else:
    #minutes spent watching season 2
        print("You've watched season 2", "\n","\n","\n")

#this module will calculate the sum of eye rolling in TV show 
def SUMM():
    #initialized value
    total=0
    # per each season (there is only 2 seasons) enter total amount of eye roll calculation
    for count in range(2):
        number = int(input('Enter the amount of times character rolls eyes per season:'))
        total = total + number

        #display total
        print('The total is', total)

#footer function
def FOOTER():
    print(summ, '\n','\n','\n')

#end of file
def EOF():
    print(eof,my_name,date,c_num,Test, '\n', '\n', '\n')

#_average = AVERG()    


main()
