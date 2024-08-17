

import string
import re

def clean_and_format_text(file_path, output_file_path=None):
    # Define the translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove punctuation from the text
    no_punctuation_text = text.translate(translator)
    
    # Replace multiple spaces with a single space
    formatted_text = re.sub(r'\s+', ' ', no_punctuation_text).strip()
    
    # Print or write the cleaned and formatted text
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_text)
        print(f"Formatted text has been written to {output_file_path}")
    else:
        print(formatted_text)


# Example usage
clean_and_format_text('/Users/pinax/Desktop/PythonApps/text_analysis/input_text.txt', '/Users/pinax/Desktop/PythonApps/text_analysis/output_text.txt')
