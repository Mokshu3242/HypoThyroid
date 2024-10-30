import os
from aspose.cells import Workbook

# Set the directory containing the XML files
input_dir = "/untitled folder/archive"

# Set the output directory for the PNG files
output_dir = "/archive/Output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an XML file
    if filename.endswith(".xml"):
        # Construct the input and output file paths
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")

        # Load the XML file into a Workbook object
        workbook = Workbook(input_file)

        # Save the Workbook as a PNG file
        workbook.save(output_file, aspose.cells.SaveFormat.PNG)

        print(f"Converted {filename} to {os.path.basename(output_file)}")