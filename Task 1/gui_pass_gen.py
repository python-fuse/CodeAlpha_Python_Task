from tkinter import *
from tkinter import ttk
import string,random

letters = string.ascii_letters
symbols = '()!@#&,.%_+-'
digits = string.digits


characters = symbols + letters + digits

root = Tk()

root.title('Password Generator')
root.geometry('300x150')

password = StringVar()
length = IntVar()

def generate_password():
    password.set(random.sample(characters,length.get()))



pass_display = ttk.Entry(root,textvariable=password,font=('roboto medium',10),).pack(pady=5,ipadx=10)
pass_display = ttk.Label(root,text='Enter desired legnth').pack()
pass_display = ttk.Entry(root,textvariable=length,width=3, font=('Helvetica',10,'bold')).pack()
gen_button = ttk.Button(root,text='Generate',command=generate_password).pack(pady=10)
quit_button = ttk.Button(root,text='Exit',command=root.destroy).pack()


root.mainloop()