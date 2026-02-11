On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\KIIT0001\Desktop\ocr-project> git push
Everything up-to-dateimport streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="OCR App", layout="centered")

st.title("📄 OCR Text Extractor (EasyOCR)")
st.write("Upload an image and extract text using Deep Learning OCR with bounding boxes.")

# Initialize EasyOCR reader (loads model once)
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'])

reader = load_reader()

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    # Run OCR
    results = reader.readtext(img_array)

    extracted_text = ""
    boxed_image = img_array.copy()

    # Draw bounding boxes + collect text
    for bbox, text, prob in results:
        extracted_text += text + " "

        pts = np.array(bbox).astype(int)
        cv2.polylines(boxed_image, [pts], True, (0, 255, 0), 2)

    st.subheader("Detected Text Areas")
    st.image(boxed_image, use_container_width=True)

    st.subheader("Extracted Text")
    st.text_area("", extracted_text, height=300)

    st.download_button(
        label="Download Text",
        data=extracted_text,
        file_name="output.txt"
    )
