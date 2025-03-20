from tkinter import *
import random
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime  

root=Tk()
root.title('Billing Slip')
root.geometry('1280x720')
bg_color= '#4D0039'

c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000,9999)
bill_no.set(str(x))
custom_welcome = StringVar()
custom_welcome.set('Welcome to the Billing System')
l=[]


def welcome():
    textarea.delete(1.0, END)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    textarea.insert(END, "            *** Billing Slip ***\n")
    textarea.insert(END, f"            Bill No: {bill_no.get()}\n")
    textarea.insert(END, f"            Customer: {c_name.get()}\n")
    textarea.insert(END, f"            Phone: {c_phone.get()}\n")
    textarea.insert(END, "==============================================\n")
    textarea.insert(END, f"            {custom_welcome.get()}\n")
    textarea.insert(END, "==============================================\n")
    textarea.insert(END, "Product               Qty    Rate     Price\n")
    textarea.insert(END, "----------------------------------------------\n")
    
    for i in range(len(l)):
        
        product_name = item.get().ljust(20)  
        qty = str(Quantity.get()).rjust(6)    
        rate = str(Rate.get()).rjust(8)      
        price = str(l[i]).rjust(10)         

        textarea.insert(END, f"{product_name}{qty}{rate}{price}\n")

    textarea.insert(END, "----------------------------------------------\n")
    textarea.insert(END, f"\nTotal Amount:  {sum(l)}\n")
    textarea.insert(END, "==============================================\n")
    textarea.insert(END, f"Date & Time: {current_time}\n")
    textarea.insert(END, "Thank you for shopping with us!\n")
    textarea.insert(END, "Visit us again!\n")


def additm():
    rate_value = c_phone.get()
    quantity_value = Quantity.get()

    if not rate_value.isdigit():
        messagebox.showerror('Error', 'Product rate must be a valid number.')
        return

    if not is_valid_number(quantity_value, integer=True):
        messagebox.showerror('Error', 'Product quantity must be a valid number.')        
        return

    rate_value = float(rate_value)
    quantity_value = int(quantity_value)
    m = rate_value * quantity_value
    l.append(m)

    if item.get() == '':
        messagebox.showerror('Error', 'Please Enter the item')
    else:
        item_name = item.get().ljust(20)
        quantity = str(quantity_value).rjust(10)
        rate = str(rate_value).rjust(10)
        price = str(m).rjust(10)
        textarea.insert((10.0 + float(len(l) - 1)), f'{item_name}{quantity}{rate}{price}\n')


def is_valid_number(value, integer=False):
    try:
        if integer:
            int(value)
        else:
            float(value)
        return True
    except ValueError:
        return False


def gbill():
    if c_name.get() == '' or not c_name.get().isalpha():
        messagebox.showerror('Error', 'Customer name must contain only alphabets.')
        return

    if c_phone.get() == '' or not c_phone.get().isdigit():
        messagebox.showerror('Error', 'Phone number must contain only digits.')
        return
    
    welcome()
    tex = textarea.get(10.0, (10.0 + float(len(l))))
    textarea.insert(END, tex)
    textarea.insert(END, "\n======================================\n")
    textarea.insert(END, f"Total payable Amount: {sum(l)}\n")
    textarea.insert(END, "======================================\n")
    savebill()


def savebill():
    op = messagebox.askyesno('Save Bill', 'Do you want to save the bill?')
    if op > 0:
        bills_details = textarea.get(1.0, END)
        import os
        if not os.path.exists("bills"):        #Ensure there is a folder named "bills" where the bill will be saved

            os.makedirs("bills")
        with open(f"bills/{bill_no.get()}.txt", 'w') as f1:
            f1.write(bills_details)
        messagebox.showinfo('Saved', f'Bill no: {bill_no.get()} saved successfully')
    else:
        return


def clear():
    c_name.set('')  
    c_phone.set('')  
    item.set('')  
    Rate.set(0)  
    Quantity.set(0)  
    l.clear()  
    welcome()  



def exit():
    op=messagebox.askyesno('Exit', 'Do you really want to exit')  
    if op>0:
        root.destroy()


def set_custom_welcome():
    custom_text = simpledialog.askstring("Enter Business Name", "Enter the name for the welcome message:")
    if custom_text:
        custom_welcome.set(custom_text)
        welcome()


title=Label(root, text='Billing Software', bg=bg_color, fg='white',font=('times new rommon', 25, 'bold'), relief=GROOVE,bd=12)
title.pack(fill=X)


F1=LabelFrame(root,text='Customer Details', bg=bg_color, fg='gold',font=('times new rommon', 18, 'bold'), relief=GROOVE,bd=10)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name', bg=bg_color, fg='white',font=('times new rommon', 18, 'bold'))
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt = Entry(F1,width=15,font=('arial', 15, 'bold'), relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No.', bg=bg_color, fg='white',font=('times new rommon', 18, 'bold'))
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)
cphone_txt = Entry(F1,width=15,font=('arial', 15, 'bold'), relief=SUNKEN, textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)


F2=LabelFrame(root,text='Product Details', bg=bg_color, fg='gold',font=('times new rommon', 18, 'bold'), relief=GROOVE,bd=10)
F2.place(x=20,y=180,width=630,height=500)

itm=Label(F2,text='Product Name', font=('times new rommon',18,'bold'),bg=bg_color,fg='light green')
itm.grid(row=0,column=0,padx=30,pady=20)
itm_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)

rate=Label(F2,text='Product Rate', font=('times new rommon',18,'bold'),bg=bg_color,fg='light green')
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold', textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

quantity=Label(F2,text='Product Quantity', font=('times new rommon',18,'bold'),bg=bg_color,fg='light green')
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold', textvariable= Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)


btn1=Button(F2,text='Add item', font='arial 15 bold',padx=5,pady=10,bg='#A4D400',width=15, command=additm)
btn1.grid(row=3, column=0, padx=10, pady=30)

btn2=Button(F2,text='Generate Bill', font='arial 15 bold',padx=5,pady=10,bg='#A4D400',width=15, command= gbill)
btn2.grid(row=3, column=1, padx=10, pady=30)

btn3=Button(F2,text='Clear', font='arial 15 bold',padx=5,pady=10,bg='#A4D400',width=15, command=clear)
btn3.grid(row=4, column=0, padx=10, pady=30)

btn4=Button(F2,text='Exit', font='arial 15 bold',padx=5,pady=10,bg='#A4D400',width=15, command=exit)
btn4.grid(row=4, column=1, padx=10, pady=30)

btn_set_custom_welcome = Button(F1, text='Set Custom Welcome', font='arial 15 bold', padx=5, pady=10, bg='#A4D400', width=20, command=set_custom_welcome)
btn_set_custom_welcome.grid(row=0, column=4, padx=10, pady=5)


F3= Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold', relief=GROOVE,bd=7).pack(fill=X)
scroll_y= Scrollbar(F3, orient=VERTICAL)
textarea= Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT, fill= Y)
scroll_y.config(command=textarea.yview)
textarea.pack()

welcome()
title.mainloop()