# Cloud Automation Platform Architecture

## Overview

The Cloud Automation Platform is a Python application designed to demonstrate software engineering and cloud computing concepts. The project allows users to upload, store, search, and manage files while following a modular software design. The application currently stores files locally but is designed to be upgraded to Amazon Web Services (AWS) using Amazon EC2 and Amazon S3.

The goal of this project is to gradually transform a local Python application into a cloud-based application by implementing industry-standard technologies and best practices.

---

# Current Architecture

Current System Design

```
            User
              │
              ▼
      Python Application
              │
              ▼
      File Storage Module
              │
              ▼
     Local Storage Folder
      (data/uploads)
```

### Description

The application currently runs on a local computer.

When a user uploads a file, the Python application validates the file and copies it into the `data/uploads` directory. All uploaded files are stored locally on the same machine where the application is running.

The project is organized into multiple folders to separate responsibilities and improve maintainability.

Project Structure

```
cloud-automation-platform/

├── config/
├── data/
│   └── uploads/
├── logs/
├── scripts/
│   └── file_storage.py
├── main.py
├── README.md
├── Architecture.md
├── requirements.txt
└── .gitignore
```

---

# Current Workflow

1. The user starts the Python application.
2. The application displays a menu.
3. The user chooses to upload a file.
4. The application validates the file path.
5. The file is copied into the `data/uploads` directory.
6. The application confirms that the upload was successful.

---

# Current Limitations

Although the current design works well for development and testing, it has several limitations.

- Files only exist on the local computer.
- Files cannot easily be shared across multiple systems.
- If the computer is lost or damaged, uploaded files may also be lost.
- Storage capacity depends entirely on the local machine.
- The application is not yet cloud accessible.

---

# Planned S3 Upgrade

The next stage of the project is to migrate file storage from the local machine to Amazon S3 while hosting the application on an Amazon EC2 instance.

Future System Design

```
             User
               │
               ▼
       Python Application
               │
               ▼
        Amazon EC2 Server
               │
               ▼
        Amazon S3 Bucket
               │
               ▼
        Uploaded Files
```

Instead of copying uploaded files into the local `data/uploads` folder, the application will upload them directly into an Amazon S3 bucket.

This change allows the application to take advantage of cloud storage while keeping the rest of the application structure largely unchanged.

---

# Future Workflow

1. The user uploads a file.
2. The Python application validates the file.
3. The application sends the file to Amazon S3.
4. Amazon S3 stores the file securely.
5. The application confirms that the upload was successful.
6. The uploaded file can later be retrieved from Amazon S3.

---

# Benefits of Amazon S3

Migrating to Amazon S3 provides several advantages.

- Durable cloud storage
- Scalable storage for large numbers of files
- High availability
- Better reliability than local storage
- Easy integration with other AWS services
- Separation of application logic and storage
- Industry-standard cloud architecture

---

# System Components

## Python Application

The main application provides the user interface, processes user requests, validates files, and coordinates all storage operations.

## File Storage Module

The file storage module contains the functions responsible for uploading, retrieving, and managing files.

## Amazon EC2

Amazon EC2 will host the Python application on a Linux virtual server, allowing the application to run in the cloud.

## Amazon S3

Amazon S3 will store uploaded files securely and provide scalable cloud storage.

---

# Future Improvements

Planned improvements for future versions of the project include:

- Amazon S3 integration
- Logging system
- User authentication
- File downloads
- File deletion
- Database for file metadata
- REST API
- Web interface
- Automated backups
- Additional cloud automation features

---

# Conclusion

The Cloud Automation Platform is being developed using a modular design that separates application logic from file storage. The current implementation stores files locally, providing a simple environment for development and testing. The planned migration to Amazon EC2 and Amazon S3 will transform the application into a cloud-based solution that follows modern software engineering and cloud computing practices.