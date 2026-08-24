from scripts.file_storage import (
    create_storage,
    upload_file,
    list_files,
    read_file,
    delete_file
)
from scripts.logger import logger


def main():
    create_storage()

    while True:
        print("\n==============================")
        print("   CLOUD AUTOMATION PLATFORM")
        print("==============================")
        print("1. Upload File")
        print("2. List Files")
        print("3. Read File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                source_path = input("Enter file path: ")
                upload_file(source_path)
                print("File uploaded successfully.")

            elif choice == "2":
                files = list_files()

                if files:
                    print("\nFiles:")
                    for file in files:
                        print(file)
                else:
                    print("No files found.")

            elif choice == "3":
                filename = input("Enter filename: ")
                content = read_file(filename)
                print("\nFile Contents:")
                print(content)

            elif choice == "4":
                filename = input("Enter filename: ")
                delete_file(filename)
                print("File deleted successfully.")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid option.")

        except Exception as e:
            logger.error("Operation failed: %s", e)
            print(f"Error: {e}")


if __name__ == "__main__":
    main()