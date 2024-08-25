import shutil

source_folder = str(input("Enter the source folder path: "))
backup_folder = str(input("Enter the backup folder path: "))

shutil.copytree(source_folder, backup_folder)
print("Backup complete!")