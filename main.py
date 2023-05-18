import os
import shutil

def organize_files(folder_path):
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    file_extensions = {}
    
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        
        if file_extension not in file_extensions:
    
            folder = os.path.join(folder_path, file_extension[1:])
            os.makedirs(folder, exist_ok=True)
            file_extensions[file_extension] = folder
        
        source_file = os.path.join(folder_path, file)
        destination_file = os.path.join(file_extensions[file_extension], file)
        shutil.move(source_file, destination_file)
    
    print("Files organized successfully!")

# Provide the path to the folder you want to organize
folder_path = "path/of/the/folder"
#Add suitable path depending on the OS
organize_files(folder_path)
