from PIL import Image
import pyheif

def convert_heic_to_jpg(input_path, output_path):
    # Read the HEIC file
    heif_file = pyheif.read(input_path)
    
    # Convert the HEIC file to a PIL image
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # Save the image as a JPG file
    image.save(output_path, "JPEG")

# Read all .HEIC files from `input` directory
input_dir = "input"
output_dir = "output"

import os
for file in os.listdir(input_dir):
    if file.endswith(".HEIC"):
        input_heic_file = os.path.join(input_dir, file)
        output_jpg_file = os.path.join(output_dir, file.replace(".HEIC", ".jpeg"))
        convert_heic_to_jpg(input_heic_file, output_jpg_file)
        print(f"Converted {input_heic_file} to {output_jpg_file}")

print("All done!")
