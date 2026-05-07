import tkinter as tk
import customtkinter as ctk
import json
import os
BG = "#0A84FF"

root=ctk.CTk()
root.title("To do list")
root.lift()
root.attributes('-topmost', True)
listbox = tk.Listbox(root, relief = "flat", bd = 0)
listbox.pack(fill = "both", expand = True , padx = 10, pady = 10)

entry = ctk.CTkEntry(root, corner_radius = 10)
entry.pack(fill = "x", padx = 10, pady = 10)

def add_task():
    task = entry.get()
    listbox.insert(tk.END, task)
    save_tasks()

def rem_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    save_tasks()

def save_tasks():
    tasks = list(listbox.get(0, tk.END))
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open ("tasks.json") as f:
            tasks = json.load(f)
            for task in tasks:
                listbox.insert(tk.END, task)

addtask = ctk.CTkButton(root, text = "Add Task", command = add_task, fg_color=BG)
addtask.pack(fill = "x", padx = 10, pady = 10)

remtask = ctk.CTkButton(root, text = "Remove Task", command = rem_task, fg_color=BG)
remtask.pack(fill = "x", padx = 10, pady = 10)

root.configure(bg=BG)
load_tasks()
root.mainloop()
