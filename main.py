from scripts.logger import logger

from scripts.file_storage import (
    create_storage,
    upload_file,
    list_files,
    read_file,
    delete_file,
)


def menu():

    create_storage()

    while True:

        print("\n========== Cloud Automation Platform ==========")
        print("1. Upload File")
        print("2. List Files")
        print("3. Read File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        # Upload File
        if choice == "1":

            source_path = input("\nEnter the full path of the file: ")

            try:
                filename = upload_file(source_path)

                print(f"\n{filename} uploaded successfully!")

                logger.info(
                    "Operation=UPLOAD | File=%s | Status=SUCCESS",
                    filename
                )

            except FileNotFoundError:

                print("\nError: file missing.")

                logger.error(
                    "Operation=UPLOAD | File=%s | Status=FAILED",
                    source_path
                )

            except Exception as e:

                print("\nError: could not upload file.")

                logger.error(
                    "Operation=UPLOAD | File=%s | Status=FAILED | Error=%s",
                    source_path,
                    e
                )

        # List Files
        elif choice == "2":

            try:

                list_files()

                logger.info(
                    "Operation=LIST | File=ALL | Status=SUCCESS"
                )

            except Exception as e:

                print("\nError: could not list files.")

                logger.error(
                    "Operation=LIST | File=ALL | Status=FAILED | Error=%s",
                    e
                )

        # Read File
        elif choice == "3":

            filename = input("\nEnter the filename: ")

            try:

                read_file(filename)

                logger.info(
                    "Operation=READ | File=%s | Status=SUCCESS",
                    filename
                )

            except FileNotFoundError:

                print("\nError: file not found.")

                logger.error(
                    "Operation=READ | File=%s | Status=FAILED",
                    filename
                )

            except Exception as e:

                print("\nError: could not read file.")

                logger.error(
                    "Operation=READ | File=%s | Status=FAILED | Error=%s",
                    filename,
                    e
                )

        # Delete File
        elif choice == "4":

            filename = input("\nEnter the filename: ")

            try:

                deleted_file = delete_file(filename)

                print(f"\n{deleted_file} deleted successfully!")

                logger.info(
                    "Operation=DELETE | File=%s | Status=SUCCESS",
                    deleted_file
                )

            except FileNotFoundError:

                print("\nError: file not found.")

                logger.error(
                    "Operation=DELETE | File=%s | Status=FAILED",
                    filename
                )

            except Exception as e:

                print("\nError: could not delete file.")

                logger.error(
                    "Operation=DELETE | File=%s | Status=FAILED | Error=%s",
                    filename,
                    e
                )

        # Exit
        elif choice == "5":

            logger.info(
                "Operation=EXIT | File=N/A | Status=SUCCESS"
            )

            print("\nGoodbye!")
            break

        # Invalid Option
        else:

            print("\nInvalid option.")

            logger.warning(
                "Operation=MENU | File=N/A | Status=FAILED | Invalid Option=%s",
                choice
            )


menu()