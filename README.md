Image Batch Renamer

A simple and efficient Python utility to sequentially rename image files in a directory. This script is perfect for organizing datasets, photography projects, or web assets by converting chaotic filenames into a clean, numbered sequence.

🚀 Features

Sequential Numbering: Renames files starting from any integer you choose (default is 1 or 11).

Format Preservation: Automatically detects and maintains the original file extension (e.g., .jpg, .png, .webp).

Alphanumeric Sorting: Files are sorted before renaming to ensure the sequence follows a logical order.

Error Handling: Includes a try-except block to prevent the script from crashing if a file is in use or restricted.

Wide Compatibility: Supports .jpg, .jpeg, .png, .bmp, .gif, and .webp.

📂 Workflow Process

The script follows a structured 4-step process to ensure your files are handled correctly:

Scanning: The script looks into the provided folder_path and identifies files matching the supported image extensions.

Sorting: To avoid random ordering, it sorts the file list alphabetically.

Indexing: It iterates through the list, taking the start_number and adding the current loop index to create a new filename.

Renaming: It executes os.rename() to apply the changes to the file system.

🛠️ Usage

1. Prerequisites

You need Python 3.x installed. This script uses the built-in os module, so no external libraries (like pip install) are required.

2. Configuration

Open the script and edit the SETTINGS section at the bottom:

# Set the path to your image folder
my_folder = r"C:\Users\YourName\Pictures\Project" 

# Set the number to start renaming from
rename_images(my_folder, start_number=1)


3. Execution

Run the script from your terminal or command prompt:

python your_script_name.py


📋 Example

Before:

vacation_photo.jpg

IMG_0023.png

screenshot_final.jpeg

After (with start_number=1):

1.jpg

2.png

3.jpeg

⚠️ Important Safety Note

Always back up your images before running the script. This utility performs "in-place" renaming, meaning it modifies the files directly in your folder. Once renamed, the original filenames cannot be automatically restored by the script.

📜 License

Distributed under the MIT License. See LICENSE for more information.
