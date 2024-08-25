import os

folder_path = input("Enter the folder path (default is /home): ")
folder_path = "/home" if folder_path == "" else folder_path

def rename_files(prefix, new_prefix):
    for filename in os.listdir(folder_path):
        if filename.startswith(prefix):
            new_filename = filename.replace(prefix, new_prefix)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

prefix = input("Enter the prefix to rename: ")
new_prefix = input("Enter the new prefix: ")

rename_files(prefix, new_prefix)