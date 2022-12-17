from tkinter import *

root = Tk()
root.title('Calculator')

# root.maxsize(400, 600)
root.minsize(400, 600)
root.geometry('400x600')





name = Label(root, text="Standard", pady=2)
name.grid(row=0, column=0)

sum_result = Entry(root, width=50)
sum_result.grid(row=1, column=0, columnspan=4)


def button_click(number):
    current = sum_result.get()
    sum_result.delete(0, END)
    sum_result.insert(0, str(current) + str(number))


def button_delete():
    sum_result.delete(0, END)


def button_undo():
    current = sum_result.get()
    sum_result.delete(len(current)-1)


division_button = Button(root, width=11, pady=15, text='%', command=lambda: button_click)
ce_button = Button(root, width=11, pady=15, text='CE', command=lambda: button_delete())
c_button = Button(root, width=11, pady=15, text='C', command=lambda: button_delete())
back_space_button = Button(root, width=11, pady=15, text='<--', command=lambda: button_undo())

one_division_by = Button(root, width=11, pady=15, text='1/x', command=lambda: button_click)
power_by_two = Button(root, width=11, pady=15, text='x**2', command=lambda: button_click)
square_root = Button(root, width=11, pady=15, text='square_root', command=lambda: button_click)
division = Button(root, width=11, pady=15, text='/', command=lambda: button_click)

multiplication_button = Button(root, width=11, pady=15, text='X', command=lambda: button_click)
nine_button = Button(root, width=11, pady=15, text='9', command=lambda: button_click(9))
eight_button = Button(root, width=11, pady=15, text='8', command=lambda: button_click(8))
seven_button = Button(root, width=11, pady=15, text='7', command=lambda: button_click(7))

subtraction_button = Button(root, width=11, pady=15, text='-', command=lambda: button_click)
six_button = Button(root, width=11, pady=15, text='6', command=lambda: button_click(6))
five_button = Button(root, width=11, pady=15, text='5', command=lambda: button_click(5))
four_button = Button(root, width=11, pady=15, text='4', command=lambda: button_click(4))

addition_button = Button(root, width=11, pady=15, text='+', command=lambda: button_click)
three_button = Button(root, width=11, pady=15, text='3', command=lambda: button_click(3))
two_button = Button(root, width=11, pady=15, text='2', command=lambda: button_click(2))
one_button = Button(root, width=11, pady=15, text='1', command=lambda: button_click(1))

sum_button = Button(root, width=11, pady=15, text='=', command=lambda: button_click)
comma_button = Button(root, width=11, pady=15, text=',', command=lambda: button_click)
zero_button = Button(root, width=11, pady=15, text='0', command=lambda: button_click(0))
naegative_button = Button(root, width=11, pady=15, text='+/-', command=lambda: button_click)





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