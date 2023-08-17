from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [str(choice(numbers)) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    username = username_entry.get().lower()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    complete = len(website) != 0 and len(username) != 0 and len(password) != 0
    if not complete:
        messagebox.showinfo(title="Incomplete", message="Please complete all fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # read old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  # update old data with new data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # save updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter a website to search.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"The website {website.title()} was not found.")
        else:
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title=website.title(), message=f"Username: {username}\n Password: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"The website {website.title()} was not found.")


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

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_btn = Button(text="Search", command=search, width=13)
search_btn.grid(column=2, row=1)

username_label = Label(text="Email/Username:", anchor="e", width=17)
username_label.grid(column=0, row=2)

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "kaitlyn@email.com")


password_label = Label(text="Password:", anchor="e", width=17)
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=38, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
