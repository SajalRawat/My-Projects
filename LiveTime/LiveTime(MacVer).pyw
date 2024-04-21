from tkinter import *
from time import strftime

def auto_time():
    string  = strftime('%H:%M')
    p_time = strftime('%p')
    time_label.config(text=string)
    p_label.config(text=p_time)
    time_label.after(1000, auto_time )


root = Tk()
root.title("Live Time")
root.configure(bg="black")
root.attributes("-fullscreen",True)

p_label  = Label(font = "consolas 60 bold",bg="black",fg="white",padx=50)
p_label.pack(side=RIGHT,anchor='n',pady=140)
time_label = Label(font = "ds-digital 350 bold",bg="black",fg="white",pady=255)
time_label.pack()

auto_time()
root.mainloop()
