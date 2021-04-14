import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd=r'C:\Users\Ven02111\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img=Image.open('C:/New folder/ash python/pqe.jpg')
text=tess.image_to_string(img)
print("extracted textv dfrom image is as ")

print(text)