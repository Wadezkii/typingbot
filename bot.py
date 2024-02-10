import pyautogui
import time

def type_text(text, delay=0.1):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)