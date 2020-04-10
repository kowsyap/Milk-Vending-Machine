import Tkinter as tk
import CASH

root = tk.Tk()
root.geometry("800x480")
root.attributes("-fullscreen",True)
#root.config(cursor = "none")
can = tk.Canvas(root,)
can.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame1 = tk.Frame(can,)
frame1.pack(side=tk.TOP)
photo1 = tk.PhotoImage(file="but.png")
photo1 = photo1.subsample(2, 2)
button1 = tk.Button(frame1, compound=tk.TOP, image=photo1,command=CASH.app,borderwidth=0,activebackground=None,activeforeground=None,bd=None,bg=None,fg=None
                    )
button1.pack(side=tk.LEFT)
button1.image = photo1

frame2 = tk.Frame(can)
frame2.pack(side=tk.TOP, fill=tk.X)
photo2 = tk.PhotoImage(file="but1.png")
photo2 = photo2.subsample(2, 2)
button2 = tk.Button(frame2, compound=tk.TOP, image=photo2,command=tk.NONE,border="0")
button2.pack(side=tk.LEFT)
button2.image = photo2

frame3 = tk.Frame(can)
frame3.pack(side=tk.TOP, fill=tk.X)
photo3 = tk.PhotoImage(file="but2.png")
photo3 = photo3.subsample(2, 2)
button3 = tk.Button(frame3, compound=tk.TOP, image=photo3,command=tk.NONE,border="0",)
button3.pack(side=tk.LEFT)
button3.image = photo3


root.mainloop()
