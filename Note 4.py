from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msb

window = Tk()
window.title("Combo Box Demo")
window.geometry('400x350')

books = {
    'Harry Potter': ['J.K. Rowling', 450, 10.00],
    'The Lord of the Rings': ['J.R.R. Tolkien', 600, 15.00],
    'The Hunger Games': ['Suzanne Collins', 350, 12.00],
    'Twilight': ['Stephenie Meyer', 400, 12.00],
    'The Da Vinci Code': ['Dan Brown', 500, 12.00]
}
selected_index = 0

def lst_books_selected(event):
    global selected_index
    try:
        selected_index = lst_books.curselection()[0]
        book_name = lst_books.get(selected_index)
        book_author = books[book_name][0]
        set_text(txt_author, book_author)
        book_pages = books[book_name][1]
        set_text(txt_pages, book_pages)
        book_price = books[book_name][2]
        set_text(txt_price, book_price)

        payment = calculate_payment(book_price)
        lbl_payment.configure(text=f'Payment: ${payment:.2f}')
    except IndexError:
        msb.showerror("Error", "Please select a book")

def calculate_payment(book_price):
    quantity = txt_quantity.get()
    payment = book_price * int(quantity)

    if cbb_shipmode.get() == 'Now ($5)':
        payment += 5
    elif cbb_shipmode.get() == 'Express ($2)':
        payment += 2
    else:
        payment += 1  
    
    if cover_var.get():
        payment += 1
    if card_var.get():
        payment += 2

    return payment

def set_text(txt_ui, text):
    txt_ui.configure(state='normal')
    txt_ui.delete(0, END)
    txt_ui.insert(0, text)
    txt_ui.configure(state='readonly')

def extra_selected():
    book_price = float(txt_price.get())
    payment = calculate_payment(book_price)
    lbl_payment.configure(text=f'Payment: ${payment:.2f}')

lbl_books = Label(window, text="Books:")
lbl_books.grid(row=0, column=0, sticky=W, padx=5, pady=5)

lst_books = Listbox(window, width=20, height=10)
lst_books.grid(row=1, column=0, rowspan=5, columnspan=2, padx=5, pady=5)
lst_books.insert(END, *books)
lst_books.bind('<<ListboxSelect>>', lst_books_selected)

lbl_author = Label(window, text="Author:")
lbl_author.grid(row=0, column=2, sticky=W, padx=5, pady=5)

txt_author = Entry(window, width=15)
txt_author.grid(row=1, column=2, sticky=W+N, padx=5)

lbl_pages = Label(window, text="Pages:")
lbl_pages.grid(row=2, column=2, sticky=W, padx=5)

txt_pages = Entry(window, width=15)
txt_pages.grid(row=3, column=2, sticky=W+N, padx=5)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=4, column=2, sticky=W, padx=5)

txt_price = Entry(window, width=15)
txt_price.grid(row=5, column=2, sticky=W+N, padx=5)

lbl_payment = Label(window, text="Payment: $0")
lbl_payment.grid(row=6, column=2, sticky=W, padx=5)

lbl_quantity = Label(window, text="Quantity:")
lbl_quantity.grid(row=6, column=0, sticky=W, padx=5)

quantity_var = IntVar()
quantity_var.set(1)
txt_quantity = Entry(window, width=5, textvariable=quantity_var)
txt_quantity.grid(row=6, column=1, sticky=E, padx=5)

lbl_shipmode = Label(window, text="Ship Mode:")
lbl_shipmode.grid(row=7, column=0, sticky=W, padx=5)

cbb_shipmode = Combobox(window, width=10, state='readonly')
cbb_shipmode['values'] = ['Standard ($1)', 'Express ($2)', 'Now ($5)']
cbb_shipmode.current(0)
cbb_shipmode.grid(row=7, column=1, sticky=E, padx=5)

lbl_extra = Label(window, text="Extra:")
lbl_extra.grid(row=8, column=0, sticky=W, padx=5)

cover_var = BooleanVar()
cb_cover = Checkbutton(window, text="Cover ($1)", variable=cover_var, command=extra_selected)
cb_cover.grid(row=9, column=0, columnspan=2, sticky=W, padx=5)

card_var = BooleanVar()
cb_greeting_card = Checkbutton(window, text="Greeting Card ($2)", variable=card_var, command=extra_selected)
cb_greeting_card.grid(row=10, column=0, columnspan=2, sticky=W, padx=5)

def buy_button_clicked():
    try:
        book_price = float(txt_price.get())
        payment = calculate_payment(book_price)
        msb.showinfo("Purchase", f"Total payment: ${payment:.2f}")
    except ValueError:
        msb.showerror("Error", "Invalid price")

btn_buy = Button(window, text="Buy", command=buy_button_clicked)
btn_buy.grid(row=11, column=0, columnspan=2, sticky=W, padx=5)

window.mainloop()