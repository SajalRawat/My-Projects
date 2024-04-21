from tkinter import *
import webbrowser
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)
root.title("SmartDict")

def search_func():
    Init_Value =Radio_Var.get()
    Search_Value = main_entry.get()
    if Init_Value == "0":
        tmsg.showerror("Error","You didn't selected any language")
    else:
        Search_Sen = f"What is the meaning of {Search_Value} in {Init_Value}"
        Search_Sen.replace(" ","+")
        webbrowser.open(f"www.google.com/search?q={Search_Sen}")
        main_entry.delete(first=0,last=1000)




main_title_label = Label(text="SmartDict-poweredbygoogle",font="helvetica 14 ",bg="cyan",padx=25)
main_title_label.pack()

main_entry = Entry(font="helvetica 12")
main_entry.pack(pady=20)

Lang_label = Label(text="You want meaning in which Language",font="helvetica 12")
Lang_label.pack()

Radio_Var = StringVar()
Radio_Var.set("0")

Radio = Radiobutton(text="   Hindi",value="Hindi",font="helvetica 8",variable=Radio_Var)
Radio.pack(anchor="center",pady=5)
Radio = Radiobutton(text="English",value="English",font="helvetica 8",variable=Radio_Var)
Radio.pack(anchor="center")

search_button = Button(text="Search Meaning",font="helvetica 12 bold",bg="Cyan",command = search_func)
search_button.pack(pady=10)

root.mainloop()