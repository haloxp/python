#name: Maheen Khan
#Date:3/26/21
#Lab: lab 8
#Summary: Array

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/26/2021"
lab_num = "Lab 8"
eoff = "EOF Message"
summ = "Array"

#headr function
def hdr():
    print(my_name,date,c_num,lab_num, '\n', '\n', '\n')

#building a manual array list, printing by list.
def fun():
    array=[66,2,99,33,22,1,67,100,3]
    print("This is my data in my Array", array, '\n','\n','\n')
    print("This is a list print of the Data",'\n','\n','\n')
    
#bubble sort the array in ascending order
def bubsort():
    #print initial array
    print(array)
    #set to last value
    max_ele=len(array)-1
    #while not reaching end of array(when list has been sorted)
    while max_ele>=0:
        index=0
        #while still going through array
        while index <=1 max_ele-1:
            #see if element is greater than the subsequent element
            if array[index]>array[index+1]:
                #swap the elements so that the lesser one is first
                temp = array[index]
                array[index]=array[index+1]
                array[index+1]=temp

                #print the array to witness changes
                print(array)
            #increment index
                index +=1
        #decrease max element
        max_ele-=1
#footer function
def ftr():
    print(summ, '\n','\n','\n')

#end of file
def eof():
    print(eoff,my_name,date,c_num,lab_num, '\n','\n','\n')

#main function
def main():
    hdr()
    fun()
    ftr()
    eof()
