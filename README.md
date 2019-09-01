# TwitterDeAuth
A hacky Python program for de-authorizing apps on your Twitter account.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You must have Python 3 installed. 
You must have the pyautogui package installed. A good reference for how to do that is in one of the chapters of [Automate the Boring Stuff, Chapter 18](https://automatetheboringstuff.com/chapter18/).

For this to work, I recommend turning off any scaling settings you have on your machine, like the "Scale and Layout" settings that are on Windows 10. 

Also, you might want to limit your resolution to 1920 x 1080, since the larger the desktop, the slower this script runs (because of image processing).

### Installation

Copy all files to a folder on your machine. In the command line, navigate to that folder.


If your mouse is set for left-handers, the program should run fine. If it's set for right-handers, you'll need to edit the program so that the constant for handedness reflects that you want to do left mouse button clicks instead of right.

### Setting up on Twitter

Navigate to More-->Settings and Privacy-->Account-->Apps and Sessions on the Twitter website for your account.

### Running the program

Run the program from the command line. For example:

C:\Users\YourName\YourDevFolder\py deauth.py

The script will ask you for an upper limit for deauthorizations. You should be able to sit back and watch it work.

There is a [YouTube video of what it looks like running here](https://www.youtube.com/watch?v=SPjp8lrn9gc).