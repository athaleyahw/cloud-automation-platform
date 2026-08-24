import os
from config import STORAGE_PATH
from scripts.logger import logger


def create_storage():
    os.makedirs(STORAGE_PATH, exist_ok=True)
    logger.info("Storage directory checked: %s", STORAGE_PATH)


def upload_file(source_path):
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"File not found: {source_path}")

    filename = os.path.basename(source_path)
    destination = os.path.join(STORAGE_PATH, filename)

    with open(source_path, "rb") as source:
        with open(destination, "wb") as target:
            target.write(source.read())

    logger.info("Uploaded file: %s", filename)


def list_files():
    create_storage()

    files = os.listdir(STORAGE_PATH)
    logger.info("Listed files")

    return files


def read_file(filename):
    filepath = os.path.join(STORAGE_PATH, filename)

    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    logger.info("Read file: %s", filename)

    return content


def delete_file(filename):
    filepath = os.path.join(STORAGE_PATH, filename)

    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filename}")

    os.remove(filepath)

    logger.info("Deleted file: %s", filename)