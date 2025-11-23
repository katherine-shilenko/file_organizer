import os
import shutil

directory = r""    # <--- UPDATE WITH THE DIRECTORY PATH YOU'D LIKE TO HAVE SORTED

# UPDATE WITH THE KEYWORD YOU'D LIKE TO USE FOR SORTING
# Example file: my_dog.jpg -> keyword = "dog"
# Leave empty to match all files
keyword = ""

# IF SORTING BY KEYWORD, ADD NEW FOLDER NAME HERE
# Otherwise, use extensions below
new_folder = ""

# ADD EXTENSIONS AS NEEDED
# Format: ".extension": "Desired Folder Name"
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".py": "Python Projects",
    ".zip": "Archives",
    ".pptx": "Power Points",
    ".csv": "Excel Sheets",
    ".xlsx": "Excel Sheets",
    ".exe": "Executables",
    ".js": "JavaScript",
    ".mjs": "JavaScript",
    ".css": "CSS"
}

try:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            if extension in extensions and keyword in filename:
                if new_folder == "":
                    folder_name = extensions[extension]
                else:
                    folder_name = new_folder
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder_name} folder.")
            else:
                print(f"Skipped {filename}. Unknown file extension or keyword.")

        else:
            print(f"Skipped {filename}. It is a directory.")

    print("File organization completed.")

except OSError as e:
    print(f"Path not found: {e.filename}")
