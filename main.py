from tkinter import *
from tkinter import ttk

def sum():
    lbl_name['text']=int(first.get())+int(second.get())
def minus():
    lbl_name['text']=int(first.get())-int(second.get())
def mult():
    lbl_name['text']=int(first.get())*int(second.get())

root=Tk()
root.title('КАЛЬКУЛЯТОР')
root.geometry('512x512')
first, second = ttk.Entry(), ttk.Entry()
first.pack()
second.pack()
label_name = Button(text='+',command=sum)
label_name.pack()
label_name = Button(text='-',command=minus)
label_name.pack()
label_name = Button(text='*',command=mult)
label_name.pack()
lbl_name = Label(text='')
lbl_name.pack()
root.mainloop()
