from tkinter import *

master = Tk()

var1 = IntVar()
var2 = IntVar()


def vypis():
    print("muž:", var1.get())
    print("žena:", var2.get())

    if var1.get() == 1:
        stitek.config(text="Vybrali jste: muž")
    elif var2.get() == 1:
        stitek.config(text="Vybrali jste: žena")
    else:
        stitek.config(text="Nic není vybráno")

Checkbutton(master, text='muž', variable=var1, command=vypis).grid(row=0, sticky=W)
Checkbutton(master, text='žena', variable=var2, command=vypis).grid(row=1, sticky=W)

Button(master, text='Zobrazit výběr', command=vypis).grid(row=2, sticky=W, pady=4)

stitek = Label(master, text="")
stitek.grid(row=3, sticky=W) 

mainloop()
