import os
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
# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

### Convert all files
process_target = []
for file in os.listdir(input_dir):
    if file.endswith(".HEIC") or file.endswith(".heic"):
        process_target.append(file)

sorted_target = sorted(process_target)

## Additinal filter
## sorted_target = [file for file in sorted_target if file >= "IMG_2818.HEIC"]

count = 0
for file in sorted_target:
    try:
        input_heic_file = os.path.join(input_dir, file)
        output_jpg_file = os.path.join(output_dir, file.replace(".HEIC", ".jpeg"))
        convert_heic_to_jpg(input_heic_file, output_jpg_file)
        count += 1
        print(f"Converted {input_heic_file} to {output_jpg_file}")
    except Exception as e:
        print(f"Error converting {input_heic_file}: {e}")

print(f"Converted {count} files")
