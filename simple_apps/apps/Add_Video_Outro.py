import os
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Store the profile settings in a JSON file
SETTINGS_FILE = 'video_settings.json'

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {}

def setup_profile():
    settings = load_settings()

    profile_name = input("Enter profile name: ")
    settings[profile_name] = {}

    for video_type in ["Landscape Video Setup", "Portrait Video Setup"]:
        print(f"\n-- {video_type} --")
        outro_dir = input("Enter the OUTRO VIDEO directory (leave blank if not needed): ")

        settings[profile_name][video_type] = {
            "Outro Directory": outro_dir
        }

    save_settings(settings)
    print(f"Profile '{profile_name}' saved successfully.")

def detect_video_orientation(file_path):
    clip = VideoFileClip(file_path)
    width, height = clip.size
    clip.close()

    return "Landscape" if width > height else "Portrait"

def generate_output_filename(video_file, add_outro):
    # Extract the file name and extension
    base_name, ext = os.path.splitext(os.path.basename(video_file))

    # Add appropriate suffixes to the file name
    suffix = "_outro" if add_outro else ""

    # Generate the output file name
    output_filename = f"{base_name}{suffix}{ext}"

    # Return the full path to the output file (same directory as the original)
    return os.path.join(os.path.dirname(video_file), output_filename)

def process_video():
    settings = load_settings()

    if not settings:
        print("No profiles available. Please set up a profile first.")
        return

    # Display available profiles
    profile_names = list(settings.keys())
    if not profile_names:
        print("No profiles available. Please set up a profile first.")
        return

    print("Available profiles:")
    for i, profile in enumerate(profile_names, 1):
        print(f"{i}. {profile}")

    # Select profile by number
    while True:
        try:
            profile_index = int(input("Select profile number: ")) - 1
            if 0 <= profile_index < len(profile_names):
                profile_name = profile_names[profile_index]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    video_file = input("Enter the path to the video file you want to modify: ")
    if not os.path.exists(video_file):
        print("Video file not found!")
        return

    orientation = detect_video_orientation(video_file)
    video_setup = "Landscape Video Setup" if orientation == "Landscape" else "Portrait Video Setup"

    print(f"\nDetected video orientation: {orientation}")
    outro_dir = settings[profile_name][video_setup]["Outro Directory"]

    # Extract only the filename for the confirmation prompt
    outro_filename = os.path.basename(outro_dir)

    add_outro = input(f"Add outro? (yes/no) [Current outro: {outro_filename}]: ").lower() == "yes"

    # Process the video
    clip = VideoFileClip(video_file)

    # Add outro if requested
    if add_outro and outro_dir and os.path.exists(outro_dir):
        outro_clip = VideoFileClip(outro_dir)
        # Ensure that both clips have audio
        clip = clip.set_audio(clip.audio)
        outro_clip = outro_clip.set_audio(outro_clip.audio)
        clip = concatenate_videoclips([clip, outro_clip], method="compose")

    # Generate the output file name
    output_file = generate_output_filename(video_file, add_outro)

    # Write the processed video to the output file with audio explicitly enabled
    clip.write_videofile(output_file, audio=True)

    print(f"Video processing complete. Output saved to: {output_file}")

def main():
    while True:
        print("\nVideo Processing App")
        print("1. Setup Profile")
        print("2. Process Video")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            setup_profile()
        elif choice == "2":
            process_video()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
