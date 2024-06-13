from tkinter import *

root=Tk()
root.title("Calculator")

num=Entry(root,width=35,borderwidth=5)
num.grid(row=0,column=0,columnspan=3,pady=10)


global fValue
global operator

operator=''

def button_clicked(number):
    current=num.get()
    num.delete(0, END)
    num.insert(-1,  str(current) + str(number))

def button_clear():
    num.delete(0, END)


def button_add():
    first_value=num.get()
    global fValue
    global operator
    operator = 'add'
    fValue=int(first_value)
    num.delete(0,END)
    return True



def button_subtract():
    first_value = num.get()
    global fValue
    global operator
    operator = 'subtract'
    fValue = int(first_value)
    num.delete(0, END)
    return True

def button_multiply():
    first_value = num.get()
    global fValue
    global operator
    operator = 'multiply'
    fValue = int(first_value)
    num.delete(0, END)
    return True

def button_divide():
    first_value = num.get()
    global fValue
    global operator
    operator = 'divide'
    fValue = int(first_value)
    num.delete(0, END)
    return True,fValue



def button_equal():
    secondValue=(num.get())
    num.delete(0,END)

    if operator=='add':
        num.insert(0,fValue + int(secondValue))
    elif operator=='subtract':
        num.insert(0,fValue - int(secondValue))
    elif operator=='multiply':
        num.insert(0,fValue * int(secondValue))
    elif operator=='divide':
        num.insert(0, fValue / int(secondValue))








numButton0=Button(root,text="0",padx=40,pady=20,command=lambda: button_clicked(0))
numButton1=Button(root,text="1",padx=40,pady=20,command=lambda: button_clicked(1))
numButton2=Button(root,text="2",padx=40,pady=20,command=lambda: button_clicked(2))
numButton3=Button(root,text="3",padx=40,pady=20,command=lambda: button_clicked(3))
numButton4=Button(root,text="4",padx=40,pady=20,command=lambda: button_clicked(4))
numButton5=Button(root,text="5",padx=40,pady=20,command=lambda: button_clicked(5))
numButton6=Button(root,text="6",padx=40,pady=20,command=lambda: button_clicked(6))
numButton7=Button(root,text="7",padx=40,pady=20,command=lambda: button_clicked(7))
numButton8=Button(root,text="8",padx=40,pady=20,command=lambda: button_clicked(8))
numButton9=Button(root,text="9",padx=40,pady=20,command=lambda: button_clicked(9))

addButton=Button(root,text="+",padx=39,pady=20,command=button_add)
subtractButton=Button(root,text="-",padx=39,pady=20,command=button_subtract)
multiplyButton=Button(root,text="*",padx=39,pady=20,command=button_multiply)
divideButton=Button(root,text="/",padx=39,pady=20,command=button_divide)


equalButton=Button(root,text="=",padx=101,pady=20,command=button_equal)
clearButton=Button(root,text="Clear",padx=90,pady=20,command=button_clear)

numButton1.grid(row=3,column=0)
numButton2.grid(row=3,column=1)
numButton3.grid(row=3,column=2)

numButton4.grid(row=2,column=0)
numButton5.grid(row=2,column=1)
numButton6.grid(row=2,column=2)

numButton7.grid(row=1,column=0)
numButton8.grid(row=1,column=1)
numButton9.grid(row=1,column=2)

numButton0.grid(row=4,column=0)


addButton.grid(row=5,column=0)
subtractButton.grid(row=6,column=0)
multiplyButton.grid(row=6,column=1)
divideButton.grid(row=6,column=2)

equalButton.grid(row=5,column=1,columnspan=2)
clearButton.grid(row=4,column=1,columnspan=2)









root.mainloop()