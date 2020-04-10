import tkinter as tk
#from PIL import Image, ImageTk
#import tkinter.messagebox as tmsg
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pandas as pd
    
expression = ""


def cashy():

    class But(tk.Button):
        def __init__(self, master=None, **kwargs):
            self.img = tk.PhotoImage()
            tk.Button.__init__(self, master, image=self.img, compound='center', **kwargs)

    def change_color():
        current_color = box.cget("foreground")
        next_color = "green" if current_color == "red" else "red"
        box.config(foreground=next_color)
        root.after(1000, change_color)

    top =tk.Toplevel()
    top.geometry("800x480")
    top.attributes("-fullscreen",True)
    top.config(cursor = "none")

    box = tk.Label(top, text="INSERT CASH/COIN FOR MILK", font="helvetica 30 bold", foreground="green", bd=2,
                relief=tk.GROOVE)
    change_color()
    box.place(relx=0.13, rely=0.02)

    button1 = But(top, text='500', fg='black',
                  height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
    button1.place(relx=0.08, rely=0.25)

    button2 = But(top, text='10.2', fg='black',
                  height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
    button2.place(relx=0.66, rely=0.25)

    text1 = tk.Label(top, text="Rupees", font=('Helvetica', '30'), bg='#b3aee6', bd=2, relief=tk.GROOVE)
    text1.place(relx=0.095, rely=0.4, relheight=0.1, relwidth=0.26)

    text2 = tk.Label(top, text="Litres", font=('Helvetica', '30'), bg='#b3aee6', bd=2, relief=tk.GROOVE)
    text2.place(relx=0.675, rely=0.4, relheight=0.1, relwidth=0.26)

    button1 = But(top, text='FINISH', fg='black', bg='GREEN', activebackground='GREEN',
                  height=80, width=200, font=('Helvetica', '40', 'bold'), bd=2, relief=tk.GROOVE)
    button1.place(relx=0.7, rely=0.79)
    
    back = But(top,text="Back",command=top.destroy,height=80,width=200,fg="black",bg="RED",font=('Helvetica', '40', 'bold'),bd=2,relief=tk.GROOVE)
    back.place(relx=0.02,rely=0.79)    


def cardy():
    # RFID CODE for raspi
    def RFID():
        reader =SimpleMFRC522()
        try:
            id,_=reader.read()
            #$print(id)
            
            df =pd.read_csv('data.csv')
            flag =0
            for i in range(len(df)):
                if(df['id'][i]==id):
                    l = [df['name'][i],df['balance'][i]]
                    return ([1,l])
            return 0
            
            
        finally:
            GPIO.cleanup()


    def rf():

        flag = RFID()
        if flag==0:
            tmsg.showinfo("Error", "Looks like you have not registered yet:)")
            top.destroy()
        else:
            name = flag[1][0]
            balance = flag[1][1]
            # NUMPAD START
            class But(tk.Button):
                def __init__(self, master=None, **kwargs):
                    self.img = tk.PhotoImage()
                    tk.Button.__init__(self, master, image=self.img, compound='center', **kwargs)

            def press(num):
                global expression
                expression = expression + str(num)
                equation.set(expression)
                if(int(expression) == 0):
                    equation.set("Error")
                if(int(expression) > balance):
                    equation.set("Error")
                

            def clear():
                global expression
                expression = ""
                equation.set("")

            gui = tk.Toplevel()
            gui.geometry("800x480")
            gui.attributes("-fullscreen",True)
            gui.config(cursor = "none")
            gui.configure(bg="#E0E0E0")
            
            equation = tk.StringVar()
            expression_field = tk.Entry(gui, textvariable=equation, relief=tk.FLAT, bg="#E0E0E0",
                                        font=('Helvetica', '50'))
            expression_field.place(relx=0.1, rely=0.21)
            symbol = "\u20B9"
            symbo = tk.Label(gui, text=symbol, font=('Helvetica', '60'), bg="#E0E0E0")
            symbo.place(relx=0.03, rely=0.2)
            title = "Enter Amount : "
            title = tk.Label(gui, text=title, font=('Helvetica', '30', 'bold'), bg="#E0E0E0", fg="red")
            title.place(relx=0.03, rely=0.08)

            # ------------------------------------
            n1 = "Name : "+ name
            nn = tk.Label(gui, text=n1, font=('Helvetica', '30', 'bold'), bg="#E0E0E0", fg="blue")
            nn.place(relx=0.03, rely=0.7)

            bal = "Balance :"+str(balance)
            balan = tk.Label(gui, text=bal, font=('Helvetica', '30', 'bold'), bg="#E0E0E0", fg="blue")
            balan.place(relx=0.03, rely=0.8)
            # -------------------------------
            can = tk.Canvas(gui, bg="#E0E0E0")
            can.place(relx=0.5, rely=0.5, anchor=tk.W)

            button1 = But(can, text=' 1 ', fg='black', bg='#5DADE2',
                          command=lambda: press(1), height=80, width=80, font=('Helvetica', '20'))
            button1.grid(row=2, column=0, padx=10, pady=10)

            button2 = But(can, text=' 2 ', fg='black', bg='#5DADE2',
                          command=lambda: press(2), height=80, width=80, font=('Helvetica', '20'))
            button2.grid(row=2, column=1, padx=10, pady=10)

            button3 = But(can, text=' 3 ', fg='black', bg='#5DADE2',
                          command=lambda: press(3), height=80, width=80, font=('Helvetica', '20'))
            button3.grid(row=2, column=2, padx=10, pady=10)

            button4 = But(can, text=' 4 ', fg='black', bg='#5DADE2',
                          command=lambda: press(4), height=80, width=80, font=('Helvetica', '20'))
            button4.grid(row=3, column=0, padx=10, pady=10)

            button5 = But(can, text=' 5 ', fg='black', bg='#5DADE2',
                          command=lambda: press(5), height=80, width=80, font=('Helvetica', '20'))
            button5.grid(row=3, column=1, padx=10, pady=10)

            button6 = But(can, text=' 6 ', fg='black', bg='#5DADE2',
                          command=lambda: press(6), height=80, width=80, font=('Helvetica', '20'))
            button6.grid(row=3, column=2, padx=10, pady=10)

            button7 = But(can, text=' 7 ', fg='black', bg='#5DADE2',
                          command=lambda: press(7), height=80, width=80, font=('Helvetica', '20'))
            button7.grid(row=4, column=0, padx=10, pady=10)

            button8 = But(can, text=' 8 ', fg='black', bg='#5DADE2',
                          command=lambda: press(8), height=80, width=80, font=('Helvetica', '20'))
            button8.grid(row=4, column=1, padx=10, pady=10)

            button9 = But(can, text=' 9 ', fg='black', bg='#5DADE2',
                          command=lambda: press(9), height=80, width=80, font=('Helvetica', '20'))
            button9.grid(row=4, column=2, padx=10, pady=10)

            button0 = But(can, text=' 0 ', fg='black', bg='#5DADE2',
                          command=lambda: press(0), height=80, width=80, font=('Helvetica', '20'))
            button0.grid(row=5, column=1, padx=10, pady=10)

            enter = But(can, text=' ENTER ', fg='black', bg='#17A589',
                        command=tk.NONE, height=80, width=80, font=('Helvetica', '15'))
            enter.grid(row=5, column=2, padx=10, pady=10)

            clear = But(can, text='CLEAR', fg='black', bg='#E74C3C',
                        command=clear, height=80, width=80, font=('Helvetica', '15'))
            clear.grid(row=5, column='0', padx=10, pady=10)
            
            
            
        # NUMPAD END



    top =tk.Toplevel()
    top.geometry("800x480")
    top.config(cursor = "none")
    top.attributes("-fullscreen",True)
    canvas = tk.Canvas(top, width=800, height=480)
    canvas.pack()
    img = tk.PhotoImage(file='rf.png')
    img = img.subsample(3, 3)
    bg = tk.Label(canvas, image=img)
    bg.place(relx=0, rely=0.1, relheight=1, relwidth=1)
    canvas.img = img
    text = tk.Label(top, text="PLEASE TAP YOUR CARD", font="helvetica 35 bold", foreground="BLUE")
    text.place(relx=0.15, rely=0.2)
    top.after(1000,rf)
    



def rcardy():
    top =tk.Toplevel()
    top.geometry("800x480")

root = tk.Tk()

root.geometry("800x480")
root.attributes("-fullscreen",True)
root.config(cursor = "none")
can = tk.Canvas(root,)
can.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame1 = tk.Frame(can,)
frame1.pack(side=tk.TOP)
photo1 = tk.PhotoImage(file="but.png")
photo1 = photo1.subsample(2, 2)
button1 = tk.Button(frame1, compound=tk.TOP, image=photo1,command=cashy,borderwidth=0,activebackground=None,activeforeground=None,bd=None,bg=None,fg=None
                    )
button1.pack(side=tk.LEFT)
button1.image = photo1

frame2 = tk.Frame(can)
frame2.pack(side=tk.TOP, fill=tk.X)
photo2 = tk.PhotoImage(file="but1.png")
photo2 = photo2.subsample(2, 2)
button2 = tk.Button(frame2, compound=tk.TOP, image=photo2,command=cardy,border="0")
button2.pack(side=tk.LEFT)
button2.image = photo2

frame3 = tk.Frame(can)
frame3.pack(side=tk.TOP, fill=tk.X)
photo3 = tk.PhotoImage(file="but2.png")
photo3 = photo3.subsample(2, 2)
button3 = tk.Button(frame3, compound=tk.TOP, image=photo3,command=rcardy,border="0",)
button3.pack(side=tk.LEFT)
button3.image = photo3


root.mainloop()
