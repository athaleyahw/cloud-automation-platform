import os
import shutil

from config.config import STORAGE_PATH
from scripts.logger import logger


def create_storage():
    """Create the uploads folder if it doesn't exist."""
    os.makedirs(STORAGE_PATH, exist_ok=True)
    logger.info("Storage folder ready.")


def upload_file(source_path):
    """
    Copy a file from the user's computer into storage.
    """

    if not os.path.exists(source_path):
        raise FileNotFoundError("File not found.")

    filename = os.path.basename(source_path)

    destination = os.path.join(STORAGE_PATH, filename)

    shutil.copy(source_path, destination)

    logger.info("Copied %s into storage.", filename)

    return filename


def list_files():
    """Display every stored file."""

    files = os.listdir(STORAGE_PATH)

    if not files:
        print("Storage is empty.")
        logger.info("Storage is empty.")
        return

    print("\nStored Files")

    for file in files:
        print(f"- {file}")

    logger.info("Listed all stored files.")


def read_file(filename):
    """Display the contents of a stored file."""

    file_path = os.path.join(STORAGE_PATH, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found.")

    logger.info("Opening file %s.", filename)

    with open(file_path, "r") as file:
        print("\n----- File Contents -----")
        print(file.read())
        print("-------------------------")


def delete_file(filename):
    """Delete a stored file."""

    file_path = os.path.join(STORAGE_PATH, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found.")

    os.remove(file_path)

    logger.info("Deleted %s from storage.", filename)

    return filename