import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Create a frame for the Listbox and Scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Create the Listbox widget
        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar widget
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach the scrollbar to the Listbox
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Entry field for new tasks
        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack(pady=10)

        # Add and Remove buttons
        self.button_add = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_remove = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.button_remove.pack(side=tk.LEFT)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
