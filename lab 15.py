#name: Maheen Khan
#lab: lab 15 example GUI
#class: CIS 1400 NET05
#DATE: 04/04/21
#summary: GUI

#This program displays two labels with text
import tkinter

class MYGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #create two label widget
        self.label1 = tkinter.Label(self.main_window, \
                                    text= 'Header: Maheen Khan,04.04.21,CIS 1400 NET05,lab 15')
        self.label2 = tkinter.Label(self.main_window, \
                                    text='Footer: GUI')
        self.label3 = tkinter.Label(self.main_window, \
                                    text='EOF Message: End of File')
        self.label4 = tkinter.Label(self.main_window, \
                                    text='Course Number: CIS 1400 NET05')
        self.label5 = tkinter.Label(self.main_window, \
                                    text='Date: 04.04.21')
        self.label6 = tkinter.Label(self.main_window, \
                                    text = 'Maheen Khan')

        #call both label widgets' pack method
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.label6.pack()

        #enter tinker main loop
        tkinter.mainloop()
#create instance of MyGUI class
my_gui =MYGUI()
