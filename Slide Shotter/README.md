# Slide Shotter
## Problem
Some profs do not post lecture slides despite posting the recording. This can be a bit of a nuisance since I like to review slides when studying to ensure I haven't missed out on any concepts or equations. So instead of fast forwarding the lecture recording, I made a python script to watch the lecture for me and save screenshots of the slides.

## How it works (kinda)
The script uses opencv and pyautogui to do screenshotting and to determine the number of pixels changed, which may indicate the slide has changed. I also use Tesseract OCR to determine if the text on the screenshotted slides has changed. Using both pixel counting and OCR, the script can figure out with ~80% accuracy if the slide has changed and consequently saving a screenshot. This script is based on my Stormhacks 2022 hackathon project but modified to work slightly better.

## How to use it
Simply have the lecture open on a second monitor playing at 2x speed and run the script (with Tesseract and required python dependencies installed). In the meantime you can do something else like wondering if you should have used your time studying instead of making this script. After your lecture recording finishes you should have the screenshotted slides saved on your computer. 

## Result
Scripting in python is fun. Might see if I can use OCR and python scripting to automate other daily tasks.