import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize contacts data
        self.contacts = self.load_contacts()

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets

        # Entry fields for contact details
        self.label_name = tk.Label(self.root, text="Name")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = tk.Label(self.root, text="Phone")
        self.label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(self.root, width=30)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.root, width=30)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address = tk.Label(self.root, text="Address")
        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root, width=30)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for operations
        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, padx=10, pady=5)

        self.button_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=4, column=1, padx=10, pady=5)

        self.button_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.button_search.grid(row=5, column=0, padx=10, pady=5)

        self.button_update = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.button_update.grid(row=5, column=1, padx=10, pady=5)

        self.button_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=6, column=0, padx=10, pady=5)

        self.button_load = tk.Button(self.root, text="Load Contacts", command=self.load_contacts)
        self.button_load.grid(row=6, column=1, padx=10, pady=5)

    def load_contacts(self):
        """Load contacts from a JSON file."""
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """Add a new contact to the contact book."""
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def view_contacts(self):
        """Display all contacts in a messagebox."""
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts found.")
            return

        contact_list = "\n".join([f"{name}: {info['phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        """Search for a contact by name."""
        name = self.entry_name.get()
        if name in self.contacts:
            info = self.contacts[name]
            contact_info = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info.get('email', 'N/A')}\nAddress: {info.get('address', 'N/A')}"
            messagebox.showinfo("Contact Found", contact_info)
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def update_contact(self):
        """Update an existing contact."""
        name = self.entry_name.get()
        if name in self.contacts:
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()

            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        """Delete a contact."""
        name = self.entry_name.get()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def clear_entries(self):
        """Clear input fields."""
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
