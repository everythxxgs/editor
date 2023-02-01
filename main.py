import tkinter as tk
import time
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

file_path = None
auto_save_interval = 5000 # 5 seconds

def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            text.delete('1.0', tk.END)
            text.insert(tk.END, f.read())

def save_file():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as f:
            f.write(text.get('1.0', tk.END))

def auto_save():
    global file_path
    if file_path:
        with open(file_path, 'w') as f:
            f.write(text.get('1.0', tk.END))
    root.after(auto_save_interval, auto_save) # save every interval

def change_auto_save_interval():
    global auto_save_interval
    interval = simpledialog.askinteger("Auto Save Interval", "Enter the auto save interval (in seconds):", minvalue=1)
    if interval:
        auto_save_interval = interval * 1000
        root.after_cancel(auto_save_timer) # cancel the previous timer
        auto_save_timer = root.after(auto_save_interval, auto_save) # start the new timer

def exit_editor():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill='both')

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

settings_menu = tk.Menu(menu)
menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Auto Save Interval", command=change_auto_save_interval)

auto_save_timer = root.after(auto_save_interval, auto_save) # start the auto-save timer

root.mainloop()
