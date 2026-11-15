import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from ServiceCentreone import *
from ProductCategorytwo import *
from Productsthree import *
from ServiceTypesfour import *
from Customersfive import *
from Engineerssix import *
from CallDataseven import *
from CallCloseDataeight import *
from CallFeedbacknine import *


t=tkinter.Tk()
t.geometry('800x650')
t.configure(bg='light blue')
t.title('Service Centre Management System')
a=Label(t, text="DASHBOARD")
a.place(x=390,y=60)
b1=Button(t,text='Service Centre', command=servicecentreone, width=25, height=3)
b1.place(x=100,y=100)
b2=Button(t,text='Product Category',command=productcategorytwo,width=25,height=3)
b2.place(x=300,y=100)
b3=Button(t,text='Products',command=productsthree,width=25,height=3)
b3.place(x=500,y=100)
b4=Button(t,text='Service Types',command=servicetypesfour,width=25,height=3)
b4.place(x=100,y=200)
b5=Button(t,text='Customers',command=customersfive,width=25,height=3)
b5.place(x=300,y=200)
b6=Button(t,text='Engineers',command=engineerssix,width=25,height=3)
b6.place(x=500,y=200)
b7=Button(t,text='Call Data',command=calldataseven,width=25,height=3)
b7.place(x=100,y=300)
b8=Button(t,text='Call Close Data',command=callclosedataeight,width=25,height=3)
b8.place(x=300,y=300)
b9=Button(t,text='Call Feedback',command=callfeedbacknine,width=25,height=3)
b9.place(x=500,y=300)
t.mainloop()


