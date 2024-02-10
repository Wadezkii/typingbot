import os
from dotenv import load_dotenv
load_dotenv()
import pyautogui
import time
from PIL import ImageGrab
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def wait_for_key_press(key='enter'):
    print(f"Press {key} to continue...")
    pyautogui.waitForAnyKeyPress(keys=[key])

def select_area():
    print("Move the mouse to the start position and press Enter.")
    input()
    start_x, start_y = pyautogui.position()

    print("Move the mouse to the end position and press Enter.")
    input()
    end_x, end_y = pyautogui.position()

    if start_x > end_x:
        start_x, end_x = end_x, start_x
    if start_y > end_y:
        start_y, end_y = end_y, start_y

    return (start_x, start_y, end_x, end_y)


def read_text_from_selected_area(bbox):
    screenshot = ImageGrab.grab(bbox=bbox)
    text = pytesseract.image_to_string(screenshot)
    return text.strip()

def type_text(text, delay_range=(0.05, 0.35)):
    words = text.split()
    
    for word in words:
        pyautogui.typewrite(word, interval=0)
        random_delay = random.uniform(*delay_range)
        time.sleep(random_delay)
        pyautogui.typewrite(' ')

def main():
    bbox = select_area()
    text_to_type = read_text_from_selected_area(bbox)
    time.sleep(1)
    type_text(text_to_type)

if __name__ == "__main__":
    main()