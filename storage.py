from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Store Passwords")
root.configure(padx=10, pady=10)

d = open("data.txt", "r")


# create defs
def save():
    global d
    d = open("data.txt", "a")
    d.write(e_mail.get() + " --- ")
    d.write(password.get() + "\n")
    d.close()
    messagebox.showinfo("Store Passwords", "Your E-Mail and Password have been saved!")


def clear():
    e_mail.delete(0, END)
    password.delete(0, END)


def destroy():
    global d
    global button
    result = messagebox.askquestion(title="Wipe", message="Would you like to wipe all passwords saved?", icon="warning")
    if result == 'yes':
        d = open("data.txt", "w")
        d.write("Account    ---     Password \n")
        d.close()
        messagebox.showinfo(title="Wiped", message="Everything's been deleted!", icon="info")
    else:
        messagebox.showinfo(title="Info", message="All files conserved.", icon="info")


# create labels
label1 = Label(root, text="E-Mail")
label2 = Label(root, text="Password")
frame = LabelFrame(root, bd=1, padx=5, pady=5)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
frame.grid(row=3, column=0, columnspan=3, padx=10)

# in frame
button = Button(frame, text="Wipe all saved passwords?", command=destroy)
button.pack()

# create entries
e_mail = Entry(root)
password = Entry(root)

e_mail.grid(row=0, column=1, columnspan=2)
password.grid(row=1, column=1, columnspan=2)

# create buttons
button_save = Button(root, text="Save", command=save)
button_clear = Button(root, text="Clear", command=clear)

button_save.grid(row=2, column=1, pady=5)
button_clear.grid(row=2, column=2, pady=5)

root.mainloop()
