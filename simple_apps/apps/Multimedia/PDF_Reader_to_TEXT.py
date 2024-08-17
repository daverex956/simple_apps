import pdfplumber
import pytesseract
from PIL import Image
from tqdm import tqdm
import os

def ocr_pdf_to_text(pdf_path, txt_output_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
            for page_num, page in tqdm(enumerate(pdf.pages), total=len(pdf.pages), desc="Processing pages"):
                # Convert PDF page to an image
                image = page.to_image(resolution=300).original

                # Perform OCR on the image
                text = pytesseract.image_to_string(image)

                # Write the extracted text or indicate failure
                if text.strip():
                    txt_file.write(text + '\n')
                else:
                    txt_file.write(f"[Page {page_num + 1} could not be extracted]\n")
    
    print(f'OCR text extraction complete. Text saved to {txt_output_path}')


def get_valid_file_path(prompt):
    while True:
        file_path = input(prompt).strip()
        if os.path.isfile(file_path):
            return file_path
        else:
            print(f"Error: The file '{file_path}' does not exist. Please try again.")


if __name__ == "__main__":
    # Get a valid PDF path from user
    pdf_path = get_valid_file_path("Please enter the full path to the PDF file: ")

    # Autogenerate output file name in the same directory as the PDF
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Get PDF file name without extension
    pdf_dir = os.path.dirname(pdf_path)  # Get directory of the PDF file
    txt_output_path = os.path.join(pdf_dir, f"{base_name}_output.txt")  # Create the output file path in the same directory as the PDF

    # Run OCR conversion
    ocr_pdf_to_text(pdf_path, txt_output_path)
