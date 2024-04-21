from tkinter import *
import os
import tkinter.messagebox as tmsg
from time import strftime


root = Tk()

root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.title("PassProtect")


title = Label(text="Pass Protect",font="helvetica,15,bold",bg="lightblue",fg="black")
title.pack(fill=X)


def new_uid_creation():
    create_root = Tk()
    create_root.geometry("300x100")
    create_root.minsize(400,100)
    create_root.maxsize(400,100)
    create_root.title("UID Creation Window")
    root.config(bg="light yellow")

    def creation_func():
        tmsg.showwarning("Caution","You will get a 12 digit UID number. Please remember it to access your UID File.")
        d_rem = strftime("%D")
        col_rem = d_rem.replace("/", "")
        init_time = strftime("%H%M%S")
        new_UID = f"{init_time}{col_rem}"
        f =open(f"{new_UID}.lock","w")
        f.close()
        tmsg.showwarning("Info","Your New UID has been made succesfully,In next window your are goint to get that UID.please dont lose it")
        tmsg.showinfo("UID",f"Your new UID is : {new_UID} ,Please don't lose it")
        tmsg.showwarning("File Info","Your file is Locked, Please unlock it when needed")
        exit()

    text_label = Label(create_root,text="Click on the button below and you wil get your new UID File",font="helvetica 10")
    text_label.pack()

    new_uid_button = Button(create_root,text="Create UID",bg="blue",fg="white",font="helvetica 12",command=creation_func)
    new_uid_button.pack(pady=8)



    create_root.mainloop()

def status_check():
    tmsg.showwarning("Caution","Your UID should be correct else you may get wrong status of the file.")
    uid_for_status = user_uid.get()
    try:
        f = open(f"{uid_for_status}.lock","r")
        f.close()
        tmsg.showinfo("UID Status",f"{uid_for_status} : Locked")

    except:
        tmsg.showinfo("UID Status",f"{uid_for_status} : UnLocked (Must lock It)")

    uid_entry.delete(first=0,last=1000)




def unlock():
    tmsg.showinfo("Caution", "After writing must close and save the file otherwise it may get corrupt or software may not work")
    tmsg.showwarning("Caution","Must Lock Your File after use")
    try:
        uid =user_uid.get()
        os.rename(f"{uid}.lock",f"{uid}.txt")
        tmsg.showinfo("Unlocked Successfully",f" Your file assigned to {uid} is successfully unlocked")
        os.system(f"{uid}.txt")
        uid_entry.delete(first=0, last=1000)

    except Exception as error:
        tmsg.showerror("Error","UID not available. You may need to make new UID or File is already unlocked")
        uid_entry.delete(first=0, last=1000)




def lock():
    try:
        uid =user_uid.get()
        os.rename(f"{uid}.txt",f"{uid}.lock")
        tmsg.showinfo("Locked Succesfully",f" Your file assigned to {uid} is succesfully Locked")
        uid_entry.delete(first=0, last=1000)

    except Exception as error:
        tmsg.showerror("Error","You may need to make new UID or File is already Locked or File is open in background first lose it and then retry")
        uid_entry.delete(first=0, last=1000)




user_uid = StringVar()

uid_label = Label(text="Enter your UID number",font="helvetica,15,bold")
uid_label.pack(pady=10)

uid_entry = Entry(font="helvetica,15,bold",textvariable=user_uid)
uid_entry.pack(pady=5)
unlock_button = Button(text="UnLock",font="helvetica,15,bold",command=unlock,padx=4,bg="green",fg="white")
lock_button =  Button(text="Lock",font="helvetica,15,bold",padx=14,command=lock,bg="red",fg="white")
newregister_button =  Button(text="New UID",font="helvetica,15,bold",bg="blue",fg="white",command=new_uid_creation)
status_button = Button(text="Check Status",font="helvetica,15,bold",command=status_check,padx=4,bg="purple",fg="white")
unlock_button.pack(pady=10)
lock_button.pack(pady=10)
newregister_button.pack(pady=10)
status_button.pack(pady=10)



root.mainloop()

