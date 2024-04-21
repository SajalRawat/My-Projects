from tkinter import *
import tkinter.messagebox as tmsg
import os
import shutil
root = Tk()
root.geometry('300x300')
root.minsize(300,200)
root.maxsize(300,200)
root.title("GreetUP")


os.system("startup_location_service.bat")
f = open("startup_temp_.txt",'r')
startup_temp = f.read()
f.close()
f = open("current_location_.txt","r")
current_location = f.read()
f.close()
startup_temp_ = startup_temp.replace("\n","")
current_location_ = current_location.replace("\n","")
print(current_location_)
print(startup_temp_)

def preview_func():
    a = add_entry.get()
    g = open(("GreetUP.vbs"), 'w')
    g.write("Dim speaks, speech")
    g.write("\n")
    g.write("speaks =")
    g.write('''"''')
    g.write(a)
    g.write('''"''')
    g.write("\n")
    g.write('''Set speech=CreateObject("sapi.spvoice")''')
    g.write("\n")
    g.write("speech.Speak speaks")
    g.close()
    os.system("GreetUP.vbs")
    os.remove("GreetUP.vbs")
    ask_preview = tmsg.askquestion("Confirmation", "Would you Like to add this as your PC's greeting?")
    if ask_preview == "yes":
        g = open(("startup_temp_greet_.vbs"), 'w')
        g.write("Dim speaks, speech")
        g.write("\n")
        g.write("speaks =")
        g.write('''"''')
        g.write(a)
        g.write('''"''')
        g.write("\n")
        g.write('''Set speech=CreateObject("sapi.spvoice")''')
        g.write("\n")
        g.write("speech.Speak speaks")
        g.close()
        add_entry.delete(first=0,last=100)
        shutil.move(f"{current_location_}",f"{startup_temp_}")


    if ask_preview == "no":
        add_entry.delete(first=0,last=100)



def remove_func():
    try:
        os.remove(f"{startup_temp_}")
        tmsg.showinfo("Successfully Removed","We successfully removed previous greet")
    except:
        tmsg.showerror("No greeting found","It seems that there was no previously added greet in your pc")





add_entry = Entry(font="helvetica 12 bold")
add_entry.pack(pady=7)
add_button = Button(text="Preview and Add",font="helvetica 13 ",bg="blue",fg="white",command=preview_func)
remove_button = Button(text="Remove any Greetings",font="helvetica 13 ",bg="red",fg="white",command=remove_func)
add_button.pack()
remove_button.pack()


root.mainloop()
