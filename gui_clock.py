import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime, timedelta

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    day_label.config(text=datetime.now().strftime('%A'))
    calendar_label.config(text=datetime.now().strftime('%d %B %Y'))
    time_label.after(1000, update_time)

def start_timer():
    global start_time, end_time
    start_time = datetime.now()
    button_timer.config(text="Stop", command=stop_timer)
    end_time = start_time + timedelta(seconds=10)
    update_timer()

def stop_timer():
    start_time=0
    timer_label.config(text="Timer stopped")
    button_timer.config(text="Start")
    timer_label.after_cancel(update_timer)

def update_timer():
    global elapsed_time
    elapsed_time = datetime.now() - start_time
    timer_label.config(text=f"{elapsed_time} seconds")
    timer_label.after(100, update_timer)

#https://stackoverflow.com/questions/19944712/browse-for-file-path-in-python
def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        timer_file_entry.delete(0, tk.END)
        timer_file_entry.insert(0, file_path)


def write_time():
    timer_file=open(timer_file_entry.get(), "w")
    timer_file.write("Start time: " + str(start_time) + "\n"+ "End time: " + str(end_time) + "\n" + "Elapsed time: " + str(elapsed_time))
# Set up the GUI window
root = tk.Tk() 
root.resizable(False,False)
root.title("GUI Clock")
root.geometry('500x400')

# label to display the time
time_label = ttk.Label(root, font="Bahnschrift 25", background="lightblue")
time_label.pack(side="top")

day_label = ttk.Label(root, font="Bahnschrift 10")
day_label.place(x=430, y=0)

calendar_label = ttk.Label(root, font="Bahnschrift 10")
calendar_label.place(x=0, y=0)

# create a timer to update the time every second
timer_label=ttk.Label(root, font="Bahnschrift 10")
timer_label.pack()

# editable field for timer file location
timer_file_entry = ttk.Entry(root, width=50)
timer_file_entry.pack()

# button to choose timer file location
timer_file_button = ttk.Button(root, text="Choose Timer File", command=choose_file)
timer_file_button.pack()

button_timer = ttk.Button(root, text="Start", command=start_timer)
button_timer.pack()

update_time()

root.mainloop()
