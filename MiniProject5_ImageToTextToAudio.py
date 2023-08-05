from PIL import Image, ImageFilter
from gtts import gTTS
import pytesseract
import os 
#Importing all the necessary libraries

pytesseract.pytesseract.tesseract_cmd  = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def convert_to_sound(image):
    try:
        open_image = Image.open(image)
        text = pytesseract.image_to_string(open_image)
        text_file = ''.join(text.split("\n"))
        print(text_file)
        sound = gTTS(text_file,lang="en")
        sound.save("sound.mp3")
        os.system("start sound.mp3")
        return True
    except Exception as bug:
        print("The error while exercuting the code ",bug)
if __name__ == "__main__":
    convert_to_sound('imagetotext.jpeg')