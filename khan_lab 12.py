#Maheen Khan
#date: 04/16/21
#lab: 12
#CIS 1400 NET05

#global variables
name="Maheen Khan"
date="04/18/21"
cnum="CIS NET1400"
lab="11"
eofmsg="EOF message"
summary="Text Processing"


#headr function
def hdr():
    print(name,date,cnum,lab, '\n')

############################ISN#######################
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

#footer
def ftr():
    print(summary)
#eof message
def eof():
    print(eofmsg,name,date,cnum,lab)

def main():
    hdr()
    ISN()
    ISP()
    ISD()
    ISL()
    ftr()
    eof()
main()
