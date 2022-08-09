from tkinter import *
from tkinter import messagebox
from pass_gen import PassGen
import json


# ------------------------ CONSTANTS AND PASSWORD GENERATOR ------------------
FONT_NAME = "arial"
FONT_SIZE = 8
PASS_SIZE_FONT_SIZE = 12
generator = PassGen(size=12)

# ----------------------- SAVING DATA ON TEXT FILE ------------------


def get_data():
    website = web_entry.get()
    user_email = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": user_email,
            "password": password
        }
    }

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You left empty fields!")
    else:
        is_ok = messagebox.askokcancel(title="Data Confirmation", message=f"\nWebsite: {website}\n"
                                                                          f"User: {user_email}\n"
                                                                          f"Password: {password}\n"
                                                                          f"Press 'OK' to confirm.")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


def new_rand_pass():
    new_pass_size = get_pass_size()
    pass_entry.delete(0, END)
    new_gen = PassGen(size=new_pass_size)
    new_pass = new_gen.password
    pass_entry.insert(0, new_pass)


def get_pass_size():
    size = int(pass_size.get())
    return size


def search_website():
    try:
        with open("data.json", mode="r") as web_file:
            web_data = json.load(web_file)
    except FileNotFoundError:
        messagebox.showwarning("No Data", message="No Data File Yet")
    else:
        web_to_search = web_entry.get()
        try:
            web_data[web_to_search]
        except KeyError:
            messagebox.showwarning(title="Error", message="No website in database.")
        else:
            searched_user = web_data[web_to_search]["email"]
            searched_pass = web_data[web_to_search]["password"]
            found_message = f"Website: {web_to_search}\n" \
                            f"User: {searched_user}\n" \
                            f"Password: {searched_pass}"
            messagebox.showinfo(title="Data Found", message=found_message)

# ------------------------ SETTING UI -------------------------------


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=2)

# ----------------------- LABELS ------------------------------------
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_label.grid(row=2, column=1)

email_user_label = Label(text="Username/e-mail:", font=(FONT_NAME, FONT_SIZE))
email_user_label.grid(row=3, column=1)

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_label.grid(row=4, column=1)

pass_size_label = Label(text="Password Size:", font=(FONT_NAME, PASS_SIZE_FONT_SIZE))
pass_size_label.grid(row=1, column=2)

# ----------------------- BUTTONS ------------------------------------
add_button = Button(text="Add", font=(FONT_NAME, FONT_SIZE), width=50, command=get_data)
add_button.grid(row=5, column=2, columnspan=2)

generate_button = Button(text="Generate Password", font=(FONT_NAME, FONT_SIZE), command=new_rand_pass)
generate_button.grid(row=4, column=3)

search_button = Button(text="Search", font=(FONT_NAME, FONT_SIZE), width=16, command=search_website)
search_button.grid(row=2, column=3)

# ----------------------- SLIDER -------------------------------------
pass_size = Scale(from_=8, to=20, orient=HORIZONTAL)
pass_size.grid(row=1, column=3)

# ----------------------- ENTRIES ------------------------------------
web_entry = Entry(width=32)
web_entry.grid(row=2, column=2)
web_entry.focus()

user_entry = Entry(width=50)
user_entry.grid(row=3, column=2, columnspan=2)
user_entry.insert(0, "user@gmail.com")

pass_entry = Entry(width=33)
pass_entry.insert(0, generator.password)
pass_entry.grid(row=4, column=2)


window.mainloop()
