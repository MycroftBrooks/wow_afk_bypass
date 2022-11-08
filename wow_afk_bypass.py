import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import time
import random

def main():
    print("Now launch WOW and wait...")
    wowTitle = "World of Warcraft"
    starttime=time.time()
    keys = ['left', 'right', 'up', 'down', 'space']
    while True:
        currentWindow = GetWindowText(GetForegroundWindow())
        key = random.randint(0, 4)
        if(currentWindow == wowTitle):
            print("Pressing key: " + keys[key])
            pyautogui.press(keys[key])
        interval = random.randint(1, 120)
        time.sleep(interval - ((time.time() - starttime) % interval))

if __name__ == "__main__":
    main()

