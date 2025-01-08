import random
import time
import pyautogui

while True:
    width, height = pyautogui.size()
    x = random.randint(0, width)
    y = random.randint(0, height)
    pyautogui.moveTo(x, y)
    # pyautogui.click()
    time.sleep(2)