import pytesseract
from PIL import Image
import pyttsx3

# Set the path to the Tesseract executable (if it's not in your PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image (make sure to have an image with text in it)
image = Image.open('image.png')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Convert the extracted text to speech
engine.say(text)

# Play the speech
engine.runAndWait()
