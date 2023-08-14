from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", anchor="e", width=17)
website_label.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username:", anchor="e", width=17)
username_label.grid(column=0, row=2)

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", anchor="e", width=17)
password_label.grid(column=0, row=3)

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=38)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
