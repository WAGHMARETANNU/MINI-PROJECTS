import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Management Tool")
        self.root.geometry("500x400")
        self.root.configure(bg="white")  # White background color

        self.current_path = tk.StringVar()
        self.current_path.set("")

        self.path_label = tk.Label(root, textvariable=self.current_path, wraplength=480, fg="red", bg="white", font=("Arial", 18, "italic"))
        self.path_label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse Folder", command=self.browse_folder, fg="red", bg="white", font=("Arial", 14, "italic"), relief=tk.FLAT)
        self.browse_button.pack(pady=5)

        self.sort_by_label = tk.Label(root, text="Sort by:", fg="red", bg="white", font=("Arial", 14, "italic"))
        self.sort_by_label.pack()

        self.sort_by_variable = tk.StringVar()
        self.sort_by_variable.set("Date")

        self.sort_by_optionmenu = tk.OptionMenu(root, self.sort_by_variable, "Date", "Alphabetically", "Type")
        self.sort_by_optionmenu.configure(fg="red", bg="white", activeforeground="red", activebackground="white", highlightbackground="white", font=("Arial", 14, "italic"))
        self.sort_by_optionmenu.pack()

        self.file_listbox = tk.Listbox(root, width=60, height=15, fg="red", bg="white", selectbackground="lightgray", font=("Arial", 14, "italic"))
        self.file_listbox.pack()

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_list, fg="red", bg="white", font=("Arial", 14, "italic"), relief=tk.FLAT)
        self.refresh_button.pack(pady=5)

        self.animate_objects()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.current_path.set(folder_path)
            self.refresh_list()

    def refresh_list(self):
        self.file_listbox.delete(0, tk.END)
        if not self.current_path.get():
            messagebox.showerror("Error", "Please select a folder.")
            return

        files = os.listdir(self.current_path.get())
        sort_option = self.sort_by_variable.get()
        if sort_option == "Date":
            files.sort(key=lambda x: os.path.getmtime(os.path.join(self.current_path.get(), x)))
        elif sort_option == "Alphabetically":
            files.sort()
        elif sort_option == "Type":
            files.sort(key=lambda x: os.path.splitext(x)[1])

        for file in files:
            self.file_listbox.insert(tk.END, file)

    def animate_objects(self):
        # Add animation or lively objects here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="white")
    app = FileManagementApp(root)
    root.mainloop()
