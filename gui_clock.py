import tkinter as tk
from tkinter import ttk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    day_label.config(text=datetime.now().strftime('%A'))
    time_label.after(1000, update_time)

# Set up the GUI window
root = tk.Tk() 
root.resizable(False,False)
root.title("GUI Clock")
root.geometry('500x400')

# label to display the time
time_label = ttk.Label(root, font="Bahnschrift 25", background="lightblue")
time_label.pack(side="top")

day_label = ttk.Label(root, font="Bahnschrift 10")
# Place the day_label at the top right corner


day_label.place(x=430, y=0)

update_time()

root.mainloop() 