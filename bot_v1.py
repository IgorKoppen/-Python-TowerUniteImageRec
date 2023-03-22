# Import required packages 

import cv2
import pytesseract 
import pyautogui
import keyboard

# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/igork/AppData/Local/Tesseract-OCR/tesseract.exe'


# function handles thresholding and using tesseract
def get_text_from_img(img):
    text = ''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
      
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
      
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30)) 
      
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
      
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                     cv2.CHAIN_APPROX_NONE) 
      
    im2 = img.copy() 

    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped) 

    return text.replace('\n', ' ')

# two screenshots (one for first word and then everything else)

# get first word



# get all words but first word
keyboard.wait('-')
for i in range(40):
 pyautogui.screenshot('first.png', region=(690, 810, 170, 40))
 first_word = get_text_from_img(cv2.imread('first.png')).split(' ')[0]
 pyautogui.screenshot('rest.png', region=(720, 810, 740, 100))
 rest = get_text_from_img(cv2.imread('rest.png')).split(' ', 1)[1]
 text = first_word + ' ' + rest
 keyboard.write(text, delay=0.00057) # close to 200 WPM
