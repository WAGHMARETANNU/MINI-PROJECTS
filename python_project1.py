import os
import shutil
from tkinter import *
from tkinter import filedialog
from collections import Counter

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_label.config(text=f"Selected folder: {folder_path}")

def arrange_files():
    option = option_var.get()
    if option == "Datewise":
        arrange_datewise()
    elif option == "Typewise":
        arrange_typewise()
    elif option == "Alphabetically":
        arrange_alphabetically()
    elif option == "Count files":
        count_files()

def arrange_datewise():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            creation_date = os.path.getctime(file_path)
            date_folder = os.path.join(folder_path, str(creation_date))
            if not os.path.exists(date_folder):
                os.makedirs(date_folder)
            shutil.move(file_path, date_folder)

def arrange_typewise():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_type = os.path.splitext(filename)[1][1:]
            type_folder = os.path.join(folder_path, file_type)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            shutil.move(file_path, type_folder)

def arrange_alphabetically():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            first_letter = filename[0].upper()
            letter_folder = os.path.join(folder_path, first_letter)
            if not os.path.exists(letter_folder):
                os.makedirs(letter_folder)
            shutil.move(file_path, letter_folder)

def count_files():
    file_counts = Counter(os.listdir(folder_path))
    result_text.delete("1.0", END)
    result_text.insert(END, f"Number of files in the folder: {len(file_counts)}\n\n")
    for filename, count in file_counts.items():
        result_text.insert(END, f"{filename}: {count}\n")

root = Tk()
root.title("File Manager")

folder_label = Label(root, text="No folder selected")
folder_label.pack(pady=10)

select_button = Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

option_var = StringVar(root)
option_var.set("Datewise")
option_menu = OptionMenu(root, option_var, "Datewise", "Typewise", "Alphabetically", "Count files")
option_menu.pack(pady=10)

arrange_button = Button(root, text="Arrange Files", command=arrange_files)
arrange_button.pack(pady=10)

result_text = Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()












