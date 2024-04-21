from tkinter import *
import random
root =Tk()
root.geometry("350x350")
root.minsize(350,350)
root.maxsize(350,350)
root.title("Dice")

def main_function():
    a = random.randint(1,6)
    if a==6:
        b=6
    if a==1:
        b=1
    if a==2:
        b=2
    if a==3:
        b=3
    if a==4:
        b=4
    if a==5:
        b=5

    main_button['state'] = DISABLED
    number_label = Label(text=f"Dice has given the number {b}",font="helvetica,30,bold")
    number_label.pack(pady=10)

    def RESET():
        number_label.destroy()
        main_button['state'] = NORMAL
        Clear_button.destroy()



    Clear_button = Button(text="Clear",font="helvetica,12,bold",command=RESET,bg="red",fg="white")
    Clear_button.pack()

main_button = Button(text="RollTheDice",font="helvetica,15,bold",bg="blue",fg="white",command=main_function)
main_button.pack(pady=80)

root.mainloop()
