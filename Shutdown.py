import tkinter as tk
from tkinter import *
import subprocess
import os


def shutdown():
    return os.system("shutdown /s /t 1")

def shutdown_scheduled(seconds=0):
    command = ["shutdown", "/s", "/t", str(seconds)]
    print(f"Executing command: {command}")
    return subprocess.run(command, shell=True)

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

def show_scheduled_shutdown_window():
    scheduled_shutdown_window = tk.Toplevel(gui)
    scheduled_shutdown_window.title("Scheduled Shutdown")

    label = tk.Label(scheduled_shutdown_window, text="Enter seconds to delay shutdown:")
    label.pack()

    entry = tk.Entry(scheduled_shutdown_window)
    entry.pack()

    button = tk.Button(scheduled_shutdown_window, text="Shutdown", command=lambda: shutdown_scheduled(int(entry.get())))
    button.pack()

def sleep():
    return os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


if __name__ == "__main__":
    gui = Tk()
    gui.title("Shutdown")
    gui.geometry("250x140")
    Button(gui, text="Instant Shutdown", width=34, command=shutdown).grid(row=0)
    Button(gui, text="Schedule your shutdown", width=34, command=show_scheduled_shutdown_window).grid(row=1)
    Button(gui, text="Restart", width=34, command=restart).grid(row=2)
    Button(gui, text="Sleep", width=34, command=sleep).grid(row=3)
    Button(gui, text="Log out", width=34, command=logout).grid(row=4)


mainloop()
