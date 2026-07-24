import os
import shutil

# This is the location where our files will be stored
STORAGE_PATH = "../data/uploads"


# Create the storage folder if it does not already exist
def create_storage():
    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH)
        print("Storage folder created")


# Save a file into our storage folder
def save_file(filename, content):
    file_path = os.path.join(STORAGE_PATH, filename)

    with open(file_path, "w") as file:
        file.write(content)

    print(f"{filename} saved successfully")


# Show all files currently stored
def list_files():
    files = os.listdir(STORAGE_PATH)

    if len(files) == 0:
        print("No files found")
    else:
        print("Stored files:")
        for file in files:
            print(file)


# Read a file from storage
def read_file(filename):
    file_path = os.path.join(STORAGE_PATH, filename)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()

        print(content)

    else:
        print("File does not exist")


# Delete a file from storage
def delete_file(filename):
    file_path = os.path.join(STORAGE_PATH, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{filename} deleted")

    else:
        print("File does not exist")


# Test the storage system
create_storage()

save_file("example.txt", "AWS cloud automation project")

list_files()

read_file("example.txt")

delete_file("example.txt")