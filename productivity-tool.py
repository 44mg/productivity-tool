import tkinter as tk
import customtkinter as ctk
import json
import os
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

timer_label = ctk.CTkLabel(tabview.tab("Pomodoro Timer"), text = "25:00", font = ("Arial", 48))
timer_label.pack(fill = "both", expand = True, padx= 10, pady = 10)

# todo list functions

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

# pomodoro functions

current_minutes = 25
current_seconds = 0

def tick(minutes, seconds):
    global current_minutes, current_seconds
    if not running:
        return
    current_minutes = minutes
    current_seconds = seconds
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

def toggletimer():
    global running
    if running:
        running = False
        pause_btn.configure(text = "Resume")
    else:
        running = True
        tick(current_minutes, current_seconds)
        pause_btn.configure(text = "Pause")

def reset_timer():
    global running
    running = False
    pause_btn.configure(text = "Pause")
    timer_label.configure(text = "25:00")

# todo list

addtask = ctk.CTkButton(tabview.tab("To Do"), text = "Add Task", command = add_task, fg_color=BG)
addtask.pack(fill = "x", padx = 10, pady = 10)

remtask = ctk.CTkButton(tabview.tab("To Do"), text = "Remove Task", command = rem_task, fg_color=BG)
remtask.pack(fill = "x", padx = 10, pady = 10)

# pomodoro timer

start_btn = ctk.CTkButton(tabview.tab("Pomodoro Timer"), text = "Start", command = start_timer )
start_btn.pack(fill = "x", padx = 10, pady = 10)

pause_btn = ctk.CTkButton(tabview.tab("Pomodoro Timer"), text = "Pause", command = toggletimer)
pause_btn.pack(fill = "x", padx = 10, pady = 10)

reset_btn = ctk.CTkButton(tabview.tab("Pomodoro Timer"),  text = "Reset", command = reset_timer)
reset_btn.pack(fill = "x", padx = 10, pady = 10)



root.configure(fg_color=BG)
load_tasks()
root.mainloop()
