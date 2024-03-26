# CalendarAppTkinter
A personal calendar app made with the `Tkinter`, `datetime`, and `calendar` modules in Python. 

If you think the code's messy, it probably is very messy and hard to read. But it works and is updatable (very difficult to update though). Edit the code at your own risk because even I forgot some of the connections between variables in the code. 

> **Installation**

Ensure that all assets and main `.py` file are placed in the same directory. You need to have the `PIL` library installed with the following: `pip install pillow`. You may want to check which modules are already installed with `python -m pip list`. 

> **Purpose**

This is a personal calendar app that I programmed for my own use. Coding such an app may seem like a simple task but requires a lot of familiarity with the programming mindset: a mindset which utilizes lots of logic. The ability to add new features without breaking old ones succesfully, the ability to persevere in the face of troubleshooting, these are all skills I want to learn and have improved upon by coding this project. 

Some examples of the logic that's difficult to code includes the placement of each month, matching the GUI layout with the internal date and event trackers, and managing all of the data efficiently with nested lists. 

> **Roadmap**

 - Finish the strikethrough system for events so that it works correctly.
 - Add a visual list for each date on the calendar.
 - Store the internal data in lists within text files in the same directory (this way the data is saved even after closing the GUI).
 - Clear old data stored in the text files to speed up the program.
 - Create a "focus timer" system which starts a timer (similar to the Microsoft Clock app's focus system on Windows 11)
 - Graph the user's productivity over a certain month based on how many hours they focus each day.
 - Connect to spotify for music during focus sessions using Spotify API. 
 - Convert this program to an `.exe` file for personal use, using pyexe module from PIP. 
