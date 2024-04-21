from tkinter import *
import webbrowser
root = Tk()
root.title("Universal Search")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)


def reset():
    search_entry.delete(first=0,last=100)

def google_search():
    search_value = search.get()
    search_value.replace(" ","+")
    webbrowser.open(f"www.google.com/search?q={search_value}")

def bing_search():
    search_value = search.get()
    search_value.replace(" ","+")
    webbrowser.open(f"www.bing.com/search?q={search_value}")


def yahoo_search():
    search_value = search.get()
    search_value.replace(" ","+")
    webbrowser.open(f"https://in.search.yahoo.com/search?p={search_value}")

def ask_search():
    search_value = search.get()
    search_value.replace(" ","+")
    webbrowser.open(f"https://www.search.ask.com/web?q={search_value}")

def duckduckgo():
    search_value = search.get()
    search_value.replace(" ","+")
    webbrowser.open(f"https://duckduckgo.com/?q={search_value}")

def allinone():
    search_value = search.get()
    search_value.replace(" ", "+")
    webbrowser.open(f"https://duckduckgo.com/?q={search_value}")
    webbrowser.open(f"https://www.search.ask.com/web?q={search_value}")
    webbrowser.open(f"www.google.com/search?q={search_value}")
    webbrowser.open(f"www.bing.com/search?q={search_value}")
    webbrowser.open(f"https://in.search.yahoo.com/search?p={search_value}")
    search_entry.delete(first=0, last=100)





search = StringVar()
search_entry = Entry(root,font="helvetica,10,bold",textvariable=search)
search_entry.pack(ipadx=130,ipady=5,pady=20)


reset_button  = Button(text="Clear Search",fg="green",bg="white",font="helvetica,10,bold",command=reset,padx=13).pack(padx=10,anchor="nw")
allinone_button  = Button(text="All in one Search",fg="white",bg="blue",font="helvetica,10,bold",command=allinone).pack(padx=10,anchor="nw")


search_label = Label(text="Search from any of these engines",bg="white",fg="blue",font="helvetica,15,bold").pack(fill=X,pady=10)


google_button  = Button(text="Google",fg="blue",bg="white",font="helvetica,10,bold",command=google_search,padx=5).pack(side=LEFT,anchor="n",pady=20,padx=2)
yahoo_button = Button(text="Yahoo Search",fg="white",bg="purple",font="helvetica,10,bold",command=yahoo_search).pack(side=LEFT,anchor="n",pady=20,padx=10)
bing_button = Button(text="Bing",fg="white",bg="green",font="helvetica,10,bold",padx=10,command=bing_search).pack(side=LEFT,anchor="n",pady=20,padx=10)
duckduckgo_button = Button(text="DuckDuck Go",fg="white",bg="orange",font="helvetica,10,bold",command=duckduckgo).pack(side=LEFT,anchor="n",padx=5,pady=20)
ask_button = Button(text="Ask.com",fg="white",bg="red",font="helvetica,10,bold",command=ask_search).pack(side=LEFT,anchor="n",pady=20,padx=10)




root.mainloop()
