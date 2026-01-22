# https://tkinter.py.cz/tkinter_events_binds.html
from tkinter import *

okno = Tk()
def levy_klik(event):
    print("Single Click, Button-l") 
def stop(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

tlacitko = Button(okno, text='Mouse Clicks')
tlacitko.pack()
tlacitko.bind('<Button-1>', levy_klik)
tlacitko.bind('<Double-1>', stop) 
okno.mainloop()