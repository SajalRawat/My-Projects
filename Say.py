from tkinter import *
import os
root = Tk()
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)

root.title ("Say")

def tempbindevent(event):
    a= sd.get()
    g = open(( "temp.vbs"), 'w')
    g.write("Dim speaks, speech")
    g.write("\n")
    g.write("speaks =" )
    g.write('''"''')
    g.write(a)
    g.write('''"''')
    g.write("\n")
    g.write('''Set speech=CreateObject("sapi.spvoice")''')
    g.write("\n")
    g.write("speech.Speak speaks")
    g.close()
    cd = "temp.vbs"
    os.system(cd)
    os.remove(cd)
    E.delete(first=0,last=1000)

def temp():
    a= sd.get()
    g = open(( "temp.vbs"), 'w')
    g.write("Dim speaks, speech")
    g.write("\n")
    g.write("speaks =" )
    g.write('''"''')
    g.write(a)
    g.write('''"''')
    g.write("\n")
    g.write('''Set speech=CreateObject("sapi.spvoice")''')
    g.write("\n")
    g.write("speech.Speak speaks")
    g.close()
    cd = "temp.vbs"
    os.system(cd)
    os.remove(cd)
    E.delete(first=0,last=1000)

root.bind('<Return>',tempbindevent)
    

    

    



     







sd = StringVar()



F =Frame(root)

F.pack(side=BOTTOM,fill=X)



E = Entry(F,textvariable= sd,font="helvetica,10,bold")

E.pack(fill=X,ipady=2) 



B= Button(root,text="Say",fg="white",bg="blue", font="helvetica,12,bold",padx=10,command=temp)

B.pack(anchor=SE,side=BOTTOM)



root.mainloop()

