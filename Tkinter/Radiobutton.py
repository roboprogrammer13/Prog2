from tkinter import *

master = Tk()

volba = IntVar()  # jedna proměnná pro radiobuttony

stitek = Label(master, text="")
stitek.grid(row=3, sticky=W)

def vypis():
    print("volba:", volba.get())

    if volba.get() == 1:
        stitek.config(text="Vybrali jste: muž")
    elif volba.get() == 2:
        stitek.config(text="Vybrali jste: žena")
    else:
        stitek.config(text="Nic není vybráno")

Radiobutton(master, text='muž', variable=volba, value=1, command=vypis).grid(row=0, sticky=W)
Radiobutton(master, text='žena', variable=volba, value=2, command=vypis).grid(row=1, sticky=W)

Button(master, text='Zobrazit výběr', command=vypis).grid(row=2, sticky=W, pady=4)

mainloop()
