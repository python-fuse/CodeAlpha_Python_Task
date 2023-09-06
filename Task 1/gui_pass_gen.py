from tkinter import *
from password_generator import characters
import random

root = Tk()

root.title('Password Generator')
root.geometry('300x200')

password = StringVar()

def generate_password():
    password.set(random.sample(characters,12))





pass_display = Entry(root,textvariable=password,font=('Helvetica',10,'bold'),justify=CENTER).pack(pady=10,ipadx=4)
gen_button = Button(root,text='Generate',command=generate_password).pack(pady=20)
quit_button = Button(root,text='Exit',command=root.destroy,bg='red').pack()


root.mainloop()