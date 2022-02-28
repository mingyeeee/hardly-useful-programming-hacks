import cv2
import numpy as np
import time
import os
import pyautogui
from difflib import SequenceMatcher

# finds the similarity between 2 images
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# takes a screenshot of the screen and converts it into gray scale for OCR
def screenshot():
    img = pyautogui.screenshot()
    grayimg = np.array(img)
    img = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY)
    # crop screen to remove 7% from left and right
    grayimg = grayimg[:, int(grayimg.shape[1]*0.15):int(img.shape[1]*0.85)]
    # crop screen to remove taskbar
    grayimg = grayimg[0:int(img.shape[0]*0.92), :]
    return grayimg

time.sleep(5)
count = 1
prevtext = ""
previmg = screenshot()
while(True):
    # Capture frame-by-frame
    img = screenshot()

    # save a screenshot in color incase the image needs to be saved
    colorimg = pyautogui.screenshot()
    colorimg = np.array(colorimg)
    # crop screen to remove 7% from left and right
    saveimg = colorimg[:, int(colorimg.shape[1] * 0.1):int(colorimg.shape[1] * 0.9)]
    
    # find difference between current and previous image
    diff = cv2.absdiff(img, previmg)
    # count number of pixels that are different
    pixeldiff = np.sum(diff)

    # save image for tesseract to run OCR on
    cv2.imwrite('screenshot.png', img)
    cmd = "tesseract screenshot.png out"
    os.system(cmd)

    # retrieve return text from Tesseract OCR
    f = open("out.txt", "r", encoding="utf-8")
    text = f.read().encode('utf-8')
    f.close()

    # compare OCR text to previous OCR text and 
    #   previous screenshots to the current screen
    #   to see if it has changed
    if similar(text,prevtext) < 0.5 and pixeldiff > 5000:
        prevtext = text
        previmg = img
        print(text)
        print("Saving ...")
        print("Similarity: " + str(similar(text,prevtext)))
        print("Pixel difference: " + str(pixeldiff))
        # save image to folder
        cv2.imwrite('slide'+str(count)+'.png', saveimg)
        count += 1
    
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
