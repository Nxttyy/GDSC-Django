import os
import shutil
from datetime import datetime, timedelta

def Flist(directory="."):
    files = []
    for dp, dn, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(dp, filename))
    return files

def is_recently_modified(file_path, days=1):
    now = datetime.now()
    file_stat = os.stat(file_path)
    modified = datetime.fromtimestamp(file_stat.st_mtime)
    created = datetime.fromtimestamp(file_stat.st_ctime)
    delta_modified = now - modified
    delta_created = now - created
    return delta_modified < timedelta(days=days) or delta_created < timedelta(days=days)

def update_file(file_path):
    with open(file_path, 'a') as file:
        file.write('\n#Updated at: ' + str(datetime.now()))

def create_last_24hours_folder():
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files_to_last_24hours(files):
    for file in files:
        try:
            shutil.move(file, os.path.join("last_24hours", os.path.basename(file)))
        except shutil.SameFileError:
            print(f"file[{os.path.basename(file)}] already exists")

def copy_files_to_last_24hours(files):
    for file in files:
        try:
            shutil.copy(file, os.path.join("last_24hours", os.path.basename(file)))
        except shutil.SameFileError:
            print(f"file[{os.path.basename(file)}] already exists")



def main():
    current_directory = os.getcwd()
    files_to_update = []
    # Selection
    for file in Flist(current_directory):
        if is_recently_modified(file):
            files_to_update.append(file)
    # Creation
    create_last_24hours_folder()
    # Updating TEXT
    for files in files_to_update:
        update_file(files)
    # Moving
    # move_files_to_last_24hours(files_to_update)
        
    # Copying
    copy_files_to_last_24hours(files_to_update)

main()

#Updated at: 2024-02-26 21:31:43.765028
#Updated at: 2024-02-26 21:33:49.492851