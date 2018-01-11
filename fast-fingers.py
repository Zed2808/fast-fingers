from PIL import Image
import pyscreenshot
import pytesseract
import pyautogui

# Set bounds for the OCR screenshot
x_min = 275
x_max = 1245
y_min = 300
y_max = 340

last = ''

while True:
    # Get the current mouse coordinates
    x, y = pyautogui.position()

    # Only run if the mouse is approximately over the first letter of the first word
    if x_min < x < x_max and y_min < y < y_max:
        # Take a screenshot with the specified bounds
        im = pyscreenshot.grab(bbox=(x_min, y_min, x_max, y_max))

        # Use tesseract OCR to convert the image to a string
        s = pytesseract.image_to_string(im)

        # Only type if a new line is detected
        if s != last:
            print(s)

            # Enter the line word by word, followed by a space to enter the word
            # Using a 0.01s delay prevents typing too fast for the site to handle
            pyautogui.typewrite(f'{s} ', interval=0.01)

        last = s
