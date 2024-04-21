from tkinter import *
from time import strftime

def auto_time():
    string  = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, auto_time )


root = Tk()
root.title("Live Time")

time_label = Label(font = "ds-digital,80",bg="black",fg="cyan")
time_label.pack()

auto_time()
mainloop()