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

def XCC():
    print('1. Recursion')
    print('2. Exit')
    print()

menu_selection=int(input('Enter selection 1 or 2:'))


while menu_selection<1 or menu_selection>2:
        print('That is an invalid selection')
        menu_selection=int(input('Enter selection 1 or 2:'))
if menu_selection==1:
    def RECC(times=nnn):
        if (times>0):
            print('|',times,'|','|Maheen Khan|')
            RECC(times-1)
elif menu_selection==2:
    def EXIT():
        print('\n')
        print("You've exited the program.")
def main():
    Hdr()
    XCC()
    RECC()
    EXIT()
    eof()
    ftr()
main()

