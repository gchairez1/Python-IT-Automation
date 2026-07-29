"""
=========================================================
BackupUtility.py
Author: Gonzalo Chairez

Description:
Creates a backup of a selected folder while
preserving directory structure and timestamps.

Python IT Automation Toolkit
=========================================================
"""

import shutil
import os
import time

print("=" * 60)
print("              BACKUP UTILITY")
print("=" * 60)

source = input("Enter source folder: ").strip()
destination = input("Enter destination folder: ").strip()

if not os.path.exists(source):
    print("\n[ERROR] Source folder does not exist.")
    exit()

if not os.path.exists(destination):
    os.makedirs(destination)

folder_name = os.path.basename(os.path.normpath(source))
backup_path = os.path.join(destination, folder_name)

start_time = time.time()

files_copied = 0

for root, dirs, files in os.walk(source):

    relative_path = os.path.relpath(root, source)
    target_folder = os.path.join(backup_path, relative_path)

    os.makedirs(target_folder, exist_ok=True)

    for file in files:

        source_file = os.path.join(root, file)
        destination_file = os.path.join(target_folder, file)

        try:
            shutil.copy2(source_file, destination_file)
            files_copied += 1
            print(f"Copied: {source_file}")

        except Exception as e:
            print(f"Failed: {source_file}")
            print(e)

elapsed = round(time.time() - start_time, 2)

print("\n" + "=" * 60)
print("BACKUP COMPLETE")
print("=" * 60)
print(f"Files Copied : {files_copied}")
print(f"Destination  : {backup_path}")
print(f"Time Elapsed : {elapsed} seconds")
print("=" * 60)
