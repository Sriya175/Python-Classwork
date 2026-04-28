from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():

    messagebox.showinfo("Information", "My name is Sriya")

button = Button(root, text= "Info", command=msg)
button.place(x=40, y=80)

def msg2():

    messagebox.showerror("Error", "There was a error")

button2 = Button(root, text= "Error", command=msg2)
button2.place(x=150, y=80)

def msg3():

    messagebox.askquestion("Question", "Are you having fun?")

button3 = Button(root, text= "Question", command=msg3)
button3.place(x=40, y=120)

def msg4():

    messagebox.askokcancel("Cancel", "Are you having fun?")

button4 = Button(root, text= "Cancel", command=msg4)
button4.place(x=150, y=120)

def msg5():

    messagebox.askyesno("Yes", "Are you having fun?")

button5 = Button(root, text= "Yes", command=msg5)
button5.place(x=40, y=160)

def msg6():

    messagebox.askretrycancel("retry", "Are you having fun?")

button6 = Button(root, text= "retry", command=msg6)
button6.place(x=150, y=160)


root.mainloop()
