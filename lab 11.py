#name: Maheen Khan
#date:04/11/21
#lab:11
#summary:menu driven

#############VARS##############

#variables for hdr ftr eof
name="Maheen Khan"
date="04/11/21"
cnum="CIS NET1400"
lab="11"
eofmsg="EOF message"
summary="Menu Driven"

############Functions##########

#file header
def hdr():
    print(name + ',',date + ',',cnum + ',', lab, '\n')
    print()
#Example of Menu Driven code, with 4 selections including Exit selection
def MDM():

#displays menu
    print('1. Convert inches to centimeters.','\n')
    print('2. Convert feet to meters.','\n')
    print('3. Convert miles to kilometers.','\n')
    print('4. Exit menu. Goodbye!', '\n')

#prompt user for selection
    menu_selection = int(input('Enter 1,2,3,4:'))
    print()
#validate menu selection
    while menu_selection <1 or menu_selection >4:
        print(menu_selection,'is an invalid selection - Please try again')
        menu_selection = int(input('Enter 1,2,3,4:'))
        print()
#perform the selected operation
    if menu_selection ==1:
#convert inches to centimeters.

        inches = float(input('Enter the number of inches:'))
        centimeters= inches*2.54
        print(inches,'inches is equal to', centimeters, 'centimeters.', '\n')
    elif menu_selection ==2:
#convert feet to meters
        feet= float(input('Enter number of feet:'))
        meters = feet *0.3048
        print(feet, 'feet is equal to', meters, 'meters.','feet')
    elif menu_selection ==3:
#Convert miles to kilometers
        miles = float(input('Enter number of miles'))
        kilometers = miles*1.609
        print(miles,'miles is equal')
#Exit program
    elif menu_selection ==4:
        print('\n')
        print('**** You have exited the Program, Have a Nice Day - Goodbye!****')
#footer
def ftr():
    print(summary,'\n')

#end of file message
def eof():
    print(eofmsg +',' ,name+ ',',date+ ',',cnum+ ',',lab, '\n')

def main():
    hdr()
    MDM()
    ftr()
    eof()
main()
