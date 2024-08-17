from gtts import gTTS, gTTSError
import os
from tqdm import tqdm
import time

def text_to_speech(file_path, lang='en', chunk_size=500, delay=2, max_retries=5):
    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into chunks to manage API requests
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Initialize an empty list to store the names of temporary audio files
    temp_files = []

    # Display progress bar and process each chunk
    for i, chunk in enumerate(tqdm(chunks, desc="Processing text to speech")):
        temp_file = f'temp_{i}.mp3'
        retries = 0
        success = False

        while not success and retries < max_retries:
            try:
                tts = gTTS(text=chunk, lang=lang, slow=False)
                tts.save(temp_file)
                temp_files.append(temp_file)
                success = True
            except gTTSError as e:  # Corrected the exception to use gTTSError
                if '429' in str(e):
                    retries += 1
                    wait_time = delay * (2 ** retries)  # Exponential backoff
                    print(f"Rate limit hit. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise e

    # Combine the temporary audio files into a single output file
    output_file = os.path.splitext(file_path)[0] + '.mp3'
    with open(output_file, 'wb') as final_file:
        for temp_file in temp_files:
            with open(temp_file, 'rb') as temp:
                final_file.write(temp.read())

    # Clean up temporary files
    for temp_file in temp_files:
        os.remove(temp_file)

    print(f"Text to speech conversion completed. Audio saved as {output_file}")

# Prompt user for file path
file_path = input("Please enter the path to the .txt file: ").strip()
text_to_speech(file_path)
