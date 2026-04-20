import os
import shutil

source = "your_folder_path"

for file in os.listdir(source):
    if file.endswith(".jpg"):
        os.makedirs("Images", exist_ok=True)
        shutil.move(file, "Images")
    elif file.endswith(".pdf"):
        os.makedirs("PDFs", exist_ok=True)
        shutil.move(file, "PDFs")