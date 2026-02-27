import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
         website:{"email":email, "password":password

         } }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
        except JSONDecodeError or FileNotFoundError:
            with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file,indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
def find_password():
    w=website_entry.get().title()
    try:
        r=json.load(open("data.json","r"))
        for i in r:
            if i==w:
                messagebox.showinfo(
                    title="Password",
                    message=f"Email for the website {w}: {r[i]['email']}\nPassword: {r[i]['password']}"
                )
                break
                 #   The above break statement is only triggered when the condition is True, otherwise it isnt triggered
                    #This is how a break statement works inside an if clause
        # The reason why we are using the else clause outside the for loop and not inside is because,The break statement is only triggered when the cond is TRUE
        # So if you had putten an else clause inside the for loop, then while itterating, if any itteration condition was False then the else clause would be triggered
        # This would lead to multiple executioning of the else clause
        else:
            messagebox.showinfo(title="Oops",message="No such website exists in the file.")


    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No such file.")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=32)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",command=find_password,width=12)
search_button.grid(row=1, column=2)

window.mainloop()
