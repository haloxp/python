#Maheen Khan
#date: 04/16/21
#lab: 12
#CIS 1400 NET05

#global variables
name="Maheen Khan"
date="04/11/21"
cnum="CIS NET1400"
lab="11"
eofmsg="EOF message"
summary="Menu Driven"

#def ISN():
    #print

#alpha module
def ISP():

#prompt user to enter a sentence
sentence = input("Enter a alphabetical sentence")

#intialize index (loop counter)
index=0

#initialize uppercase_count accumulator
alpha_count = 0

#count the number of lowercase characters
while index<len(sentence):
    if sentence[index].isalpha():
        alpha_count=alpha_count +1
    index=index

#Display the number of lowercase characters
print("That string has", alpha_count, "alphabetic letters")
