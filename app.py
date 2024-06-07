import streamlit as st
import cv2

# Load the image
img = cv2.imread("img.jpg")  # Replace with the actual path to your image

# Define functions for image processing
def grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def blur(img):
    blurred = cv2.GaussianBlur(img, (27, 27),0)  # Adjust blur kernel size as needed
    return blurred

def edge(img):
    edges = cv2.Canny(img, 100, 200)  # Adjust thresholds as needed
    return edges

# Create the Streamlit app layout
st.title("Image Processing with Streamlit")

st.image(img, caption="Original Image", use_column_width=True)

# Add buttons for image processing actions
action = st.radio("Select Action", ("Grayscale", "Blur", "Edge Detection"))

if action == "Grayscale":
    processed_img = grayscale(img)
    st.image(processed_img, caption="Grayscale Image", use_column_width=True)
elif action == "Blur":
    processed_img = blur(img)
    st.image(processed_img, caption="Blurred Image", use_column_width=True)
elif action == "Edge Detection":
    processed_img = edge(img)
    st.image(processed_img, caption="Edge Image", use_column_width=True)
