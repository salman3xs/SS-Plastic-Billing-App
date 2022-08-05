from tkinter import *
import tkinter as tk
from tkinter import ttk
from fpdf import FPDF
import num2words

def sel_row(event):
    global s
    i = list1.curselection()[0]
    s = list1.get(i)


def ad():
    e10.delete(0, END)
    list = []
    list.append(material.get())
    list.append(hsn.get())
    list.append(quantity.get())
    list.append(rate.get())
    t = int(list[2])*float(list[3])
    list.append(t)
    e10.insert(END, list[4])
    list1.insert(END, list[0]+str('       ')+list[1]+str('    ')+list[2]+str('     ')+list[3]+str('    ')+str(list[4]))
    totallist.append(list)


def tot():
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e15.delete(0, END)
    x = 0
    for i in totallist:
        x = x+int(i[4])
    e11.insert(END, x)
    e12.insert(END, int(float(x*9/100)))
    e13.insert(END, int(float(x*9/100)))
    e15.insert(END, int(float(2*x*9/100+x)))


def prnt():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(100, 10, txt='S S PLASTIC',
             ln=1, align='C')
    pdf.cell(300, txt='Sales Invoice',
             ln=1, align='C')
    pdf.cell(100, 10, txt='H/G-31/4A/5/211 - Mehrun,Jalgaon-425001',
                 ln=2, align='C')
    pdf.cell(250, txt='Date: '+date.get(),
                 ln=2, align='C')
    pdf.cell(100, 10, txt='Email : ssplastic.sk7@gmail.com',
                ln=3, align='C')
    pdf.cell(250, txt='Invoice No. '+invoice.get(),
                 ln=1, align='C')
    pdf.cell(100, 10, txt='Mobile : 9975433377/ 9226897384/ 9730622956',
                ln=4, align='C')
    pdf.cell(100, 10, txt='GSTIN NO : 27EXAPS8247G1Z1',
                ln=5, align='C')
    pdf.cell(100, 10, txt='State : MAHARSHTRA    State Code :27',
                ln=6, align='C')
    pdf.cell(80, 10, txt='Mr. '+name.get(),
                 ln=1, align='C')
    pdf.cell(90, 10, txt='Address: '+add.get(),
                 ln=1, align='C')
    pdf.cell(80, 10, txt='GSTIN NO:'+gst.get(),
                 ln=1, align='C')
    pdf.cell(50, 10, txt='              State:Maharashtra                     State Code:27',
                 ln=1)
    pdf.cell(50, 10, txt='      Sr No    Particulars                                                            HSN         Quantity      Rate Per Pcs                    Amount  ',
                 ln=1)
    y = 120
    z = 1
    for j in totallist:
        pdf.set_xy(15, y)
        pdf.cell(50, 10,txt=str(z)+'                         '+str(j[0]),
                 ln=1)
        z += 1
        pdf.set_xy(90, y)
        pdf.cell(50, 10,txt='                 '+str(j[1])+'                    '+str(j[2])+'             '+str(j[3])+'                     '+str(j[4]),
                 ln=1)
        y += 10
    pdf.set_xy(10,190)
    pdf.cell(50, 10, txt='DECLARATION:',
                 ln=23, align='C')
    pdf.set_xy(20,200)
    pdf.cell(60, 10, txt='I/we declare that this invoice shows the actual price of the goods described and that all',
                 ln=2)
    pdf.set_xy(15,210)
    pdf.cell(50, 10, txt='particulars are true and correct.',
                 ln=1)
    pdf.set_xy(10,220)
    pdf.cell(50, 10, txt='Rs in words :',
                 ln=1, align='C')
    pdf.set_xy(30,230)
    # pdf.cell(50, 10, txt=str(num2words(int(float(gtotal.get()))))+'Rs Only',
    #              ln=1, align='C')
    pdf.set_xy(125, 215)
    pdf.cell(50, 10, txt='Total',
                 ln=1, align='C')
    pdf.set_xy(155, 215)
    pdf.cell(50, 10, txt=total.get(),
                 ln=1, align='C')
    pdf.set_xy(125, 225)
    pdf.cell(50, 10, txt='CGST 9%',
                 ln=1, align='C')
    pdf.set_xy(155, 225)
    pdf.cell(50, 10, txt=cgst.get(),
                 ln=1, align='C')
    pdf.set_xy(125, 235)
    pdf.cell(50, 10, txt='SGST 9%',
                 ln=1, align='C')
    pdf.set_xy(155, 235)
    pdf.cell(50, 10, txt=sgst.get(),
                 ln=1, align='C')
    pdf.set_xy(125, 245)
    pdf.cell(50, 10, txt='Round Off',
                 ln=1, align='C')
    pdf.set_xy(155, 245)
    pdf.cell(50, 10, txt=roundoff.get(),
                 ln=1, align='C')
    pdf.set_xy(125, 255)
    pdf.cell(50, 10, txt='G. Total',
                 ln=1, align='C')
    pdf.set_xy(155, 255)
    pdf.cell(50, 10, txt=gtotal.get(),
                 ln=1, align='C')
    pdf.set_xy(145, 265)
    pdf.cell(50, 10, txt='For S S Plastic Authorized Signature',
                 ln=1, align='C')
    pdf.set_xy(10, 255)
    pdf.cell(50, 10, txt="Receiver's Sign.",
                 ln=1, align='C')
    pdf.set_xy(140,50)
    pdf.cell(50, 10, txt='Original For Recipiant',
                 ln=23, align='C')
    pdf.set_xy(140,60)
    pdf.cell(50, 10, txt='Duplicate for Transporter',
                 ln=23, align='C')
    pdf.set_xy(140,70)
    pdf.cell(50, 10, txt='Triplicate for Supplier',
                 ln=23, align='C')
    pdf.set_xy(95,80)
    pdf.cell(50, 10, txt='D.C. NO.',
                 ln=23, align='C')
    pdf.set_xy(110,90)
    pdf.cell(50, 10, txt='Mode of Delivery:BY Hand',
                 ln=23, align='C')
    pdf.set_xy(100,100)
    pdf.cell(50, 10, txt='Vehicle NO.',
                 ln=23, align='C')
    pdf.line(10, 10, 10, 10)
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10,10,200,10)#vertical                           MARGIN
    pdf.line(10,290,10,10)#horizontal
    pdf.line(10,290,200,290)
    pdf.line(200,10,200,290)
    pdf.line(110,110,110,10)
    pdf.line(110,50,200,50)
    pdf.line(130,50,130,80)
    pdf.line(10,70,200,70)
    pdf.line(110,60,200,60)
    pdf.line(110,80,200,80)
    pdf.line(110,90,200,90)
    pdf.line(110,100,200,100)
    pdf.line(10,120,200,120)
    pdf.line(10,110,200,110)
    pdf.line(10,190,200,190)
    pdf.line(140,215,200,215)
    pdf.line(140,265,200,265)
    pdf.line(140,215,140,265)
    pdf.set_line_width(0.5)
    pdf.line(140,225,200,225)
    pdf.line(140,235,200,235)
    pdf.line(140,245,200,245)
    pdf.line(140,255,200,255)
    pdf.line(168,215,168,265)
    pdf.line(28,110,28,190)
    pdf.line(100, 110, 100, 190)
    pdf.line(118, 110, 118, 190)
    pdf.line(138, 110, 138, 190)
    pdf.line(168, 110, 168, 190)
    pdf.output("GFG.pdf")


def delt():
    print(s)


totallist = []
w = Tk()

w.wm_title('BILL')

l1 = Label(w, text='Customer Name')
l1.grid(row=0, column=0)

name = StringVar()
e1 = Entry(w, text=name, width=30)
e1.grid(row=0, column=1, rowspan=2, columnspan=4)

l2 = Label(w, text='Address')
l2.grid(row=2, column=0)

add = StringVar()
e2 = Entry(w, text=add, width=30)
e2.grid(row=2, column=1, rowspan=2, columnspan=4)

l3 = Label(w, text='GSTIN NO')
l3.grid(row=4, column=0)

# Combobox
gst = tk.StringVar()
cb1 = ttk.Combobox(w, width=15, textvariable=gst)
cb1['values'] = ('27AAPPA5149R1Z1', '27EXAPS8247G1Z1')
cb1.grid(row=4, column=1, columnspan=1)
cb1.current()

l4 = Label(w, text='STATE')
l4.grid(row=6, column=0)

# Combobox
state = tk.StringVar()
cb2 = ttk.Combobox(w, width=15, textvariable=state)
cb2['values'] = ('MAHARASTRA', 'GUJRAT')
cb2.grid(row=6, column=1, columnspan=1)
cb2.current()

l5 = Label(w, text='Code')
l5.grid(row=6, column=3)

state_code = StringVar()
e5 = Entry(w, text=state_code, width=5)
e5.grid(row=6, column=4, rowspan=2)


l6 = Label(w, text='Material Name')
l6.grid(row=8, column=0)

# Combobox
material = tk.StringVar()
cb3 = ttk.Combobox(w, width=30, textvariable=material)
cb3['values'] = ('POLY WOSHER BIG', 'POLY WOSHER SMALL', 'NEW BBC')
cb3.grid(row=9, column=0, columnspan=4)
cb3.current()

l7 = Label(w, text='HSN')
l7.grid(row=8, column=4)

hsn = StringVar()
e7 = Entry(w, text=hsn, width=5)
e7.grid(row=9, column=4)

l8 = Label(w, text='Quantity')
l8.grid(row=8, column=5)

quantity = StringVar()
e8 = Entry(w, text=quantity, width=5)
e8.grid(row=9, column=5)

l9 = Label(w, text='Rate per pcs')
l9.grid(row=8, column=6)

rate = StringVar()
e9 = Entry(w, text=rate, width=5)
e9.grid(row=9, column=6)

l10 = Label(w, text='Amount')
l10.grid(row=8, column=7)

amount = StringVar()
e10 = Entry(w, text=amount, width=10)
e10.grid(row=9, column=7)

l11 = Label(w, text='Total')
l11.grid(row=11, column=6)

total = StringVar()
e11 = Entry(w, text=total, width=10)
e11.grid(row=11, column=7)

l12 = Label(w, text='CGST 9%')
l12.grid(row=12, column=6)

cgst = StringVar()
e12 = Entry(w, text=cgst, width=10)
e12.grid(row=12, column=7)

l13 = Label(w, text='SGST 9%')
l13.grid(row=13, column=6)

sgst = StringVar()
e13 = Entry(w, text=sgst, width=10)
e13.grid(row=13, column=7)

l14 = Label(w, text='Round Off')
l14.grid(row=14, column=6)

roundoff = StringVar()
e14 = Entry(w, text=roundoff, width=10)
e14.grid(row=14, column=7)

l15 = Label(w, text='Grand Total')
l15.grid(row=15, column=6)

gtotal = StringVar()
e15 = Entry(w, text=gtotal, width=10)
e15.grid(row=15, column=7)

list1 = Listbox(w, height=13, width=45)
list1.grid(row=12, column=0, rowspan=8, columnspan=5)

sb1 = Scrollbar(w)
sb1.grid(row=11, column=5, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', sel_row)

l11 = Label(w, text='Materials').grid(row=10, column=0)
l12 = Label(w, text='          HSN  Qty   Rate    Amnt').grid(row=10, column=1)

b1 = Button(w, text='Add', width=5, command=ad)
b1.grid(row=16, column=5)

b2 = Button(w, text='Delete', width=5, command=delt)
b2.grid(row=17, column=5)

b3 = Button(w, text='Total', width=5, command=tot)
b3.grid(row=17, column=6)

b4 = Button(w, text='Print', width=5, command=prnt)
b4.grid(row=17, column=7)

l16 = Label(w, text='Date')
l16.grid(row=0, column=5)

date = StringVar()
e16 = Entry(w, text=date, width=10)
e16.grid(row=0, column=6)

l17 = Label(w, text='Invoice No:')
l17.grid(row=2, column=5)

invoice = StringVar()
e17 = Entry(w, text=invoice, width=10)
e17.grid(row=2, column=6)
w.mainloop()
