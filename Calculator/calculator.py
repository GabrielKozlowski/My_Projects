from tkinter import *
from math import sqrt

root = Tk()
root.title('Calculator')

# root.maxsize(400, 600)
root.minsize(400, 600)
root.geometry('400x600')





name = Label(root, text="Standard", pady=2)
name.grid(row=0, column=0)

sum_result = Entry(root, width=50)
sum_result.grid(row=1, column=0, columnspan=4)


def ButtoClick(number):
    current = sum_result.get()
    sum_result.delete(0, END)
    sum_result.insert(0, str(current) + str(number))


def ButtonDelete():
    sum_result.delete(0, END)


def ButtonUndo():
    current = sum_result.get()
    sum_result.delete(len(current)-1)

def ButtonNegative():
    current = float(sum_result.get())
    if current == abs(current):
        sum_result.delete(0, END)
        sum_result.insert(0, -abs(current)) 
    else:
        current = abs(current)
        sum_result.delete(0, END)
        sum_result.insert(0, abs(current))


def ButtonDot():
    current = sum_result.get()
    if current == '':
        pass
    else:
        if '.' in current:
            pass
        else:
            sum_result.delete(0, END)
            sum_result.insert(0, current + '.')


def ButtonOneDivisionBy():
    current = sum_result.get()
    current = 1 / float(current)
    sum_result.delete(0, END)
    sum_result.insert(0, current)

def ButtoPowerByTwo():
    current = sum_result.get()
    if '.' in current:
        current = float(current)
        sum_result.delete(0, END)
        sum_result.insert(0, current ** 2)
    else:
        current = int(current)
        sum_result.delete(0, END)
        sum_result.insert(0, current ** 2)


def ButtoSqrt():
    current = sum_result.get()
    if '.' in current:
        current = float(current)
        sum_result.delete(0, END)
        sum_result.insert(0, sqrt(current))
    else:
        current = int(current)
        result = sqrt(current)
        if result.is_integer():
            sum_result.delete(0, END)
            sum_result.insert(0, int(result))
        else:
            sum_result.delete(0, END)
            sum_result.insert(0, result)
        

division_button = Button(root, width=11, pady=15, text='%', command=lambda: ButtoClick)
ce_button = Button(root, width=11, pady=15, text='CE', command=lambda: ButtonDelete())
c_button = Button(root, width=11, pady=15, text='C', command=lambda: ButtonDelete())
back_space_button = Button(root, width=11, pady=15, text='<--', command=lambda: ButtonUndo())

one_division_by = Button(root, width=11, pady=15, text='1/x', command=lambda: ButtonOneDivisionBy())
power_by_two = Button(root, width=11, pady=15, text='x**2', command=lambda: ButtoPowerByTwo())
square_root = Button(root, width=11, pady=15, text='square_root', command=lambda: ButtoSqrt())
division = Button(root, width=11, pady=15, text='/', command=lambda: ButtoClick)

multiplication_button = Button(root, width=11, pady=15, text='X', command=lambda: ButtoClick)
nine_button = Button(root, width=11, pady=15, text='9', command=lambda: ButtoClick(9))
eight_button = Button(root, width=11, pady=15, text='8', command=lambda: ButtoClick(8))
seven_button = Button(root, width=11, pady=15, text='7', command=lambda: ButtoClick(7))

subtraction_button = Button(root, width=11, pady=15, text='-', command=lambda: ButtoClick)
six_button = Button(root, width=11, pady=15, text='6', command=lambda: ButtoClick(6))
five_button = Button(root, width=11, pady=15, text='5', command=lambda: ButtoClick(5))
four_button = Button(root, width=11, pady=15, text='4', command=lambda: ButtoClick(4))

addition_button = Button(root, width=11, pady=15, text='+', command=lambda: ButtoClick)
three_button = Button(root, width=11, pady=15, text='3', command=lambda: ButtoClick(3))
two_button = Button(root, width=11, pady=15, text='2', command=lambda: ButtoClick(2))
one_button = Button(root, width=11, pady=15, text='1', command=lambda: ButtoClick(1))

sum_button = Button(root, width=11, pady=15, text='=', command=lambda: ButtoClick)
comma_button = Button(root, width=11, pady=15, text='.', command=lambda: ButtonDot())
zero_button = Button(root, width=11, pady=15, text='0', command=lambda: ButtoClick(0))
naegative_button = Button(root, width=11, pady=15, text='+/-', command=lambda: ButtonNegative())





division_button.grid(row=2, column=0)
ce_button.grid(row=2, column=1)
c_button.grid(row=2, column=2)
back_space_button.grid(row=2, column=3)

one_division_by.grid(row=3, column=0)
power_by_two.grid(row=3, column=1)
square_root.grid(row=3, column=2)
division.grid(row=3, column=3)

seven_button.grid(row=4, column=0)
eight_button.grid(row=4, column=1)
nine_button.grid(row=4, column=2)
multiplication_button.grid(row=4, column=3)

four_button.grid(row=5, column=0)
five_button.grid(row=5, column=1)
six_button.grid(row=5, column=2)
subtraction_button.grid(row=5, column=3)

one_button.grid(row=6, column=0)
two_button.grid(row=6, column=1)
three_button.grid(row=6, column=2)
addition_button.grid(row=6, column=3)

naegative_button.grid(row=7, column=0)
zero_button.grid(row=7, column=1)
comma_button.grid(row=7, column=2)
sum_button.grid(row=7, column=3)





root.mainloop()