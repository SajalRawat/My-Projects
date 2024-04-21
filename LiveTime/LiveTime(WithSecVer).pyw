from tkinter import *
from time import strftime

def auto_time():
    string  = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, auto_time )


root = Tk()
root.title("Live Time")
root.configure(bg="black")
root.attributes("-fullscreen",True)


time_label = Label(font = "ds-digital 155 bold",bg="black",fg="white",pady=255)
time_label.pack()

auto_time()
root.mainloop()
