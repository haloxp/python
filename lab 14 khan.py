#name: Maheen Khan
#date: 05/02/21
#class: CIS 1400 Net05
#lab 14

#global variables
name ="Maheen Khan"
date="05/02/21"
labnum = "14"
cnum= "1400-net"
eofmsg="eof message"
summary= "Collects and returns quizzes graded"

letter1=("A,B,C,D,F")
letter2=(90,80,70,60)

missq=0
questq=0
somequiz=None

error = "\tINVAlID AMOUNT!\n"

titles=("Enter the following information:", '\tAmount of Questions:\t',
        '\tNum Questions Missed:\t','Each Question is worth','pts.',
        '\tScore:\t','\tGrade:\t')
midterm_= """
+--------+
| midterm|
+--------+
"""
title1= """
+--------+
| Quiz 1 |
+--------+
"""
title2= """
+--------+
| Quiz 2 |
+--------+
"""
title3= """
+--------+
| Quiz 3 |
+--------+
"""
title4= """
+--------+
| Quiz 4 |
+--------+
"""
title5= """
+--------+
| Quiz 5 |
+--------+
"""
title6= """
+--------+
| Quiz 6 |
+--------+
"""
title7= """
+--------+
| Quiz 7 |
+--------+
"""
title8= """
+--------+
| Quiz 8 |
+--------+
"""
title9= """
+--------+
| Quiz 9 |
+--------+
"""
title10= """
+--------+
| Quiz 10|
+--------+
"""
title11= """
+--------+
| Quiz 11|
+--------+
"""
title12= """
+--------+
| Quiz 12|
+--------+
"""
title13= """
+--------+
| Quiz 13|
+--------+
"""
title14= """
+--------+
| Quiz 14|
+--------+
"""

title15= """
+--------+
| Quiz 15|
+--------+
"""

#hdr
def hdr():
    print(name+',', date+ ',',cnum+',',labnum,'\n')

#footer
def ftr():
    print(summary)
#eof msg
def eof():
    print(eofmsg+',',name+',',date+',',cnum+',',labnum)
#general class assignments
class Assignment:
    #set score var to something
    def set_score(self,s):
        self._score=s
    #return score
    def get_score(self):
        return self._score
    #get grade
    def get_grade(self):
        #A
        if self._score >= letter2[0]:
            grade = letter1[0]
        #B
        elif self._score >= letter2[1]:
            grade = letter1[1]
        #C
        elif self._score >= letter2[2]:
            grade = letter1[2]
        #D
        elif self._score >= letter2[3]:
            grade = letter1[3]
        #F
        else:
            grade = letter1[4]
            
        return grade
class Quiz(Assignment):
    #constructor - calculates score
    def __init__(self,qs,miss):
        #save variables as class vars
        self._quests=qs
        self._missed=miss
        #determine what each question is worth
        self._ptseach = 100.0/self._quests
        #calculate a score
        numscore= 100.0 - (self._missed * self._ptseach)
        #set the score via inherited method
        self.set_score(numscore)
    #returns pt value is for each question
    def get_ptseach(self):
        return self._ptseach
    #returns num of missed questions
    def get_missed(self):
        return self._missed
#get inputs - missed questions and amount of questions
def getinfo():
    global missq
    global questq

    print(titles[0])
    questq =int(input(titles[1]))

    #input validation - can't miss more questions than amount of questions
    valid = False
    while not valid:
        missq = int(input(titles[2]))
        if missq > questq:
            print(error)
        else:
            valid = True
    print()
#displays all info about a quiz
def disp():
    global somequiz
    #creates an object for the quiz
    somequiz = Quiz(questq, missq)

    print(titles[3], somequiz.get_ptseach(), titles[4])
    print(titles[5], somequiz.get_score())
    print(titles[6], somequiz.get_grade())

#collects and display info about a midterm
def midterm():
    print(midterm_)

    getinfo()
    disp()
#collects and display info about quiz 1
def quiz1():
    print(title1)
    getinfo()
    disp()
#collects and display info about quiz 2
def quiz2():
    print(title2)

    getinfo()
    disp()
#collects and display info about quiz 3
def quiz3():
    print(title3)

    getinfo()
    disp()
#collects and display info about quiz 4
def quiz4():
    print(title4)

    getinfo()
    disp()
#collects and display info about quiz 5
def quiz5():
    print(title5)

    getinfo()
    disp()
#collects and display info about quiz 6
def quiz6():
    print(title6)

    getinfo()
    disp()
#collects and display info about quiz 7
def quiz7():
    print(title7)

    getinfo()
    disp()
#collects and display info about quiz 8
def quiz8():
    print(title8)

    getinfo()
    disp()
#collects and display info about quiz 9
def quiz9():
    print(title9)

    getinfo()
    disp()
#collects and display info about quiz 10
def quiz10():
    print(title10)

    getinfo()
    disp()
#collects and display info about quiz 11
def quiz11():
    print(title11)

    getinfo()
    disp()
#collects and display info about quiz 12
def quiz12():
    print(title12)

    getinfo()
    disp()

#collects and displays info about quiz 13
def quiz13():
    print(title13)

    getinfo()
    disp()
#collects and displays info about quiz 14
def quiz14():
    print(title14)

    getinfo()
    disp()

#collects and displays info about quiz 15
def quiz15():
    print(title15)

    getinfo()
    disp()
    


#functions in main
def main():
    hdr()
    quiz1()
    quiz2()
    quiz3()
    quiz4()
    quiz5()
    quiz6()
    quiz7()
    quiz8()
    quiz9()
    quiz10()
    quiz11()
    quiz12()
    quiz13()
    quiz14()
    quiz15()
    midterm()
    ftr()
    eof()
main()
