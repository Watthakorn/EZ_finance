import sys
from Tkinter import *
import os

def call_a():
    '''
    call_a(...)
        Open Type A in new window
    '''
    os.startfile('TypeA.pyw')

def call_b():
    '''
    call_b(...)
        Open Type B in new window
    '''
    os.startfile('TypeB.pyw')
def call_help():
    '''
    call_help(...)
        Open Help in new window
    '''
    os.startfile('Help_Ez.txt')
def call_about_us():
    '''
    call_about_us(...)
        Open About us in new window
    '''
    os.startfile('About_us.txt')

class main():
    '''
    main menu
    '''
    def __init__(self):
        self = Tk()
        self.geometry('300x250+500+250')
        self.title('Ez-Finance')
        img = PhotoImage(file='pic1.gif')
        background_label = Label(self, image=img).pack()
        menubar = Menu(self)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=call_help)
        helpmenu.add_command(label="About us", command=call_about_us)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)

        close = Button(self, text="close", command=self.destroy)
        a = Button(self, text="Future Value", command=call_a)
        b = Button(self, text="Present Value", command=call_b)
        a.place(relx=.3, rely=.6, anchor="c")
        b.place(relx=.7, rely=.6, anchor="c")

        close.place(relx=.9, rely=.9, anchor="c")

        self.mainloop()
main()
