# BINARY MACRO
## Problem
I have a course called digital systems which involves creating many truth tables. Hence I need to type hundreds of 1s and 0s. This wouldn't be an issue if the 1 and 0 keys where next to each other on the keyboard, but those keys are on either end of the keyboard!

Typing 1s and 0s with one hand on my standard keyboard is far too inefficient to my liking.

## Over-engineered solution
To reduce the amount of distance I need to move my hand across the keyboard, I have created a SINGLE button to type 1s and 0s.
Single click for 0, double click for 1. No more need to move my hand across the keyboard :)

Uses 2 wires, arduino pro micro, and a button. 

## Unnecessarily analysis
Work = Force * Distance
Assuming the hand weighs 1Kg, the distance between the 1 and 0 key is 17cm, and the time to move the hand from 1 to 0 is 0.5s
then the work done is ~ 57.8mJ

With my over-engineered solution, the distance my finger (assuming it weighs 50g) is required to move is 1mm.
This results in the work being ~ 0.228 mJ!

This is an energy saving of 250 000% !
