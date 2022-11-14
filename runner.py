import os
from tkinter import *

root = Tk()

root.geometry('800x600')
root.title('login')

password = Entry(root)
password.pack()


def login():
    global password
    if password.get() == '12345':
        os.system('python Admin.py')
    else:
        lab = Label(root, text = 'Wrong password !').pack()



login_bt = Button(root , text = 'Login', command= login).pack()


root.mainloop()