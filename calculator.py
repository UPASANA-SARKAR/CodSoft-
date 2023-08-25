from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))



root = Tk()
root.title("CALCULATOR")
root.geometry("280x380")
root.maxsize(280,380)
root.configure(bg = "black")

result_label = Label(root,text = '',bg = "black",fg = "white" )
result_label.grid(row=0, column=0, columnspan=10, pady=(50,25), sticky='w')
result_label.config(font="verdana 30 bold")

button7 = Button(root,text='7',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(7))
button7.grid(row=1,column=0)
button7.config(font="verdana 14")

button8 = Button(root,text='8',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(8))
button8.grid(row=1,column=1)
button8.config(font="verdana 14")

button9 = Button(root,text='9',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(9))
button9.grid(row=1,column=2)
button9.config(font="verdana 14")

button_add = Button(root,text='+',bg="red",fg="white",width=5,height=2, command=lambda :get_operator('+'))
button_add.grid(row=1,column=3)
button_add.config(font="verdana 14")

button4 = Button(root,text='4',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(4))
button4.grid(row=2,column=0)
button4.config(font="verdana 14")

button5 = Button(root,text='5',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(5))
button5.grid(row=2,column=1)
button5.config(font="verdana 14")

button6 = Button(root,text='6',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(6))
button6.grid(row=2,column=2)
button6.config(font="verdana 14")

button_sub = Button(root,text='-',bg="red",fg="white",width=5,height=2, command=lambda :get_operator('-'))
button_sub.grid(row=2,column=3)
button_sub.config(font="verdana 14")

button1 = Button(root,text='1',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(1))
button1.grid(row=3,column=0)
button1.config(font="verdana 14")

button2 = Button(root,text='2',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(2))
button2.grid(row=3,column=1)
button2.config(font="verdana 14")

button3 = Button(root,text='3',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(3))
button3.grid(row=3,column=2)
button3.config(font="verdana 14")

button_mul = Button(root,text='*',bg="red",fg="white",width=5,height=2, command=lambda :get_operator('*'))
button_mul.grid(row=3,column=3)
button_mul.config(font="verdana 14")

button0 = Button(root,text='0',bg="red",fg="white",width=5,height=2,command=lambda :get_digit(0))
button0.grid(row=4,column=0)
button0.config(font="verdana 14")

button_clr = Button(root,text='C',bg="red",fg="white",width=5,height=2, command=lambda :clear())
button_clr.grid(row=4,column=1)
button_clr.config(font="verdana 14")

button_equals = Button(root,text='=',bg="red",fg="white",width=5,height=2, command = get_result)
button_equals.grid(row=4,column=2)
button_equals.config(font="verdana 14")

button_div = Button(root,text='/',bg="red",fg="white",width=5,height=2, command=lambda :get_operator('/'))
button_div.grid(row=4,column=3)
button_div.config(font="verdana 14")



root.mainloop()