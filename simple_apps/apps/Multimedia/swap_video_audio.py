from moviepy.editor import VideoFileClip, AudioFileClip
import os

def replace_audio_in_video():
    # Prompt the user for the directory and filename of the video file
    video_path = input("Enter the full path of the video file (e.g., /path/to/video.mp4): ")
    
    # Ensure the video file exists
    if not os.path.isfile(video_path):
        print("Video file does not exist.")
        return

    # Prompt the user for the directory and filename of the new audio file
    audio_path = input("Enter the full path of the new audio file (e.g., /path/to/audio.mp3): ")
    
    # Ensure the audio file exists
    if not os.path.isfile(audio_path):
        print("Audio file does not exist.")
        return
    
    # Load the video and the new audio
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip as the new audio clip
    new_video_clip = video_clip.set_audio(audio_clip)
    
    # Build the new video file path
    video_dir = os.path.dirname(video_path)
    video_filename = os.path.basename(video_path)
    new_video_filename = video_filename.replace('.mp4', '_mastered_audio.mp4')
    new_video_path = os.path.join(video_dir, new_video_filename)
    
    # Write the result to a new file
    new_video_clip.write_videofile(new_video_path, codec='libx264', audio_codec='aac')
    
    # Close the clips to free up resources
    video_clip.close()
    audio_clip.close()
    new_video_clip.close()
    
    print(f"New video with replaced audio saved as: {new_video_path}")

if __name__ == "__main__":
    replace_audio_in_video()
