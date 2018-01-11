from PIL import Image
import pyscreenshot
import pytesseract
import pyautogui

x_min = 275
x_max = 1245
y_min = 300
y_max = 340

last = ''

while True:
    x, y = pyautogui.position()

    if x_min < x < x_max and y_min < y < y_max:
        im = pyscreenshot.grab(bbox=(x_min, y_min, x_max, y_max))

        s = pytesseract.image_to_string(im)

        if s != last:
            print(s)

            pyautogui.typewrite(f'{s} ', interval=0.01)

        last = s
