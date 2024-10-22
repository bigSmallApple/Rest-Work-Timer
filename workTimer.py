import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def show_popup(title, message, callback):
    # Create a new top-level window
    popup = tk.Toplevel()
    popup.title(title)
    popup.attributes('-topmost', True)  # Ensure the window is on top
    popup.geometry("300x100")  # Set the size of the window
    popup.configure(bg='#F0F0F0')

    # Center the popup on the screen
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")

    # Display the message
    msg_label = tk.Label(popup, text=message, font=('Helvetica', 12), bg='#F0F0F0')
    msg_label.pack(expand=True, pady=20)

    # Define what happens when the popup is closed
    def on_close():
        popup.destroy()
        if callback:
            callback()

    # Add an OK button to close the popup
    ok_button = tk.Button(popup, text="OK", command=on_close, width=10)
    ok_button.pack(pady=5)

    # Bind the window close event to on_close
    popup.protocol("WM_DELETE_WINDOW", on_close)

    # Play a bell sound
    root.bell()

def start_timer():
    global is_running, is_paused, current_duration, total_duration, mode
    try:
        work_duration = max(1, round(float(work_entry.get()) * 60))
        rest_duration = max(1, round(float(rest_entry.get()) * 60))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for work and rest times.")
        return

    is_running = True
    is_paused = False
    mode = 'WORK'
    current_duration = work_duration
    total_duration = work_duration
    status_label.config(text=mode)
    start_button.config(text="Stop Timer")
    update_timer()

def update_timer():
    global current_duration, is_running, is_paused, mode, total_duration
    if is_running and not is_paused:
        sec = int(current_duration % 60)
        min = int((current_duration // 60) % 60)
        hour = int(current_duration // 3600)
        timer_label.config(text=f"{hour:02}:{min:02}:{sec:02}")
        # Update the progress bar
        progress['value'] = ((total_duration - current_duration) / total_duration) * 100

        if current_duration > 0:
            current_duration -= 1
            root.after(1000, update_timer)
        else:
            # Time's up
            def after_popup():
                if is_running:
                    switch_mode()
            show_popup("Timer Done", f"{mode} time is over!", after_popup)
    elif is_running and is_paused:
        # If paused, schedule the update_timer to check again in 1 second
        root.after(1000, update_timer)
    else:
        # Timer stopped
        reset_ui()

def switch_mode():
    global mode, current_duration, total_duration
    if mode == 'WORK':
        mode = 'REST'
        status_label.config(text=mode)
        try:
            current_duration = max(1, round(float(rest_entry.get()) * 60))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for rest time.")
            stop_timer()
            return
        total_duration = current_duration
        if current_duration > 0 and is_running:
            root.after(1000, update_timer)
        else:
            stop_timer()
    elif mode == 'REST':
        mode = 'WORK'
        status_label.config(text=mode)
        try:
            current_duration = max(1, round(float(work_entry.get()) * 60))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for work time.")
            stop_timer()
            return
        total_duration = current_duration
        if current_duration > 0 and is_running:
            root.after(1000, update_timer)
        else:
            stop_timer()

def start_stop_timer():
    global is_running
    if not is_running:
        start_timer()
    else:
        stop_timer()

def pause_timer():
    global is_paused
    if is_running:
        is_paused = not is_paused
        pause_button.config(text="Resume Timer" if is_paused else "Pause Timer")

def stop_timer():
    global is_running, is_paused
    is_running = False
    is_paused = False
    reset_ui()

def reset_ui():
    timer_label.config(text="00:00:00")
    status_label.config(text="")
    progress['value'] = 0
    pause_button.config(text="Pause Timer")
    start_button.config(text="Start Timer")

# Set up the main application window
root = tk.Tk()
root.title("Work/Rest Timer")

# Initialize variables
is_running = False
is_paused = False
current_duration = 0
total_duration = 0
mode = 'WORK'  # or 'REST'

# Create and place GUI components
default_font = ('Helvetica', 12)
timer_font = ('Helvetica', 36, 'bold')

root.configure(bg='#F0F0F0')

tk.Label(root, text="Work (minutes):", font=default_font, bg='#F0F0F0').grid(row=0, column=0, padx=5, pady=5, sticky='e')
work_entry = tk.Entry(root, font=default_font)
work_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Rest (minutes):", font=default_font, bg='#F0F0F0').grid(row=1, column=0, padx=5, pady=5, sticky='e')
rest_entry = tk.Entry(root, font=default_font)
rest_entry.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start Timer", font=default_font, command=start_stop_timer, width=12)
start_button.grid(row=2, column=0, padx=5, pady=5)

pause_button = tk.Button(root, text="Pause Timer", font=default_font, command=pause_timer, width=12)
pause_button.grid(row=2, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="", font=('Helvetica', 16), bg='#F0F0F0')
status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

timer_label = tk.Label(root, text="00:00:00", font=timer_font, bg='#F0F0F0')
timer_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

progress = ttk.Progressbar(root, orient='horizontal', length=250, mode='determinate')
progress.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
