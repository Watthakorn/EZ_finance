'''Present type of application'''
import sys, os
from Tkinter import *
import table1to4 as tb

def call_help():
    '''
    how to use program.txt
    '''
    os.startfile('help_typeA.txt')

def calculate(gui, interest, year, money, check):
    '''
    calculate(...)

        make Answer Label ans select table to calculate
    '''
    if check == 0:
        answer = str(tb.table_1(interest, year, money))
    else:
        answer = str(tb.table_2(interest, year, money))
    #select table

    mrefresh = Label(gui, text='              -               ')
    mlebel = Label(gui, text=answer)
    mlebel1 = Label(gui, text='Answer')
    mrefresh.place(relx=.6, rely=.8, anchor="c")
    mlebel.place(relx=.6, rely=.8, anchor="c")
    mlebel1.place(relx=.3, rely=.8, anchor="c")
    #make Answer label after table's calculate
    
class typea():
    '''Present Type'''
    def __init__(self):
        '''typea'''        
        self = Tk()
        self.geometry('400x400+600+300')
        self.title('Present')
        #make tk main interface size 400 x 400 and title
        money = StringVar()
        interest = StringVar()
        year = StringVar()
        check = IntVar()
        #make varable keeper

        img = PhotoImage(file="Now_to_Future.gif")
        imglabel = Label(self, image=img)
        imglabel.place(relx=.5, rely=.14, anchor="c")

        Radiobutton(self, text="one time",
                    variable=check, value=0).place(relx=.34,rely=.38, anchor="c")
        Radiobutton(self, text="every years",
                    variable=check, value=1).place(relx=.6, rely=.38, anchor="c")
        #Select Radiobutton to choose type of deposit money
            
        entry1 = Entry(self, textvariable=money)
        entry2 = Entry(self, textvariable=interest)
        entry3 = Entry(self, textvariable=year)
        entry1.place(relx=.6, rely=.3, anchor="c")
        entry2.place(relx=.6, rely=.5, anchor="c")
        entry3.place(relx=.6, rely=.6, anchor="c")
        #Entry form keep varable money interest year

        label1 = Label(self, text='Money      : ')
        label2 = Label(self, text='Interest   : ')
        label3 = Label(self, text='Year       : ')
        label1.place(relx=.3, rely=.3, anchor="c")
        label2.place(relx=.3, rely=.5, anchor="c")
        label3.place(relx=.3, rely=.6, anchor="c")
        #label of entry form
        
        ok = Button(self, text="OK",
                    command=lambda: calculate(self, interest.get(), year.get(), money.get(), check.get()))
        ok.place(relx=.5, rely=.7, anchor="c")
        #make OK button to sent varable to calculate fuction

        h = Button(self, text="How to use?", command=call_help)
        h.place(relx=.15, rely=.9, anchor="c")
        #how to use
        
        c = Button(self, text="close", command=self.destroy)
        c.place(relx=.9, rely=.9, anchor="c")
        #close button

        self.mainloop()
typea()
