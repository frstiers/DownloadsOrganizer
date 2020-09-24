# Downloads Organizer

This project is for creating a Python script for organizing the Downloads folder on your Windows desktop, although it could be tweaked to work on Mac or Linux, it wasn't designed with those OS's in mind.

## Usage/Installation

Feel free to clone the repo and set it up on your machine. For best results, schedule the script to run as a background process on your machine, see instructions below.

Instructions:
- Open your Task Scheduler in Windows 10
- Go to your Task library
- Create Basic Task
- Walk through the steps in the setup wizard until you get the the "start a program"
- Find the location of your Python3 installation on your computer (e.g. C:\Python38)
- In order to run the script completely in the background, you have to use the pythonw.exe executable instead of python.exe
- Save the steps and setup the task to run according to whatever trigger you'd like
- Note: if you need to stop the script from running in the background, open your task manager (ctrl-shift-escape) and "End task" on python

## License
[MIT](https://choosealicense.com/licenses/mit/)