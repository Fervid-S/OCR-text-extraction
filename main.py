import cv2
import pytesseract
from PIL import Image

# The path has to be changed according to your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # noise removal
    gray = cv2.medianBlur(gray, 3)

    text = pytesseract.image_to_string(gray)

    return text


if __name__ == "__main__":
    image_path = "sample.jpg"   # put any image here
    extracted_text = extract_text(image_path)

    print("Extracted Text:\n")
    print(extracted_text)
