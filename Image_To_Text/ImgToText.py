import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Python\tesseract\tesseract'

img = Image.open("D:\myprograms\Python projects\hinditext3.png")
img.load()
text = pt.image_to_string(img,lang='hin')

print(text)
