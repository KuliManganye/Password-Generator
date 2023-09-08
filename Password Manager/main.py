from tkinter import *
from tkinter import messagebox
import random
import json


FONT_NAME = "Courier"
LABEL_FONT = 12


# ------------------------------------------------- PASSWORD GENERATOR -------------------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters for _ in range(nr_letters))]
    password_symbols = [random.choice(symbols for _ in range(nr_symbols))]
    password_numbers = [random.choice(numbers for _ in range(nr_numbers))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# -------------------------------------------------- SAVE PASSWORD ------------------------------------------------ #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all blank fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("dara.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# -------------------------------------------------- FIND PASSWORD ------------------------------------------------ #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Bo Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------------------------------- UI SETUP --------------------------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create a website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Create a website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


# Create an email/username label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Create a email/username entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kulimanganye@gmail.com")


#Create a password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create a password entry
password_entry = Entry(width=16)
password_entry.grid(column=1, row=3, columnspan=1)


# Create a generate password button:
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)


# Create an add button:
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)


# Create a search button:
search_button = Button(text="Search", width=10)
search_button.grid(column=3, row=1)


window.mainloop()

