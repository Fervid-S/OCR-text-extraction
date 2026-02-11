import streamlit as st
import pytesseract
import cv2
import numpy as np
from PIL import Image

# Update path if needed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="OCR App", layout="centered")

st.title("📄 OCR Text Extractor")
st.write("Upload an image and extract text using Tesseract OCR.")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)

    text = pytesseract.image_to_string(gray)

    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.subheader("Extracted Text")
    st.text_area("", text, height=300)

    st.download_button(
        "Download Text",
        text,
        file_name="output.txt"
    )
