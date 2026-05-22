import os
def organize_files():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'PDFs': ['.pdf'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov']
    }
    
    # Create folders
    for folder in file_types.keys():
        folder_path = os.path.join(current_directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for file in files:
        file_path = os.path.join(current_directory, file)
        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    destination = os.path.join(current_directory, folder, file)
                    os.rename(file_path, destination)
                    print(f'Moved: {file} to {folder}/')
                    break

if __name__ == "__main__":
    organize_files()