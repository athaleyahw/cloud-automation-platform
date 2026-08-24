# Cloud Automation Platform

## Overview

Cloud Automation Platform is a Python-based file management
application designed to demonstrate application development,
file storage, logging, testing, Linux deployment, and cloud
infrastructure.

The application allows users to upload, list, read, and delete
files.

The project begins as a local Python application and is deployed
to AWS as part of the final implementation.

---

## Features

- Upload files
- List stored files
- Read files
- Delete files
- File error handling
- Application logging
- Unit testing
- Linux deployment
- Cloud-based file storage
- AWS infrastructure

---

## Technologies

- Python
- Linux
- Git
- GitHub
- Amazon EC2
- Amazon S3
- Amazon CloudWatch
- AWS IAM
- Boto3

---

## Project Structure

```text
cloud-automation-platform/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── Architecture.md
├── .gitignore
│
├── scripts/
│   ├── __init__.py
│   ├── file_storage.py
│   └── logger.py
│
├── tests/
│   ├── __init__.py
│   └── test_file_storage.py
│
├── data/
│   └── uploads/
│
└── logs/
    └── app.log