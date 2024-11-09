import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

st.title("Audio Extractor from Video")

# Upload video file
video_file = st.file_uploader("Upload Video File", type=["mp4", "mkv", "mov", "avi"])
if video_file:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_file.read())
        temp_video_path = temp_file.name

    try:
        # Load video
        clip = VideoFileClip(temp_video_path)

        # Extract audio
        audio_filename = "extracted_audio.mp3"
        clip.audio.write_audiofile(audio_filename)

        st.success("Audio extracted successfully!")

        # Download link for extracted audio
        with open(audio_filename, "rb") as f:
            audio_data = f.read()
            st.download_button(
                label="Download Extracted Audio",
                data=audio_data,
                file_name=audio_filename,
                mime="audio/mp3"
            )

        
    finally:
        # Clean up audio file
        os.remove(audio_filename)
