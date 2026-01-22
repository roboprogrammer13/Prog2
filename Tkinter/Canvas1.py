from tkinter import *

master = Tk()
w = Canvas(master, width=200, height=200)
w.pack()

canvas_height = 200
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y) # vodorovná čára uprostřed plátna
w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_text(canvas_width / 2,
              canvas_height / 4,
              text="Python")
mainloop()