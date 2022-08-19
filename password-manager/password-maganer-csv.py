import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pyperclip
import random

senha_pred = 1234
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Login():
    def __init__(self):
        self.window = tk.Tk()  # ativa a classe tkinter dentro da classe login
        self.window.title("Login Manager")
        self.window.config(padx=50, pady=20)

        self.canvas()
        self.labels()
        self.entries()
        self.buttons(self.window)

        # SEGUNDA JANELA

    def canvas(self):
        self.locker_icon = tk.Canvas(self.window, width=200, height=205)
        self.locker_icon_img = tk.PhotoImage(file="logo.png")
        self.locker_icon.create_image(100, 100, image=self.locker_icon_img)
        self.locker_icon.grid(column=1, row=0)

    def labels(self):
        self.website = tk.Label(self.window, text="Website:")
        self.website.grid(column=0, row=1)
        self.email_username = tk.Label(self.window, text="Email/Username:")
        self.email_username.grid(column=0, row=2)
        self.password = tk.Label(self.window, text="Password:")
        self.password.grid(column=0, row=3)


    def entries(self):
        self.website_entry = tk.Entry(self.window, width=35)
        self.website_entry.grid(column=1, row=1)
        self.website_entry.focus()
        self.email_username_entry = tk.Entry(self.window, width=35)
        self.email_username_entry.grid(column=1, row=2)
        self.email_username_entry.insert(0, "rrlc@ic.ufal.br")
        self.password_entry = tk.Entry(self.window, width=35)
        self.password_entry.grid(column=1, row=3)

    def buttons(self, window):
        self.add_button = tk.Button(self.window, text="Save Password", width=33, command=self.add_password)
        self.add_button.grid(column=1, row=4)

        self.password_generator = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.password_generator.grid(column=2, row=3)

        self.search_button = tk.Button(self.window, text="Search",command=self.search)
        self.exit_button = tk.Button(self.window, text="Quit", command=self.window.destroy).grid(column=2, row=4)

    #BUTTON FUNCTIONS
    def search(self):
        pass

    def generate_password(self):
        # DELETE PREVIOUS PASSWORD
        self.password_entry.delete(0, tk.END)

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for char in range(nr_letters):
            password_list.append(random.choice(letters))

        for char in range(nr_symbols):
            password_list += random.choice(symbols)

        for char in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        generated_password = ""
        for char in password_list:
            generated_password += char
        self.password_entry.insert(0, generated_password)

        pyperclip.copy(generated_password)

    def add_password(self):
        info_doc = pd.read_csv("logins.csv", index_col=0)
        value_website = self.website_entry.get()
        value_email_username = self.email_username_entry.get()
        value_password = self.password_entry.get()

        if value_password == "" and value_website == "" and value_email_username == "":  # POP-UP
            messagebox.showinfo(title="Invalid Input", message="Insert the data")
        elif value_password == "":
            messagebox.showinfo(title="Invalid Input", message="Missing the password")
        elif value_website == "":
            messagebox.showinfo(title="Invalid Input", message="Missing the Website")
        elif value_email_username == "":
            messagebox.showinfo(title="Invalid Input", message="Missing the Email/Username")
        else:
            confirmation = messagebox.askokcancel(title=value_website, message="SAVE DATA?")  # POP-UP
            if confirmation:
                new_data = pd.DataFrame(
                    {"website_csv": [value_website],
                     "email/username_csv": [value_email_username],
                     "password_csv": [value_password]
                     })
                updated_data = pd.concat([info_doc, new_data])
                updated_data.to_csv('logins.csv')  # replace csv
                self.website_entry.delete(0, tk.END)  # delete the existing text
                self.password_entry.delete(0, tk.END)


if __name__ == "__main__":
    login1 = Login()
    login1.window.mainloop()
