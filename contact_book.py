import tkinter as tk
from tkinter import messagebox

contacts = {}


def refresh_contact_list():
    contact_list.delete(0, tk.END)

    for name in contacts:
        contact_list.insert(tk.END, name)


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Missing details", "Please fill in every field.")
        return

    if name in contacts:
        messagebox.showwarning("Already exists", "This contact already exists.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    refresh_contact_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully!")


def search_contact():
    name = name_entry.get().strip()

    if name in contacts:
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        phone_entry.insert(0, contacts[name]["phone"])
        email_entry.insert(0, contacts[name]["email"])

        messagebox.showinfo("Found", "Contact found!")
    else:
        messagebox.showwarning("Not found", "Contact does not exist.")


def delete_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning("Select contact", "Please select a contact to delete.")
        return

    name = contact_list.get(selected[0])
    del contacts[name]

    refresh_contact_list()
    clear_fields()
    messagebox.showinfo("Deleted", "Contact deleted successfully!")


def select_contact(event):
    selected = contact_list.curselection()

    if selected:
        name = contact_list.get(selected[0])

        clear_fields()
        name_entry.insert(0, name)
        phone_entry.insert(0, contacts[name]["phone"])
        email_entry.insert(0, contacts[name]["email"])


# Main window
window = tk.Tk()
window.title("Contact Book")
window.geometry("400x420")

# Labels and input boxes
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window, width=35)
name_entry.pack()

tk.Label(window, text="Phone Number").pack()
phone_entry = tk.Entry(window, width=35)
phone_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window, width=35)
email_entry.pack()

# Buttons
tk.Button(window, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(window, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(window, text="Delete Selected Contact", command=delete_contact).pack(pady=5)

# Contact lists
tk.Label(window, text="Saved Contacts").pack(pady=10)

contact_list = tk.Listbox(window, width=45, height=10)
contact_list.pack()

contact_list.bind("<<ListboxSelect>>", select_contact)

window.mainloop()
