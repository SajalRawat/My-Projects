from tkinter import *
from time import strftime


def auto_time():
    string  = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, auto_time )


root = Tk()
root.title("Live Time")
root.geometry("700x110")
root.minsize(700,110)
root.maxsize(700,110)

time_label = Label(font = ('Century Gothic',80,'bold'),bg="black",fg="cyan",pady=50,padx=50)
time_label.pack()

auto_time()
mainloop()