from tkinter import *
import os
import tkinter.messagebox as tmsg
import Date
root =Tk()
root.title("MPM-MyPersonalManager")
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)
head_label = Label(text="MPM-MyPersonalManager",bg="blue",fg="white",font="helvetica,15,bold",pady=5)
head_label.pack(fill="x")

def main_function():
    CP = CP_entry.get()
    NAME = NAME_entry.get()
    NO = NO_entry.get()
    time = Date.findtime()
    try:
        NO_main = int(NO)
        try:
            CP_main = int(CP)
            if NO_main>0:
                Price = NO_main*CP_main
                w = open(f"{time}.txt","a")
                w.write(f"You bought {NO} {NAME} which cost {Price} rupees\n")
                w.close()
                NO_entry.delete(first=0,last=1000)
                NAME_entry.delete(first=0,last=1000)
                CP_entry.delete(first=0,last=1000)
            if NO_main<=0:
                tmsg.showerror("Error","Quantity of item cannot be 0")
                NO_entry.delete(first=0, last=1000)
                NAME_entry.delete(first=0, last=1000)
                CP_entry.delete(first=0, last=1000)
        except:
            tmsg.showerror("Error","You have entered the price of item in Alphabet")
            NO_entry.delete(first=0,last=1000)
            NAME_entry.delete(first=0,last=1000)
            CP_entry.delete(first=0,last=1000)



    except Exception as error:
        tmsg.showerror("Error","You have enter the Quantity of item in Alphabet")
        NO_entry.delete(first=0, last=1000)
        NAME_entry.delete(first=0, last=1000)
        CP_entry.delete(first=0, last=1000)


def view_data():
    tmsg.showinfo("Data","You will find the all your expenses data in txt file named as their respective date in the program directory ")

NO_value = StringVar(root,value=1)


NAME_label = Label(text="Enter The name of item",font="helvetica,13,bold")
NAME_label.pack(pady=10)
NAME_entry = Entry(root)
NAME_entry.pack()

CP_label = Label(text="Enter The cost Price of the item", font="helvetica,13,bold")
CP_label.pack(pady=10)
CP_entry = Entry(root)
CP_entry.pack()

NO_label = Label(text="Enter the number of item",font="helvetica,13,bold")
NO_label.pack(pady=10)
NO_entry = Entry(root,textvariable=NO_value)
NO_entry.pack()

ADD_button = Button(text="Add Data",font ="helvetica,13,bold",bg="blue",fg="white",command = main_function)
ADD_button.pack(pady=20)
VIEW_button = Button(text="View Data",font= "helvetica,13,bold",bg="green",fg="white",command=view_data)
VIEW_button.pack()
root.mainloop()
