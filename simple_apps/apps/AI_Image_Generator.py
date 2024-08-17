import os
import requests
from config import OPENAI_KEY

openai_api_url = "https://api.openai.com/v1/images/generations"


def generate_image(prompt, folder_path, file_name="generated_image.png"):
    try:
        print(f"Debug: Checking if folder exists or needs creation: {folder_path}")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Debug: Created directory: {folder_path}")
        else:
            print(f"Debug: Directory already exists: {folder_path}")
        
        print(f"Debug: Sending request to OpenAI to generate image with prompt: {prompt}")
        
        # Send request to OpenAI's API for image generation
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }
        response = requests.post(openai_api_url, json=data, headers=headers)
        response_data = response.json()
        
        # Check if response was successful
        if response.status_code == 200:
            image_url = response_data['data'][0]['url']
            print(f"Debug: Image URL fetched: {image_url}")
            
            # Fetch the image content
            image_data = requests.get(image_url).content
            print(f"Debug: Image data fetched successfully")
            
            # Save the image to the specified folder
            image_path = os.path.join(folder_path, file_name)
            with open(image_path, 'wb') as f:
                f.write(image_data)
            print(f"Image saved at: {image_path}")
        else:
            print(f"Error: Failed to generate image. Response: {response_data}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
prompt = "A futuristic city with flying cars and neon lights"
folder_path = input("Please enter the directory where you want the images saved: ")

if not folder_path:
    folder_path = "my_images"

generate_image(prompt, folder_path)
