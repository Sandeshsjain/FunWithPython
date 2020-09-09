from selenium import webdriver
from tkinter import *
import tkinter.ttk as ttk
import time
from tkinter.messagebox import showinfo

win = Tk()

win.title("Instagram login")
win.geometry("250x100")

def automation():
    username_automation = username.get()
    password_automation = passwd.get()
    if username_automation=="" or password_automation =="":
        showinfo("alert","please enter username and password")
    else:
        driver = webdriver.Chrome()
        driver.get("https://instagram.com")
        time.sleep(3)


        username1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        username1.send_keys(username_automation)
        time.sleep(3)

        password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(password_automation)
        time.sleep(3)

        login =  driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
        login.click()
        time.sleep(3)

        notification = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notification.click()

username_label = ttk.Label(win,text="Username",foreground = "Blue",font = ("",12))
username_label.grid(row = 0,column = 0)

username = ttk.Entry(win,width=20)
username.grid(row = 0,column = 1)

password_label = ttk.Label(win,text = "Password",foreground = "Blue",font = ("",12))
password_label.grid(row=1,column = 0)

passwd = ttk.Entry(win,width = 20)
passwd.grid(row=1,column =1,padx=15)

button = ttk.Button(win,text = 'Login',command = automation)
button.grid(row=2,column=0,columnspan = 2)

win.mainloop()