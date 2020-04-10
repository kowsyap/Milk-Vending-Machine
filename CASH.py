import Tkinter as tk
import RPi.GPIO as g
from time import sleep

global app
g.setmode(g.BCM)
g.setup(2, g.IN)
global count
count = 0
global bal
bal = 0

def increaserev(channel):
    global count
    count += 1
    if count == 4:
        count = 0
        global bal
        bal = bal + 1
        print("Balance is " + str(bal))
        
g.add_event_detect(2, g.RISING, callback=increaserev)



class But(tk.Button):
    def __init__(self, master=None, **kwargs):
        self.img = tk.PhotoImage()
        tk.Button.__init__(self, master, image=self.img, compound='center', **kwargs)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('BUY WITH CASH')
        self.geometry('800x480')
        self.mon = 0
        self.Quan = 0
        self.TimerInterval = 500
        self.buttons()
        self.labels()
        self.Getval()

    def labels(self):
        box = tk.Label(self, text="INSERT CASH/COIN FOR MILK", font="helvetica 30 bold", foreground="green", bd=2,
                       relief=tk.GROOVE)
        box.place(relx=0.13, rely=0.02)

        text1 = tk.Label(self, text="Rupees", font=('Helvetica', '30'), bg='#b3aee6', bd=2, relief=tk.GROOVE)
        text1.place(relx=0.079, rely=0.4, relheight=0.1, relwidth=0.26)

        text2 = tk.Label(self, text="Litres", font=('Helvetica', '30'), bg='#b3aee6', bd=2, relief=tk.GROOVE)
        text2.place(relx=0.66, rely=0.4, relheight=0.1, relwidth=0.26)

        self.TimerInterval = 500

    def buttons(self):
        self.money = tk.IntVar()
        self.Quantity = tk.IntVar()
        button1 = But(self, textvariable = self.money, fg='black',
                      height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
        button1.place(relx=0.08, rely=0.25)

        button2 = But(self, textvariable=self.Quantity, fg='black',
                      height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
        button2.place(relx=0.66, rely=0.25)

        back = But(self, text='BACK', fg='black',
               height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE, command=lambda: self.destroy(),bg='RED', activebackground='RED')
        back.place(relx=0.02, rely=0.8)

        button1 = But(self, text='FINISH', fg='black', bg='GREEN', activebackground='GREEN',
                      height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
        button1.place(relx=0.72, rely=0.8)

    def Getval(self):
        ## replace this with code to read sensor
        self.money.set(self.mon)
        self.mon = bal
        self.Quantity.set(self.Quan)
        self.Quan = 0.02*bal
        # Now repeat call
        self.var = self.after(self.TimerInterval, self.Getval)

global app
app = App()
app.mainloop()