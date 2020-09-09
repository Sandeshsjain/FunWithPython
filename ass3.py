import tkinter
from tkinter import messagebox,simpledialog
import sys
def finish():
    a = messagebox.askyesno("QUItting","are you sure you want to quite")
    if a == True:
        name = simpledialog.askstring("input","what is your name")
        if name is None or "":
            messagebox.showinfo("thankuu","have a good day userjee")
        messagebox.showinfo("thankuu",f"have a good day {name}")
        sys.exit(0)
def del1():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    e1.focus()


def divfun():
    try:
        e3.delete(0,'end')
        a = int(e1.get())
        b = int(e2.get())
        c = a/b
        s.set(c)
    except ValueError:
        messagebox.showerror("invalid number","please pass digit only")
    except ZeroDivisionError:
        messagebox.showerror("invalid number","please pass non zero number")

root = tkinter.Tk()
root.geometry('400x200+100+200')
root.title("this is ass1")
lbl1 = tkinter.Label(root,text = "NUMBER DIVISION PROGRAM",font=("arial" , 18, "bold"))
lbl1.grid(row = 0,column = 0,columnspan = 3)
lbl2 = tkinter.Label(root,text = "first no:")
lbl3 = tkinter.Label(root,text = "second no:")
lbl4 = tkinter.Label(root,text = "result")
e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root)
s = tkinter.StringVar()
e3 = tkinter.Entry(root,textvariable = s,fg = "green")
b1 = tkinter.Button(root,text="divide",command = divfun)
b2 = tkinter.Button(root,text="Clear",command = del1)
b3 = tkinter.Button(root,text="Quit",command = finish)
lbl2.grid(row=1,column= 0,sticky=tkinter.E)
lbl3.grid(row = 2,column = 0,sticky = tkinter.E)
lbl4.grid(row = 3,column = 0,sticky = tkinter.E)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady = 5,padx = 5,sticky=tkinter.W+tkinter.E)
b2.grid(row=4,column=1,pady = 5,padx = 5,sticky=tkinter.W+tkinter.E)
b3.grid(row=4,column=2,pady = 5,padx=5,sticky=tkinter.W+tkinter.E)
root.mainloop()
