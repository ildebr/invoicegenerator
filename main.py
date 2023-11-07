import tkinter
from tkinter import ttk, StringVar
import datetime
from second import create_pdf_file


def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, '1')
    desc_entry.delete(0,tkinter.END)
    price_spinbox.delete(0,tkinter.END)
    price_spinbox.insert(0,"0.0")

invoice_list = []
def clear_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    email_entry.delete(0,tkinter.END)

    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()



def add_item():
    print('hi')
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_items = [desc, qty,f'$${price}',line_total]
    

    invoice_list.append(invoice_items)

    tree.insert('', 0, values=invoice_items)

    clear_item()

def generate_invoice():
    name = first_name_entry.get()+last_name_entry.get()

    subtotal = sum(item[3] for item in invoice_list)

    doc_name = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") +'.pdf'

    date_now =datetime.datetime.now().strftime("%Y-%m-%d")

    list = []
    list.append(["Description", "Quantity", "Price", "Total"])
    list.extend(invoice_list)

    create_pdf_file(first_name_entry.get(), last_name_entry.get(),email_entry.get(),ninvoice_entry.get(),date_now, subtotal, list)


window = tkinter.Tk()
window.title('invoice generator')


frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)


header_section_label = tkinter.Label(frame, text="Invoice Header Information")
header_section_label.grid(row=0,column=0)


first_name_label = tkinter.Label(frame, text="First Name")
first_name_label.grid(row=1, column=0)

last_name_label = tkinter.Label(frame, text="Last Name")
last_name_label.grid(row=1, column=1)


first_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=2,column=0)

last_name_entry = tkinter.Entry(frame)
last_name_entry.grid(row=2,column=1)


email_label = tkinter.Label(frame, text="email")
email_label.grid(row=1, column=2)
email_entry = tkinter.Entry(frame)
email_entry.grid(row=2, column=2)


ninvoice_label = tkinter.Label(frame, text='N.° of Invoice')
ninvoice_label.grid(row=3, column=0)
ninvoice_entry = tkinter.Entry(frame)
ninvoice_entry.grid(row=4, column=0)


LANG_OPTIONS = ['EN', 'ES']

variable = StringVar(window)
variable.set(LANG_OPTIONS[0]) # default value

lang_dropdown = tkinter.OptionMenu(frame,variable,*LANG_OPTIONS)
lang_dropdown.grid(row=4,column=1)



invoice_elements_label = tkinter.Label(frame,text='Invoice Elements')
invoice_elements_label.grid(row=5,column=0)


qty_label = tkinter.Label(frame, text="quantity")
qty_label.grid(row=6, column=0)
qty_spinbox = tkinter.Spinbox(frame,from_=1, to=100)
qty_spinbox.grid(row=7, column=0)

desc_label = tkinter.Label(frame, text="Description")
desc_label.grid(row=6, column=1)
desc_entry = tkinter.Entry(frame)
desc_entry.grid(row=7, column=1)

price_label = tkinter.Label(frame, text="Unit Price")
price_label.grid(row=6, column=2)
price_spinbox = tkinter.Spinbox(frame, from_=0.0, to=500, increment=0.5)
price_spinbox.grid(row=7,column=2)

add_item_button = tkinter.Button(frame, text="Add item", command= add_item)
add_item_button.grid(column=1, row=8)

columns = ('desc', 'qty', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Price')
tree.heading('total', text='Total')




tree.grid(row=9, column=0, columnspan=3)


save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
save_invoice_button.grid(row=10, column=0, columnspan=3, sticky="news", padx=20, pady=5)

new_invoice_button = tkinter.Button(frame, text="New Invoice", command=clear_invoice)
new_invoice_button.grid(row=11, column=0, columnspan=3, padx=20, pady=5, sticky="news")





window.mainloop()