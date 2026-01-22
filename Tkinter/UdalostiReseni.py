from tkinter import *

def klik(event):
    global pocet
    pocet += 1

    if pocet < 5:
        label.config(text=f"Říkal jsem NEMAČKEJ MĚ! ({pocet})")
    else:
        label.config(text="Tak dost!!! 😡")

def mezernik(event):
    label.config(text="Na mezerník taky nešahej!")

def klavesnice(event):
    label.config(text=f"Stiskl jsi klávesu: {event.keysym}")

root = Tk()
root.title("Rozčilovací tlačítko")

pocet = 0

label = Label(
    root,
    text="NEMAČKEJ MĚ",
    font=("Arial", 16),
    width=30,
    height=3,
    bg="lightgray"
)
label.pack(padx=20, pady=20)

label.bind("<Button-1>", klik)
root.bind("<space>", mezernik)
root.bind("<KeyPress>", klavesnice)

root.mainloop()
