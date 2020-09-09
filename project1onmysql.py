from tkinter import *
from tkinter  import messagebox as mbox
import pymysql
root = Tk()
root.geometry("300x300")
root.title("my window")

def insert():
    name = e_name.get()
    mob = e_mob.get()
    roll = e_roll.get()
    if name=='' or mob =='' or roll=='':
        mbox.showinfo("insert status","all field are required")
    else:
        db = pymysql.connect(host='localhost',user='root',passwd='Sandesh@123',database='sandesh')
        cd = db.cursor()
        cd.execute("insert into student2 values('" +name+ "','" +mob+ "','"+ roll+ "')")
        db.commit()
        mbox.showinfo("insert status","insertion successful")
        e_roll.delete(0,'end')
        e_name.delete(0,'end')
        e_mob.delete(0, 'end')
        db.close()
def delete():
    if e_roll.get()=='':
        mbox.showinfo("delete status","roll number field is required")
    else:
        db = pymysql.connect(host='localhost',user='root',passwd='Sandesh@123',database='sandesh')
        cd = db.cursor()
        cd.execute("delete from student2 where stdrlno = '" + e_roll.get() +"' ")
        db.commit()
        mbox.showinfo("delete status","deletion successful")
        e_roll.delete(0,'end')
        e_name.delete(0,'end')
        e_mob.delete(0, 'end')
        db.close()




name = Label(root,text="enter name",font=('bold',10))
name.place(x=20,y=30)

mob = Label(root,text="enter mob no",font=('bold',10))
mob.place(x=20,y=60)

roll = Label(root,text="enter roll",font=('bold',10))
roll.place(x=20,y=90)


e_name = Entry()
e_name.place(x = 150,y=30)

e_mob = Entry()
e_mob.place(x = 150,y=60)

e_roll = Entry()
e_roll.place(x = 150,y=90)

insert = Button(root,text='Insert',font=("italic",10),bg = "white",command=insert)
insert.place(x = 20 ,y=120)

delete = Button(root,text='Delete',font=("italic",10),bg = "white",command=delete)
delete.place(x = 120 ,y=120)


root.mainloop()