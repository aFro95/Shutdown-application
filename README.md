# Shutdown-application
The program is a simple graphical interface created in Tkinter to control various system-level actions on the Windows operating system. Here's a brief description of the main functionalities of this program:

  Instant Shutdown:
The "Instant Shutdown" button immediately initiates a system shutdown (shutdown) with a delay of 1 second (/t 1).

  Schedule Your Shutdown:
The "Schedule your shutdown" button opens a separate window where you can enter a number of seconds to schedule a future system shutdown.

  Restart:
The "Restart" button immediately initiates a system restart (shutdown /r /t 1).

  Sleep:
The "Sleep" button initiates the system to enter sleep mode (rundll32.exe powrprof.dll,SetSuspendState 0,1,0).

  Log Out:
The "Log out" button initiates the log out of the current user (shutdown -l).

It's important to note that using system commands such as shutdown, rundll32.exe may vary depending on the operating system version and user permissions. 
Additionally, the functionality of scheduling system shutdown needs further review to ensure that the scheduled shutdown is handled correctly.

Also, I uploaded a version of this program as an executable file, so a person who doesn't want to use PyCharm or any other programs can run it.
