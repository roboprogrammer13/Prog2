# Hra na přiřazení názvů barev k jejich zobrazení, řádek 21 zobrazí v prvním sloupci název barvy,
# ve druhém sloupci je vstupní pole pozadí barvy (náhodně zamíchané) a ve třetím sloupci je výsledek kontroly správnosti odpovědi.
from tkinter import *
from random import sample

colours = ['red','green','orange','white','yellow','blue']
coloursshuffled = sample(colours, len(colours))

entries = []
vysledky = []

def zkontroluj():
    for i in range(len(colours)):
        odpoved = entries[i].get().lower()
        if odpoved == coloursshuffled[i]:
            vysledky[i].config(bg="green")
        else:
            vysledky[i].config(bg="red")

for r in range(len(colours)):
    Label(text=colours[r], relief=RIDGE, width=10).grid(row=r, column=0)# Název barvy

    e = Entry(bg=coloursshuffled[r], relief=SUNKEN, width=10)# Vybarvené vstupní pole
    e.grid(row=r, column=1)
    entries.append(e)

    v = Label(width=3,relief="ridge")# Prázdné pole pro výsledek
    v.grid(row=r, column=2)# Výsledek v posledním sloupci
    vysledky.append(v)

Button(text="Zkontroluj", command=zkontroluj).grid(row=len(colours), columnspan=3)

mainloop()
