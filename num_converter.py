from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Number Converter')
root.geometry('1280x720')
root.config(bg='lightblue')

lblbinary = StringVar()
lbldecimal = StringVar()
lblhexa = StringVar()
lbloctal = StringVar()

def update_num_from_decimal(decimal_value):
    lbldecimal.set(str(decimal_value))

def convert_from_binary(binary_value):
    try:
        decimal_value = int(binary_value, 2)
        lblbinary.set(binary_value)
        lbldecimal.set(str(decimal_value))
        update_num_from_decimal(decimal_value)
        lblhexa.set(hex(decimal_value)[2:].upper())
        lbloctal.set(oct(decimal_value)[2:])
    except ValueError:
        messagebox.showerror('Error', 'Invalid binary number')

def convert_from_octal(octal_value):
    try:
        decimal_value = int(octal_value, 8)
        lblbinary.set(bin(decimal_value)[2:])
        lbldecimal.set(str(decimal_value))
        update_num_from_decimal(decimal_value)
        lblhexa.set(hex(decimal_value)[2:].upper())
        lbloctal.set(octal_value)
    except ValueError:
        messagebox.showerror('Error', 'Invalid octal number')

def convert_from_hexadecimal(hex_value):
    try:
        decimal_value = int(hex_value, 16)
        lblbinary.set(bin(decimal_value)[2:])
        lbldecimal.set(str(decimal_value))
        update_num_from_decimal(decimal_value)
        lblhexa.set(hex_value.upper())
        lbloctal.set(oct(decimal_value)[2:])
    except ValueError:
        messagebox.showerror('Error', 'Invalid hexadecimal number')

def convert_from_decimal(decimal_value):
    try:
        decimal_value = int(decimal_value)
        lblbinary.set(bin(decimal_value)[2:])
        lbldecimal.set(str(decimal_value))
        update_num_from_decimal(decimal_value)
        lblhexa.set(hex(decimal_value)[2:].upper())
        lbloctal.set(oct(decimal_value)[2:])
    except ValueError:
        messagebox.showerror('Error', 'Invalid decimal number')

def on_binary_change(*args):
    binary_value = lblbinary.get()
    if binary_value:
        convert_from_binary(binary_value)

def on_octal_change(*args):
    octal_value = lbloctal.get()
    if octal_value:
        convert_from_octal(octal_value)

def on_hexadecimal_change(*args):
    hex_value = lblhexa.get()
    if hex_value:
        convert_from_hexadecimal(hex_value)

def on_decimal_change(*args):
    decimal_value = lbldecimal.get()
    if decimal_value:
        convert_from_decimal(decimal_value)

def confirm_exit():
    if messagebox.askyesno("Confirm Exit", "Do you really want to exit?"):
        root.destroy()

description_text = """
Number Converter:\n
This application facilitates the conversion of numerical values between\n
binary, decimal, hexadecimal, and octal formats. Inputting a number in\n
any field will promptly update the corresponding values in the other fields.\n
Error handling is incorporated to manage invalid numerical inputs.
"""

description_frame = Frame(root, bg='lightblue', bd=2, relief=GROOVE)
description_frame.grid(row=0, column=0, sticky='nw', padx=10, pady=10)
description_label = Label(description_frame, text=description_text, font=('arial bold', 12), bg='lightblue', justify=LEFT)
description_label.pack(fill=BOTH)

Label(root, text='Conversion System', font=('times new roman', 60, 'bold'), bg='lightgreen', fg='blue', relief=RIDGE).grid(row=1, column=0, columnspan=2, pady=20)

content_frame = Frame(root, bg='lightblue', bd=2, relief=GROOVE)
content_frame.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

Label(content_frame, text='Binary', font='arial 20 bold', bg='lightblue').grid(row=0, column=0, padx=20, pady=10, sticky='e')
Entry(content_frame, font=('times new roman', 20, 'bold'), fg='blue', justify=CENTER, relief=GROOVE, textvariable=lblbinary, bg='lightyellow').grid(row=0, column=1, padx=20, pady=10)

Label(content_frame, text='Decimal', font='arial 20 bold', bg='lightblue').grid(row=1, column=0, padx=20, pady=10, sticky='e')
Entry(content_frame, font=('times new roman', 20, 'bold'), fg='blue', justify=CENTER, relief=GROOVE, textvariable=lbldecimal, bg='lightyellow').grid(row=1, column=1, padx=20, pady=10)

Label(content_frame, text='Hexadecimal', font='arial 20 bold', bg='lightblue').grid(row=2, column=0, padx=20, pady=10, sticky='e')
Entry(content_frame, font=('times new roman', 20, 'bold'), fg='blue', justify=CENTER, relief=GROOVE, textvariable=lblhexa, bg='lightyellow').grid(row=2, column=1, padx=20, pady=10)

Label(content_frame, text='Octal', font='arial 20 bold', bg='lightblue').grid(row=3, column=0, padx=20, pady=10, sticky='e')
Entry(content_frame, font=('times new roman', 20, 'bold'), fg='blue', justify=CENTER, relief=GROOVE, textvariable=lbloctal, bg='lightyellow').grid(row=3, column=1, padx=20, pady=10)

lblbinary.trace_add("write", on_binary_change)
lbldecimal.trace_add("write", on_decimal_change)
lblhexa.trace_add("write", on_hexadecimal_change)
lbloctal.trace_add("write", on_octal_change)

buttons_frame = Frame(root, bg='lightblue')
buttons_frame.grid(row=3, column=0, columnspan=2, pady=30)

Button(buttons_frame, text='Convert', font='arial 20 bold', fg='white', bg='#4682B4', width=10, relief=GROOVE, bd=10, command=None).grid(row=0, column=0, padx=20)
Button(buttons_frame, text='Clear', font='arial 20 bold', fg='white', bg='#4682B4', width=10, relief=GROOVE, bd=10, command=lambda: [lblbinary.set(''), lbldecimal.set(''), lblhexa.set(''), lbloctal.set('')]).grid(row=0, column=1, padx=20)
Button(buttons_frame, text='Exit', font='arial 20 bold', fg='white', bg='#4682B4', width=10, relief=GROOVE, bd=10, command=confirm_exit).grid(row=0, column=2, padx=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()