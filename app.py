import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

st.markdown("""
    <h1 style="text-align:center;">
        Audio Extractor from Video 
        <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExamN1OXkycm5kZDdqcjhjYzlqOXQxbzB3OThmejhmbGIzMHZ4cDRkdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/uw0wMe62pCn0uqmFnu/giphy.gif" width="100"/>
    </h1>
""", unsafe_allow_html=True)


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
