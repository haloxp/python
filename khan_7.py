#name: Maheen Khan
#Date:3/26/21
#Lab: lab 7
#Summary: Array

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/4/2021"
lab_num = "Lab 7"
eoff = "EOF Message"
summ = "Array"

#headr function
def hdr():
    print(my_name,date,c_num,lab_num, '\n', '\n', '\n')

#building a manual array list, printing by list.
def Alist():
    numbers=[44,55,2,3,7]
    average = (44+55+2+3+7)
    print("This is my data in my Array", average, '\n','\n','\n')
    print("This is a list print of the sum of Data",'\n','\n','\n')
    print("****************************************************",'\n','\n','\n')

#building a manual array list, printing by element
def Wele():
    numbers=[2,9,1,5,6,7,10 ]
    print("This is element 0=",numbers[0],)
    print("This is element 1=",numbers[1],)
    print("This is element 2=",numbers[2],)
    print("This is element 3=",numbers[3],)
    print("This is element 4=",numbers[4],)
    print("This is element 5=",numbers[5],)
    print("This is element 6=",numbers[6],)
    print("This is a Element print of the data",'\n','\n','\n')
    print("****************************************************",'\n','\n','\n')

#building a manual array list, while loop
def Fele():
    my_list=[55,2,99,1,77,88]
    index= 0
    while index<len(my_list):
        print("This is element", index,"=", my_list[index],'\n','\n','\n')
        index +=1
#footer functoin
def ftr():
    print(summ, '\n''\n','\n')

#end of file
def eof():
    print(eoff,my_name,date,c_num,lab_num, '\n','\n','\n')

#main function
def main():
    hdr()
    Alist()
    Wele()
    Fele()
    ftr()
    eof()

