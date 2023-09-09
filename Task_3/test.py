from PIL import Image
import pytesseract
import pyttsx3

tts = pyttsx3.init()

image = Image.open("text.png")

text = pytesseract.image_to_string(image)

print(text)
tts.save_to_file(text, "output.mp3")
tts.say(text)

tts.runAndWait()
