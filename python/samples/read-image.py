from PIL import Image
import pytesseract
import json
import os
import glob

def ocr_image(image_path, languages='eng+deu'):
    # Open the image file
    img = Image.open(image_path)

    # Run OCR on the image
    text = pytesseract.image_to_string(img, lang=languages)
    return text

def generate_json(text, group_code, image_id):
    # Aggregate all extracted text as German text
    data = {
        "id": image_id,  # Use the image filename or index as ID
        "en": "",  # No text in English field
        "de": text,  # All extracted text in the German field
        "groupCode": group_code
    }
    return data

def process_images_in_folder(folder_path):
    # Create a list to store results
    results = []
    group_code = 1  # Assuming a fixed group code, you can modify if needed

    # Use glob to find all image files in the specified folder
    image_files = glob.glob(os.path.join(folder_path, '*'))

    for image_id, image_file in enumerate(image_files, start=1):
        print(f"Processing {image_file}...")
        # Run OCR
        extracted_text = ocr_image(image_file)

        # Generate JSON
        result = generate_json(extracted_text, group_code, image_id)

        # Add result to list
        results.append(result)

    return results

if __name__ == "__main__":
    # Path to your images folder
    folder_path = './image'  # Update this to your folder containing images

    # Process images in the folder
    results = process_images_in_folder(folder_path)

    for result in results:
        # Print JSON output for each image
        print(json.dumps(result, indent=2))

        # Optionally, save JSON to separate files
        output_file = f"output_{result['id']}.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)

    # Optionally, save all results to a single file
    with open('all_outputs.json', 'w') as f:
        json.dump(results, f, indent=2)