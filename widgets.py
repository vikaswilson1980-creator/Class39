from tkinter import *
from datetime import date
root = Tk()
root.title('Demo window')
root.geometry('400x300')
lbl = Label(text = "Hey there",fg = "white",bg = "#072F5F",height = 1,width = 300)
namelbl = Label(text = "Full name",bg = "#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "Welcome to the Application \n Today's date is : "
    greet = "Hello "+ name + "\n"
    textbox.insert(END,greet)
    textbox.insert(END,message)
    textbox.insert(END,date.today())
textbox = Text(height=3)
btn = Button(text= "Begin",command = display,height = 1,bg = "#1261A0",fg = "White")
lbl.pack()
namelbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()
root.mainloop()


