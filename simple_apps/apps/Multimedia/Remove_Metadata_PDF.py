import os
from PyPDF2 import PdfReader, PdfWriter

def remove_metadata_from_pdf():
    # Prompt user for file path
    file_path = input("Enter the full path of the PDF file: ")
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return
    
    # Create the output file name by appending '_1' to the original name
    file_dir, file_name = os.path.split(file_path)
    file_name_no_ext, file_ext = os.path.splitext(file_name)
    output_file_name = f"{file_name_no_ext}_1{file_ext}"
    output_file_path = os.path.join(file_dir, output_file_name)
    
    try:
        # Read the original PDF
        reader = PdfReader(file_path)
        writer = PdfWriter()

        # Copy over all the pages without the metadata
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # Save the new PDF without metadata
        with open(output_file_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Metadata removed. File saved as: {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_metadata_from_pdf()
