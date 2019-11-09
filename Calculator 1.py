from tkinter import *

# ---------------------------------------------
# Functions


def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clear_button():
    global operator
    operator = ''
    text_input.set(operator)


def equal_button():
    global operator
    try:
        sum = str(eval(operator))
    except SyntaxError:
        sum = 'Error'
    text_input.set(sum)
    operator = ''


cal = Tk()
cal.title('Calculator')
operator = ''
last_text = ''
text_input = StringVar()


txt_display = Entry(cal, font=('Arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                    bg='powder blue', justify='right').grid(columnspan=4)

# ---------------------------------------------
# Buttons

button_0 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='0', command=lambda: button_click(0), bg='powder blue').grid(row=4, column=0)
clear_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='C', command=clear_button, bg='powder blue').grid(row=4, column=1)
equal_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='=', command=equal_button, bg='powder blue').grid(row=4, column=2)

button_1 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='1', command=lambda: button_click(1), bg='powder blue').grid(row=3, column=0)
button_2 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='2', command=lambda: button_click(2), bg='powder blue').grid(row=3, column=1)
button_3 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='3', command=lambda: button_click(3), bg='powder blue').grid(row=3, column=2)
button_4 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='4', command=lambda: button_click(4), bg='powder blue').grid(row=2, column=0)
button_5 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='5', command=lambda: button_click(5), bg='powder blue').grid(row=2, column=1)
button_6 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='6', command=lambda: button_click(6), bg='powder blue').grid(row=2, column=2)
button_7 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='7', command=lambda: button_click(7), bg='powder blue').grid(row=1, column=0)
button_8 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='8', command=lambda: button_click(8), bg='powder blue').grid(row=1, column=1)
button_9 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='9', command=lambda: button_click(9), bg='powder blue').grid(row=1, column=2)

addition_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='+', command=lambda: button_click('+'), bg='powder blue').grid(row=1, column=3)
subtraction_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='-', command=lambda: button_click('-'), bg='powder blue').grid(row=2, column=3)
multiplication_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='*', command=lambda: button_click('*'), bg='powder blue').grid(row=3, column=3)
division_button = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('Arial', 20, 'bold'), text='/', command=lambda: button_click('/'), bg='powder blue').grid(row=4, column=3)

cal.mainloop()
