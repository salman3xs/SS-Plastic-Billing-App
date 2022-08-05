from tkinter import *
import tkinter as tk
from tkinter import ttk

def sel_row(event):
    global s
    i = list1.curselection()[0]
    s = list1.get(i)

w = Tk()

w.wm_title('BILL')

l1 = Label(w, text='Customer Name')
l1.grid(row=0, column=0)

customer_name = StringVar()
e1 = Entry(w, text=customer_name, width=30)
e1.grid(row=0, column=1)

l2 = Label(w, text='Address')
l2.grid(row=1, column=0)

address = StringVar()
e2 = Entry(w, text=address, width=30)
e2.grid(row=1, column=1)

l3 = Label(w, text='Mob')
l3.grid(row=2, column=0)

mob = StringVar()
e3 = Entry(w, text=mob, width=30)
e3.grid(row=2, column=1)

l4 = Label(w, text='sr no')
l4.grid(row=3, column=0)

srno = StringVar()
e4 = Entry(w, text=srno, width=30)
e4.grid(row=3, column=1)

w.mainloop()
