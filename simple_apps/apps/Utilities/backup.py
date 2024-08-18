import os
import shutil
import time
from tqdm import tqdm
import filecmp

def get_folder_path(prompt):
    folder_path = input(prompt)
    if not os.path.exists(folder_path):
        print("Path does not exist. Please try again.")
        return get_folder_path(prompt)
    return folder_path

def backup_initial(src_folder, dest_folder):
    print("Backing up files initially...")
    for root, dirs, files in os.walk(src_folder):
        relative_path = os.path.relpath(root, src_folder)
        dest_path = os.path.join(dest_folder, relative_path)
        os.makedirs(dest_path, exist_ok=True)
        for file in tqdm(files, desc="Copying files", unit="file"):
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            shutil.copy2(src_file, dest_file)

def monitor_and_backup(src_folder, dest_folder, deleted_folder):
    print(f"Monitoring changes in {src_folder}...")
    file_state = {}

    while True:
        time.sleep(5)  # Adjust the sleep time as per your preference
        for root, dirs, files in os.walk(src_folder):
            relative_path = os.path.relpath(root, src_folder)
            dest_path = os.path.join(dest_folder, relative_path)

            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_path, file)

                # If file does not exist in the backup location, copy it
                if not os.path.exists(dest_file):
                    os.makedirs(dest_path, exist_ok=True)
                    shutil.copy2(src_file, dest_file)
                    print(f"{file} - New file copied.")

                # If the file exists but is modified, update the backup
                elif not filecmp.cmp(src_file, dest_file):
                    shutil.copy2(src_file, dest_file)
                    print(f"{file} - File changed, updating backup.")

                # Track the current state of the file
                file_state[src_file] = time.time()

        # Check for deleted files and move them to the deleted folder
        for root, dirs, files in os.walk(dest_folder):
            relative_path = os.path.relpath(root, dest_folder)
            src_path = os.path.join(src_folder, relative_path)

            for file in files:
                dest_file = os.path.join(root, file)
                src_file = os.path.join(src_path, file)

                if not os.path.exists(src_file):
                    deleted_dest_path = os.path.join(deleted_folder, relative_path)
                    os.makedirs(deleted_dest_path, exist_ok=True)
                    shutil.move(dest_file, os.path.join(deleted_dest_path, file))
                    print(f"{file} - File deleted in source, moved to 'deleted files' folder.")

if __name__ == "__main__":
    # Get user input for folder locations
    src_folder = get_folder_path("Enter the folder to monitor: ")
    dest_folder = get_folder_path("Enter the backup folder location: ")
    deleted_folder = os.path.join(dest_folder, "deleted_files")

    # Initial backup
    backup_initial(src_folder, dest_folder)

    # Start monitoring and backing up changes
    monitor_and_backup(src_folder, dest_folder, deleted_folder)
