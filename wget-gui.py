import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from PIL import Image, ImageTk  # Importing Pillow for handling images
import os
import subprocess
import shlex

def change_directory():
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        dir_label.config(text=f"Current Directory: {directory}")

def submit():
    filename = entry_filename.get()
    url = text_url.get("1.0", tk.END).strip()

    if filename and url:
        quoted_filename = shlex.quote(filename)
        quoted_url = shlex.quote(url.replace('&', '^&'))
        command = f'wsl wget -O {quoted_filename} {quoted_url}'
        subprocess.Popen(["start", "cmd", "/c", command], shell=True)

root = tk.Tk()
root.title("Wget GUI")
root.resizable(True, True)

# Set the style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

# Load and set the logo
logo_path = "wget-cover.ico"  # Replace with the path to your logo file
logo_image = Image.open(logo_path)
logo_photo = ImageTk.PhotoImage(logo_image)
root.iconphoto(False, logo_photo)  # Set window icon

# Configure grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Create and place the labels and entry widgets
ttk.Label(root, text="Nama File").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_filename = ttk.Entry(root, width=50)
entry_filename.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

ttk.Label(root, text="URL").grid(row=1, column=0, padx=10, pady=5, sticky="ne")
text_url = scrolledtext.ScrolledText(root, width=50, height=4, font=("Arial", 12))
text_url.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

# Create and place the change directory button
dir_label = ttk.Label(root, text=f"Current Directory: {os.getcwd()}")
dir_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

btn_change_dir = ttk.Button(root, text="Change Directory", command=change_directory)
btn_change_dir.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Create and place the submit button
btn_submit = ttk.Button(root, text="Submit", command=submit)
btn_submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Set the position of the window to the center of the screen
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"+{center_x}+{center_y}")

root.mainloop()
