import os

def rename_images(folder_path, start_number=11):
    # Supported image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    
    # Get a list of files and sort them to ensure order
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)])
    
    if not files:
        print("No images found in the specified directory.")
        return

    print(f"Found {len(files)} images. Starting rename process...")

    for index, filename in enumerate(files):
        # Get the file extension (e.g., .jpg)
        extension = os.path.splitext(filename)[1]
        
        # Define the new name
        new_name = f"{start_number + index}{extension}"
        
        # Define full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

    print("Done!")

# --- SETTINGS ---
# Replace this with the actual path to your folder
my_folder = r"path of your images folder ......" 
rename_images(my_folder, start_number=1)