# File Organizer

A Python script that automatically sorts files in a directory based on their file extensions and optional keyword filtering.

## Features

- **Extension-based sorting**: Organizes files into folders based on their file type.
- **Keyword filtering**: Optionally filter files by keyword in the filename (case-sensitive).

## Requirements

- Python 3.x

## Installation

1. Download `main.py`.
2. No additional installation needed!

## Usage

### Basic Setup

1. Open the script in a text editor.
2. Update the `directory` variable with the path to the folder you want to organize:
   ```python
   directory = r"C:\Users\YourName\Desktop\MyFolder"
   ```

3. Run the script:
   ```bash
   python main.py
   ```

### Configuration Options

#### Sort by Extension Only

Leave the `keyword` variable empty to sort all files by their extensions:
```python
keyword = ""    # Matches all files
```

#### Sort by Keyword

Add a keyword to only move files with that word in their filename:
```python
keyword = "vacation"    # Only moves files like "vacation_photo.jpg"
```
**Note**: Keyword matching is case-sensitive.

#### Custom Folder Name

Use `new_folder` to override the default extension-based folder names:
```python
keyword = "2024"
new_folder = "2024 Files"   # All matching files go here instead of "Images", "Videos", etc.
```

#### Add Custom Extensions

Add or modify file extensions in the `extensions` dictionary:
```python
extensions = {
    ".jpg": "Images",
    ".mp4": "Videos",
    ".your_extension": "Your Folder Name"
}
```

## Example Scenarios

### Scenario 1: Organize All Files
```python
directory = r"C:\Users\kathe\Desktop\Downloads"
keyword = ""
new_folder = ""
```
Result: All JPGs go to "Images", all MP4s go to "Videos", etc.

### Scenario 2: Organize Vacation Photos Only
```python
directory = r"C:\Users\kathe\Desktop\Photos"
keyword = "vacation"
new_folder = "Vacation 2024"
```
Result: Only files with "vacation" in the name get moved to "Vacation 2024" folder.

### Scenario 3: Organize Work Documents
```python
directory = r"C:\Users\kathe\Desktop\Work"
keyword = "report"
new_folder = ""
```
Result: Files like "report_Q1.pdf" go to "Documents", "report_data.xlsx" goes to "Excel Sheets".


## Important Notes

⚠️ **File overwrites**: If a file with the same name already exists in the destination folder, it will be overwritten without warning.

⚠️ **Case sensitivity**: Keyword matching is case-sensitive (`"dog"` ≠ `"Dog"`).

## Troubleshooting

**"Path not found" error**: Make sure the directory path is correct and exists.

**Files not moving**: Check that the file extension is in the `extensions` dictionary and the keyword matches (if used).
