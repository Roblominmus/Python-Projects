import os
import shutil
import time

def organize():
    source_dir = "C:\\Users\\Admin\\Downloads"
    dest_base_dir = "C:\\Users\\Admin\\Downloads"  # You can change this to the base directory where you want to organize files.

    extensions_dict = {
        'Documents': ['.pdf', '.docx', '.csv', '.txt', '.pptx', '.pptm', '.potx', '.potm', '.ppsx', '.pps', '.ppsm'],
        'Code': ['.py', '.html', '.cs', '.css', '.scss', '.js', '.php', '.c', '.cpp', '.sql'],
        'Archives': ['.zip', '.rar'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif', '.heic', '.webp', '.raw', '.cr2', '.nef'],
        'Run Files': ['.bat', '.exe']
    }

    for item in os.listdir(source_dir):
        full_path = os.path.join(source_dir, item)

        if os.path.isfile(full_path):
            extension = os.path.splitext(item)[1]
            for key, value in extensions_dict.items():
                if extension in value:
                    dest_dir = os.path.join(dest_base_dir, key)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(full_path, os.path.join(dest_dir, item))

while True:
    organize()
    time.sleep(60)
