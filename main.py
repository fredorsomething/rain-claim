import pyautogui
import time

#CLICK LOCATION MIGHT HAVE TO BE CHANGED DEPENDING ON RESOLUTION/BROWSER/OS. Default should work on standard browser settings. Make sure you're in fullscreen!
# Define the coordinates of the first click location
x1, y1 = 100, 400

# Define the coordinates of the second click location
x2, y2 = 790, 600

# Run an infinite loop
while True:
    print("waiting for first click ")
    time.sleep(15)

    # Click at the first location
    pyautogui.click(x1, y1)
    print("first click complete (opened rain captcha)")

    # Wait for 10 seconds
    print("waiting for second click")
    time.sleep(15)
    # Click at the second location
    pyautogui.click(x2, y2)
    print("second click complete (passed captcha and entered rain)")
    time.sleep(30)
    print("waiting for next rain")
    # Waiting for 29 minutes before next rain
    time.sleep(1740)
