#name: Maheen Khan
#sate: 04/19/21
#lab: 13
#summary: Recursion

#global variables
my_name = "Maheen Khan"
c_num = "CIS 1400NET"
date = "3/4/2021"
lab_num = "Lab 13"
eoff = "EOF Message"
summary = "Recursion"
nnn=int(input('Enter a number'))

#Header
def Hdr():
    print(my_name,date,c_num,lab_num,)

#ftr
def ftr():
    print(summary)

#eof msg
def eof():
    print(eoff,my_name,date,c_num,lab_num)

#XCC menu driven
def XCC():
    #display menu
    print('1. Recursion')
    print('2. Exit')
    print()
#prompt user for menu selection
menu_selection = int(input('Enter selection 1 or 2:'))

#validate menu selection
while menu_selection<1 or menu_selection>2:
    print('That is an invalid selection')
    menu_selection=int(input('Enter selection 1 or 2:'))

#perform selection
    if menu_selection==1:

def RECC(times=nnn):
    if (times>0):
        print('|',times,'|','|Maheen Khan|')
        RECC(times-1)
    
#exit
def EXIT():
    if menu_selection==2:
        print('\n')
        print("You've exited the program")
#main module
def main():
    Hdr()
    XCC()
    RECC()
    EXIT()
    eof()
    ftr()
    
