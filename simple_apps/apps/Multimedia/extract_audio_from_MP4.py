import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    print("Starting audio extraction...")  # Debug print
    # Check if the file exists
    if not os.path.exists(video_path):
        print("Error: File does not exist.")
        return

    try:
        video = VideoFileClip(video_path)
        output_audio_path = os.path.splitext(video_path)[0] + '.mp3'
        audio = video.audio
        audio.write_audiofile(output_audio_path, codec='mp3')
        video.close()
        print(f"Audio extracted and saved as {output_audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Script started.")  # Initial debug print
video_file_path = input("Enter the path to the MP4 video file: ")
print(f"Path entered: {video_file_path}")  # Debug print to confirm input
extract_audio(video_file_path)
