from tkinter import *

root = Tk()
root.title("Autoslect/Search")
root.geometry("500x300")

my_label = Label(root, text="Start Typing...", font=("Helvetica", 14),fg="grey")
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()
my_list = Listbox(root, font=("Helvetica", 20), fg="gray",width=30)
my_list.pack(pady=40)

def update(data):
    my_list.delete(0, END)
    for item in data:
        my_list.insert(END, item)

def fillout(event):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ACTIVE))

def check(e):
    typed = my_entry.get()
    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)



toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra cheese", "Black olives", "Green peppers", "Pineapple", "Spinach"]

update(toppings)
my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>", check)
root.mainloop()