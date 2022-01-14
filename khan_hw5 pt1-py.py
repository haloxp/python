#Name: Maheen Khan
#Date: 02/28/2021
#Lab: Lab5 pt 1
#Summary: Functions, Modules, Input, IF's

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "2/28/2021"
lab_num = "Lab5"
eoff = "EOF Message"
summ = "Functions, Modules, Input, IF's"
hint = "Do you have all the Modules?"

#header function
    def hdr():
	print(my_name,date,c_num,lab_num,'\n')

#This Module prompts the user to enter three test scores.
#It displays the average of those scores and congradulates
#the user if the average is 100 or greater.	

def calk():

#Get the three test scores
    test1 = float(input('Enter the score for test 1: '))
    test2 = float(input('Enter the score for test 2: '))
    test3 = float(input('Enter the score for test 3: '))
#calculate the average test score.
    average = (test1 + test2 + test3 ) /3.0
#Print the average
    print('The average score is', average)
#If the average is 100 or greater,
#congradulate the user.
    if average ==100:
        print("Congradulations!")
        print("That is a great average")

#footer function
    def ftr():
        print(summ,'\n')

#end of file message
    def hdr():
        print(eoff,my_name,date,c_num,lab_num,hint,'\n')

#main function
    def main():
        hdr()
        calk()
        ftr()
        eof()
    main()
