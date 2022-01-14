#name: Maheen Khan
#date: 05/11/21
#class: CIS !400 NET05
#Summary: FINAL

#random function
import random

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/4/2021"
lab_num = "Lab 13"
eoff = "EOF Message"
summary = "Final Exam"

#create random number value
list1=random.randint(1,100)
list2=random.randint(1,100)
list3=random.randint(1,100)
list4=random.randint(1,100)
list5=random.randint(1,100)

#set random number to equal to array for sorting purposes
array = [list1,list2,list3,list4,list5]

#header module
def hdr():
    print(my_name,date,c_num,lab_num)

#footer module
def ftr():
    print(summary)

#end of message module
def eof():
    print(eoff)

#random number module
def Randy():
    print('5 random numbers between 1-100 will print')
    for count in range(5):
        array = [list1,list2,list3,list4,list5]
        #Display number
        print('These are random numbers',array)
#Sort array ascending
def SortA():
    print('ascending:')
    array = [list1,list2,list3,list4,list5]
    array.sort()
    print(array)
    

#Sort array descending
def SortD():
    array = [list1,list2,list3,list4,list5]
    array.sort(reverse=True)
    print(array)
#IF I PUT IS COMMAND, PUT HERE
def ISN():

        print('')

#prompt user to enter a sentence

sentence = input("Enter a sentence")



#initialize index(loop counter)

index=0



#intialize index_count

alnum_count =0



#count the number of alphanumeric characters

while index<len(sentence):

        if sentence[index].isalnum():

            alnum_count=alnum_count +1

        index=index +1

#Display the number of alphanumeric characters

print('That string has', alnum_count, 'alphabetical letters/numbers')





##########################ISP########################

#alpha module

def ISP():

        print('')

#prompt user to enter a sentence

sentence = input("Enter a sentence: ")



#intialize index (loop counter)

index=0



#initialize alpha_count accumulator

alpha_count = 0



#count the number of alpha characters

while index<len(sentence):

            if sentence[index].isalpha():

                alpha_count=alpha_count +1

            index=index +1

# Display the number of uppercase characters.

print('That string has', alpha_count, 'alphabetical letters.')







#######################ISD##########################

#isdigit module

def ISD():

        print('')

#prompt user to enter sentence

sentence=input("Enter a number")



#initialize index (loop counter)

index=0



#initialize digit_count accumulator

digit_count=0



#count the number of digit characters

while index < len(sentence):

        if sentence[index].isdigit():

            digit_count = digit_count + 1

        index = index + 1

 # Display the number of digit characters.

print('That string has', digit_count, ' numbers.')





###########################ISL###################

#islower module

def ISL():

        print('')

#prompt user to enter sentence

sentence=input("Enter a sentence")



#initialize index (loop counter)

index=0



#initialize lower_counter accumulator

lowercase_count=0





#count the number of lowercase characters

while index < len(sentence):

    if sentence[index].islower():

        lowercase_count = lowercase_count + 1

    index = index + 1

#Display the number of lowercase characters.

print('That string has', lowercase_count, ' lowercase.')





##########################ISS#####################

#isspace module

def ISS():

        print('')

#prompt user to enter sentence

sentence=input("Enter a sentence")



#initialize index (loop counter)

index=0



#initialize space_count accumulator

space_count=0



#count the number of spaces

while index < len(sentence):

    if sentence[index].isspace():

        space_count = space_count + 1

    index = index + 1

#Display the number of lowercase characters.

print('That string has', space_count, ' spaces.')







########################ISU###########################

#isupper module

def ISU():

        print('')

#prompt user to enter sentence

sentence=input("Enter a sentence")



#initialize index (loop counter)

index=0



#initialize upper accumulator

uppercase_counter=0



#count the number of uppercase characters

while index < len(sentence):

    if sentence[index].isupper():

        uppercase_count = uppercase_count + 1

    index = index + 1

#Display the number of uppercase characters.

print('That string has', uppercase_counter, ' upercases.')


#Menu Driven module
def Mennu():
    print('1.Build Array with a Random number, 5 points')
    print('2.Print the Array unsorted, to the display, 5 points.')
    print('3.Sort the Array in ascending order, 5 points.')
    print('4.Print the Array to the display and to a file named “PFILEA”. [PFILEA.txt], 10 points.')
    print('5.Sort the Array in descending order, 5 points.')
    print('6.Print the Array to the display and to a file named “PFILED”. [PFILED.txt], 10 points.')
    print('7.Exit the Menu/Program. 5 points')
    
    #have user select option 1-7
    select = int(input('Enter option number 1-7:'))
    print()
    
    #print out selection number
    while select <1 or select> 8:
        print(select,'invalid number - try again')
        print('Enter option number 1-8:')
    if select == 1:
        print ('random number:')
        Randy()
    elif select ==2:
        print('unsorted:')
        Randy()
    elif select ==3:
        SortA()
    elif select ==4:
        print('writing file PFILEA.txt...')
        #create PFILEA file
        myfile=open ('PFILEA.txt','w')
        array = (list1,list2,list3,list4,list5)
        nm = array
        
        
        #write file
        infile= open('PFILEA.txt','w')

        #read line from file
        line1= nm[0]
        line2= nm[1]
        line3=nm[2]
        line4=nm[3]
        line5=nm[4]

        #print out file
        myfile.write(str(nm[0])+ '\n')
        myfile.write(str(nm[1])+ '\n')
        myfile.write(str(nm[2])+ '\n')
        myfile.write(str(nm[3])+ '\n')
        myfile.write(str(nm[4])+ '\n')

        #close the file
        myfile.close
        print('PFILEA.txt is displayed')
        print(nm)
    elif select ==5:
        SortD()
        print()
    elif select ==6:
        print('writing file PFILED.txt...')
        #create PFILEA file
        myfile=open ('PFILED.txt','w')
        array = (list1,list2,list3,list4,list5)
        nm = array
        #myfile.write(nm)
        
        #openfile
        infile= open('PFILED.txt','w')

        #read line from file
        line1= nm[0]
        line2= nm[1]
        line3=nm[2]
        line4=nm[3]
        line5=nm[4]

        #print out file
        myfile.write(str(nm[0])+ '\n')
        myfile.write(str(nm[1])+ '\n')
        myfile.write(str(nm[2])+ '\n')
        myfile.write(str(nm[3])+ '\n')
        myfile.write(str(nm[4])+ '\n')
        print()
    #program exit
    elif select ==7:
        print('You have exited the program - Goodbye!')

Mennu()

#class thing
#class IS():

def main():
    hdr()
    ftr()
    eof()
    Mennu()
    Randy()
    SortA()
    SortD()
    ISN()
    ISP()
    ISD()
    ISL()
    ISS()
    ISU()
main()

