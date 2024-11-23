import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def organize_files_by_extension(directory):
    all_items = os.listdir(directory)
    for item in all_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            continue
        file_extension = os.path.splitext(item)[1][1:]
        if not file_extension:
            file_extension = 'no_extension'
        new_dir = os.path.join(directory, file_extension)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        os.rename(item_path, os.path.join(new_dir, item))

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files_by_extension(directory)
        messagebox.showinfo("Success", f"Files in '{directory}' have been organized by extension.")
    else:
        messagebox.showwarning("Warning", "No directory selected!")


root = tk.Tk()
root.title("File Organizer")


window_width = 400
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")


title_label = ttk.Label(frame, text="File Organizer", font=("Helvetica", 18))
title_label.grid(row=0, column=0, pady=(0, 10))


desc_label = ttk.Label(frame, text="Organize files in a directory based on their file extensions.")
desc_label.grid(row=1, column=0, pady=(0, 20))


select_button = ttk.Button(frame, text="Select Directory to Organize", command=select_directory)
select_button.grid(row=2, column=0, pady=10)


status_bar = ttk.Label(root, text="Select a directory to start organizing", relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(row=1, column=0, sticky="we")

root.mainloop()
