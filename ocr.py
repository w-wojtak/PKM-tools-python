from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'your path\tesseract.exe'


def ocr(image_path, output_file):
    # Open the image file
    img = Image.open(image_path)

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(img)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Write the extracted text to a text file
    with open(output_file, "w") as file:
        file.write(text)
    print("Text extracted and saved to", output_file)


image_path = "images/ml-qs.jpg"  # Replace with the path to your image

output_file = "extracted_text.txt"  # Path to save the extracted text
ocr(image_path, output_file)

