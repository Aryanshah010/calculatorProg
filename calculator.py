import tkinter as tk
from tkinter import *

first_num=second_num=operator=None

def get_digit(digit):
    current=display_label["text"]
    new=current+str(digit)
    display_label.config(text=new)

def clear():
    display_label.config(text='')

def get_operator(op):
    global first_num,operator
    first_num=int(display_label['text'])
    operator=op
    display_label.config(text='')

def get_result():
    global first_num,second_num,operator
    second_num=int(display_label['text'])
    if operator == '+':
        display_label.config(text=str(first_num+second_num))
    elif operator == "-":
        display_label.config(text=str(first_num-second_num))
    
    elif operator == "*":
        display_label.config(text=str(first_num*second_num))

    else:
        if second_num==0:
            display_label.config(text="Error")
        else:
            display_label.config(text=str(round(first_num / second_num,2)))

window=tk.Tk()
window.title("Calculator")
window.geometry("320x305")
window.resizable(0,0)
window.configure(background='black')

display_label=tk.Label(window,text='',background="black",foreground="white",font="Times 35 bold")
display_label.grid(row=0,column=0,padx=5,pady=25,sticky="w",columnspan=10)

btn7=Button(window,text='7',fg='black',width=2,font="verdana 30",command=lambda :get_digit(7))
btn7.grid(row=1,column=0,padx=1)

btn8=Button(window,text='8',fg='black',width=2,font="verdana 30",command=lambda :get_digit(8))
btn8.grid(row=1,column=1,padx=1)


btn9=Button(window,text='9',fg='black',width=2,font="verdana 30",command=lambda :get_digit(9))
btn9.grid(row=1,column=2,padx=1)


btn_add=Button(window,text='+',fg='black',width=2,font="verdana 30",command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3,padx=1)


btn4=Button(window,text='4',fg='black',width=2,font="verdana 30",command=lambda :get_digit(4))
btn4.grid(row=2,column=0,padx=1)

btn5=Button(window,text='5',fg='black',width=2,font="verdana 30",command=lambda :get_digit(5))
btn5.grid(row=2,column=1,padx=1)


btn6=Button(window,text='6',fg='black',width=2,font="verdana 30",command=lambda :get_digit(6))
btn6.grid(row=2,column=2,padx=1)


btn_sub=Button(window,text='-',fg='black',width=2,font="verdana 30",command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3,padx=1)


btn1=Button(window,text='1',fg='black',width=2,font="verdana 30",command=lambda :get_digit(1))
btn1.grid(row=3,column=0,padx=1)

btn2=Button(window,text='2',fg='black',width=2,font="verdana 30",command=lambda :get_digit(2))
btn2.grid(row=3,column=1,padx=1)


btn3=Button(window,text='3',fg='black',width=2,font="verdana 30",command=lambda :get_digit(3))
btn3.grid(row=3,column=2,padx=1)


btn_mul=Button(window,text='*',fg='black',width=2,font="verdana 30",command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3,padx=1)

btn_clear=Button(window,text='C',fg='black',width=2,font="verdana 30",command=lambda:clear())
btn_clear.grid(row=4,column=0)

btn0=Button(window,text='0',fg='black',width=2,font="verdana 30",command=lambda :get_digit(0))
btn0.grid(row=4,column=1)

btn_div=Button(window,text='/',fg='black',width=2,font="verdana 30",command=lambda:get_operator('/'))
btn_div.grid(row=4,column=2)


btn_equal=Button(window,text='=',fg='black',width=2,font="verdana 30",command=get_result)
btn_equal.grid(row=4,column=3)


window.mainloop()















































