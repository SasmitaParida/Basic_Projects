# Import required libraries
import tkinter as Tk
import time
from tkinter import messagebox

# Define the function to set the alarm
def actual_time():
    set_alarm_time = f"{hourTime.get()}:{minTime.get()}:{secTime.get()}"
    while True:
        # Get the current time
        time.sleep(1)
        current_time = time.strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        if current_time == set_alarm_time:
            # Show a message box when the alarm time is reached
            messagebox.showinfo("Alarm", "Time to wake up!")
            break

# Initialize the Tkinter window
clock = Tk.Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
clock.configure(bg='#FFC0CB')  # Setting a pink background color

# Time format heading
time_format = Tk.Label(clock, text="Enter time in 24-hour format!", fg="white", bg="#FF69B4", font=("Arial", 15))
time_format.place(x=60, y=20)

# Label for input fields
addTime = Tk.Label(clock, text="Hour    Min    Sec", fg="white", bg="#FF69B4", font=("Arial", 12))
addTime.place(x=140, y=50)

# "Set your alarm" label
setYourAlarm = Tk.Label(clock, text="When to wake you up", fg="white", bg="#FF69B4", relief="solid", font=("Arial", 13, "bold"))
setYourAlarm.place(x=120, y=80)

# Variables to take user input
hourTime = Tk.StringVar()
minTime = Tk.StringVar()
secTime = Tk.StringVar()

# Creating input boxes for hours, minutes, and seconds
hourEntry = Tk.Entry(clock, textvariable=hourTime, bg="white", width=4, font=("Arial", 12))
hourEntry.place(x=140, y=120)

minEntry = Tk.Entry(clock, textvariable=minTime, bg="white", width=4, font=("Arial", 12))
minEntry.place(x=190, y=120)

secEntry = Tk.Entry(clock, textvariable=secTime, bg="white", width=4, font=("Arial", 12))
secEntry.place(x=240, y=120)

# Button to set the alarm
submit = Tk.Button(clock, text="Set Alarm", fg="white", bg="#FF69B4", width=10, command=actual_time, font=("Arial", 12))
submit.place(x=150, y=160)

# Start the Tkinter loop to run the clock window
clock.mainloop()
