# modules/file_organizer.py
import os
import shutil

def organize(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].upper()
            target_folder = os.path.join(folder_path, ext + "_Files")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))