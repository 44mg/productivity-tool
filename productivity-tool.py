import tkinter as tk
import customtkinter as ctk
import json
import os
import time
BG = "#0A84FF"

running = False

root=ctk.CTk()
root.title("Productivity App")
root.lift()
root.attributes('-topmost', True)

tabview = ctk.CTkTabview(root)
tabview.pack(fill = "both", expand = True, padx = 10, pady = 10)

tabview.add("To Do")
tabview.add("Pomodoro Timer")
listbox = tk.Listbox(tabview.tab("To Do"), relief = "flat", bd = 0)
listbox.pack(fill = "both", expand = True , padx = 10, pady = 10)

entry = ctk.CTkEntry(tabview.tab("To Do"), corner_radius = 10)
entry.pack(fill = "x", padx = 10, pady = 10)

timer_label = ctk.CTkLabel(tabview.tab("Pomodoro Timer"), text = "25:00")
timer_label.pack(fill = "both", expand = True, padx= 10, pady = 10)



def add_task():
    task = entry.get()
    listbox.insert(tk.END, task)
    save_tasks(fill = "x", padx = 10, pady = 10)

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

def tick(minutes, seconds):
    if not running:
        return
    timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
    if minutes == 0 and seconds == 0:
        timer_label.configure(text="Break Time!")
        return
    if seconds == 0:
        seconds = 59
        minutes -= 1
    else:
        seconds -= 1
    root.after(1000, tick, minutes, seconds)

def start_timer():
    global running
    running = True
    tick(25, 0)

def pause_timer():
    global running
    running = False



addtask = ctk.CTkButton(tabview.tab("To Do"), text = "Add Task", command = add_task, fg_color=BG)
addtask.pack(fill = "x", padx = 10, pady = 10)

remtask = ctk.CTkButton(tabview.tab("To Do"), text = "Remove Task", command = rem_task, fg_color=BG)
remtask.pack(fill = "x", padx = 10, pady = 10)

start_btn = ctk.CTkButton(tabview.tab("Pomodoro Timer"), text = "Start", command = start_timer )
start_btn.pack(fill = "x", padx = 10, pady = 10)

pause_btn = ctk.CTkButton(tabview.tab("Pomodoro Timer"), text = "Pause", command = pause_timer)
pause_btn.pack(fill = "x", padx = 10, pady = 10)



root.configure(bg=BG)
load_tasks()
root.mainloop()
