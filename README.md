### README for Work/Rest Timer Application

#### Overview
This project is a simple Work/Rest Timer application built using the Tkinter library in Python. It allows users to set work and rest intervals, and it displays the time remaining for each interval. The timer switches automatically between work and rest modes, and a popup notification alerts the user when the time is up.

#### Features:
- **Work/Rest Mode Switching**: The timer automatically switches between work and rest intervals.
- **Progress Bar**: A progress bar visualizes how much time is left in each interval.
- **Pause/Resume Timer**: The user can pause and resume the timer at any time.
- **Popup Notification**: A popup window alerts the user when the work or rest interval is complete.
- **Input Validation**: The application validates the user's input for work and rest durations, ensuring valid numbers are entered.

#### Requirements:
- Python 3.x
- Tkinter (included with Python standard library)
- `ttk` module (included with Tkinter)

#### Setup Instructions:

1. **Install Python**: Ensure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

2. **Run the Application**:
   Save the provided code in a Python file (e.g., `work_rest_timer.py`) and run it:
   ```bash
   python work_rest_timer.py
   ```

#### How to Use:

1. **Set Work and Rest Durations**:
   - In the "Work (minutes)" field, enter the duration for the work interval in minutes.
   - In the "Rest (minutes)" field, enter the duration for the rest interval in minutes.

2. **Start the Timer**:
   - Press the "Start Timer" button to begin the timer. The application will switch between work and rest modes automatically.

3. **Pause/Resume**:
   - You can pause the timer at any time by pressing the "Pause Timer" button. To resume, press the "Resume Timer" button.

4. **Stop the Timer**:
   - To stop the timer, press the "Stop Timer" button, which will reset the timer and UI.

#### Application Components:

1. **Timer Display**:
   - Shows the current time left in the format `HH:MM:SS`.

2. **Progress Bar**:
   - Indicates the percentage of time completed in the current interval (work or rest).

3. **Popup Notifications**:
   - When a work or rest interval is complete, a popup notification informs the user. The user can close the popup to switch to the next mode.

#### Example:
- **Work Interval**: 25 minutes
- **Rest Interval**: 5 minutes
The timer will count down from 25 minutes, show a popup when the work interval is complete, and then switch to the rest interval.
