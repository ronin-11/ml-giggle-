##IMAGE CAPTIONING WEBAPP

       ##MADE BY  ABEL TINOTENDA TEMBO..................R204434C


import streamlit as st
import cv2
import tempfile
import os
from PIL import Image
from io import BytesIO
import requests

# Function to upload video and split into frames
def process_video(video):
    frames = []

    # Read video using OpenCV
    vidcap = cv2.VideoCapture(video)

    # Get frames from video
    success, image = vidcap.read()
    while success:
        frames.append(image)
        success, image = vidcap.read()

    return frames

# Function to generate text description using the deployed model
def generate_description(frames):
    descriptions = []

    # Iterate through frames and process using the deployed model
    for frame in frames:
        # Process frame with the deployed model and generate description
        # Replace this with your code to process frames with the model
        description = "This is a sample description for the frame."
        descriptions.append(description)

    return descriptions

# Main application code
def main():
    st.title("Video Description Generator")
    st.write("Upload a video file (max 2MB) to generate text descriptions for each frame.")

    # Upload video file
    video_file = st.file_uploader("Upload Video", type=["mp4", "mov"])

    if video_file is not None:
        # Check file size
        if video_file.size > 2e6:
            st.error("Video file size exceeds the limit of 2MB.")
            return

        # Save video to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(video_file.read())

        # Process video and generate frames
        frames = process_video(temp_filename)

        # Generate descriptions for frames
        descriptions = generate_description(frames)

        # Display frames and descriptions
        for i, (frame, description) in enumerate(zip(frames, descriptions)):
            st.subheader(f"Frame {i+1}")
            st.image(frame, channels="BGR", use_column_width=True)
            st.write(description)
            st.write("---")

        # Remove temporary file
        os.remove(temp_filename)

if __name__ == "__main__":
    main()

