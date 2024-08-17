import os
import random
from PIL import Image
import ffmpeg
from datetime import datetime, timedelta

def randomize_date():
    """Generate a random date within the last 10 years."""
    start_date = datetime.now() - timedelta(days=365 * 10)
    random_date = start_date + timedelta(days=random.randint(0, 3650))
    return random_date.strftime('%Y-%m-%dT%H:%M:%S')

def remove_image_metadata(file_path):
    try:
        img = Image.open(file_path)
        data = list(img.getdata())
        img_no_metadata = Image.new(img.mode, img.size)
        img_no_metadata.putdata(data)

        # Create new file name
        file_name, file_ext = os.path.splitext(file_path)
        new_file_path = f"{file_name}_clean{file_ext}"

        # Save the new image without any metadata
        img_no_metadata.save(new_file_path)
        print(f"Metadata removed from image and saved as {new_file_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

def remove_video_metadata(file_path):
    try:
        # Create new file name
        file_name, file_ext = os.path.splitext(file_path)
        new_file_path = f"{file_name}_clean{file_ext}"

        # Generate random date for metadata
        random_date = randomize_date()

        # Use ffmpeg to remove metadata and randomize the creation date
        ffmpeg.input(file_path).output(
            new_file_path,
            map_metadata=-1,
            metadata=f'creation_time={random_date}'
        ).run()
        print(f"Metadata removed from video and saved as {new_file_path}. Creation date set to {random_date}")
    except Exception as e:
        print(f"Error processing video: {e}")

def get_valid_file_path():
    while True:
        file_path = input("Enter the file location (image or video): ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print("File does not exist. Please try again.")

def main():
    file_path = get_valid_file_path()

    file_ext = os.path.splitext(file_path)[1].lower()

    # Check file type and process accordingly
    if file_ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
        remove_image_metadata(file_path)
    elif file_ext in [".mp4", ".mov", ".avi", ".mkv"]:
        remove_video_metadata(file_path)
    else:
        print("Unsupported file type. Please provide an image or video file.")

if __name__ == "__main__":
    main()
