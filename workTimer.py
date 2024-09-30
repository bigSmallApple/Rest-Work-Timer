import time
import tkinter as tk
from tkinter import messagebox
import threading

# Global variables for controlling the timer state
is_paused = False
is_running = False
timer_thread = None

def play_beep(a):
    for _ in range(a):
        time.sleep(0.25)
        print("\a")  # This will work in some terminal environments

def update_timer(label, duration):
    global is_paused, is_running
    while duration > 0 and is_running:
        if not is_paused:
            sec = duration % 60
            min = (duration // 60) % 60
            hour = duration // 3600
            label.config(text=f"{hour:02}:{min:02}:{sec:02}")
            label.update()
            time.sleep(1)
            duration -= 1
    if duration == 0 and is_running:
        play_beep(4)

def start_timer():
    global is_paused, is_running
    try:
        work_duration = int(work_entry.get()) * 60
        rest_duration = int(rest_entry.get()) * 60
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for work and rest times.")
        stop_timer()  # Reset timer if input is invalid
        return

    is_running = True
    is_paused = False

    while is_running:
        # Work timer
        status_label.config(text="WORK")
        update_timer(timer_label, work_duration)

        # If stopped during work, break out of the loop
        if not is_running:
            break

        # Rest timer
        status_label.config(text="REST")
        update_timer(timer_label, rest_duration)

        # If stopped during rest, break out of the loop
        if not is_running:
            break

def start_stop_timer():
    global timer_thread, is_running

    if not is_running:
        # Start the timer
        is_running = True
        start_button.config(text="Stop Timer")
        timer_thread = threading.Thread(target=start_timer)
        timer_thread.start()
    else:
        # Stop the timer
        stop_timer()

def pause_timer():
    global is_paused
    is_paused = not is_paused  # Toggle pause state
    if is_paused:
        pause_button.config(text="Resume Timer")
    else:
        pause_button.config(text="Pause Timer")

def stop_timer():
    global is_running, is_paused
    is_running = False
    is_paused = False
    timer_label.config(text="00:00:00")
    status_label.config(text="")
    pause_button.config(text="Pause Timer")
    start_button.config(text="Start Timer")

# Set up the main application window
root = tk.Tk()
root.title("Work/Rest Timer")

# Create and place GUI components
tk.Label(root, text="Work (minutes):").grid(row=0, column=0)
work_entry = tk.Entry(root)
work_entry.grid(row=0, column=1)

tk.Label(root, text="Rest (minutes):").grid(row=1, column=0)
rest_entry = tk.Entry(root)
rest_entry.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Timer", command=start_stop_timer)
start_button.grid(row=2, column=0)

pause_button = tk.Button(root, text="Pause Timer", command=pause_timer)
pause_button.grid(row=2, column=1)

status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.grid(row=3, column=0, columnspan=2)

timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
timer_label.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
