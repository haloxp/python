#Maheen Khan
#Date: 4.11.21
#lab: 11 Xtra Credit
#summ - sort array in descending and ascending

name="Maheen Khan"
date="04/11/21"
cnum="CIS NET1400"
lab="11"
eofmsg="EOF message"
summary="sort array in descending and ascending"

#file header
def hdr():
    print(name + ',',date + ',',cnum + ',', lab, '\n')
    print()
#sort module
def SRT():
    array = [1,3,5,7,9,2,4,6,8,0]
    print ('unsorted',array)

def XC():
#sort array in ascending order
    array = [1,3,5,7,9,2,4,6,8,0]
    array.sort()
    print('ascending',array)
#sort array in decending order
def DXC():
    array = [1,3,5,7,9,2,4,6,8,0]
    array.sort(reverse=True)
    print('decending',array)
    
#footer
def ftr():
    print(summary,'\n')
    
def main():
    hdr()
    SRT()
    XC()
    DXC()
    ftr()
main()
