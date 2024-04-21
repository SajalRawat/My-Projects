import os
from tkinter import *
import tkinter.messagebox as tmsg
import time

a = time.asctime()
d = a[3:7]
b = a[20:24]
c = a[9:10]
val = (f"{d}{c}{b}")
init_val = val.replace(" ", "")
date_value = init_val

root = Tk()

root.geometry("750x300")
root.maxsize(750, 300)
root.minsize(750, 300)
root.title("Form")


def entries_show():
    try:
        sh_read = open(f"{date_value}N.txt", 'r')
        sh_val = sh_read.read()
        sh_read.close()
        ask_val = tmsg.askquestion("Today's Entries",
                                   f"Today {sh_val} entries have been entered.Would you want to access them?")
        if ask_val == "yes":
            os.system(f"{date_value}.txt")
        else:
            print("Code Executed")


    except:
        tmsg.showinfo("Info", "No entries yet")


def function():
    a = NE.get()
    b1 = AE.get()
    c2 = PE.get()
    d3 = EE.get()
    try:
        check = int(c2)
        f = open(f"{date_value}.txt", "a")
        f.write("\n")
        f.write("\n")
        f.write("Name:")
        f.write(a)
        f.write("\n")
        f.write("Address:")
        f.write(b1)
        f.write("\n")
        f.write("PhoneNumber:")
        f.write(c2)
        f.write("\n")
        f.write("Email ID:")
        f.write(d3)
        f.close()
        N.delete(first=0, last=100)
        A.delete(first=0, last=100)
        P.delete(first=0, last=100)
        E.delete(first=0, last=100)
        try:
            fn = open(f"{date_value}N.txt", "r")
            fn_value = fn.read()
            fn.close()
            fn_write = open(f"{date_value}N.txt", "w")
            fn_value_main = int(fn_value)
            fn_value_init = fn_value_main + 1
            fn_write.write(f"{fn_value_init}")
            fn_write.close()
        except Exception as e:
            fn_try = open(f"{date_value}N.txt", "a")
            fn_try.write('1')
            fn_try.close()


    except Exception as error:
        tmsg.showerror("Error", "You have entered wrong entry in PhoneNo Column")
        P.delete(first=0, last=100)


J = Label(root, text="Fields", bg="blue", fg="white", font="helvetica,30,bold", padx=190, pady=10)
J.grid(row=0, column=1)
K = Label(root, text="Entries", bg="blue", fg="white", font="helvetica,30,bold", padx=150, pady=10)
K.grid(row=0, column=2)

NL = Label(root, text="Name", font="helvetica,15,bold", pady=10)
NL.grid(row=2, column=1)
AL = Label(root, text="Address", font="helvetica,15,bold", pady=10)
AL.grid(row=4, column=1)
PL = Label(root, text="Phone Number", font="helvetica,15,bold", pady=10)
PL.grid(row=6, column=1)
EL = Label(root, text="EmailID", font="helvetica,15,bold", pady=10)
EL.grid(row=8, column=1)

NE = StringVar()
AE = StringVar()
PE = StringVar()
EE = StringVar()

N = Entry(root, textvariable=NE)
A = Entry(root, textvariable=AE)
P = Entry(root, textvariable=PE)
E = Entry(root, textvariable=EE)

N.grid(row=2, column=2)
A.grid(row=4, column=2)
P.grid(row=6, column=2)
E.grid(row=8, column=2)

B1 = Button(root, text="Submit", bg="Green", fg="white", pady=10, padx=10, command=function, font="helvetica,15,bold")
B1.grid(row=10, column=2, pady=30)

B2 = Button(text="Today's Entries", font="helvetica,15,bold", pady=9, bg="red", fg="white", command=entries_show)
B2.grid(row=10, column=1)

root.mainloop()

