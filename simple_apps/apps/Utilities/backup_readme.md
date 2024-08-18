# Folder Monitor and Backup Script

This script monitors a specified folder, backs it up to another location, and keeps the backup up-to-date by copying any new or modified files. Deleted files in the source folder will be moved to a "deleted files" folder in the backup location. The script is easy to use and requires no programming knowledge!

## Features
- **Initial Backup**: Creates a backup of all files the first time the script runs.
- **Continuous Monitoring**: Monitors changes (new files, modifications, deletions) and updates the backup accordingly.
- **Deleted Files Handling**: Moves deleted files from the source to a "deleted files" folder in the backup location.
- **Loading Bar**: Shows a progress bar when copying files.
- **Terminal Output**: Displays messages for every file backed up or updated.

## Requirements

Before running this script, you need to have Python installed on your system. If you don’t have Python installed, follow these steps:

### Step 1: Install Python

1. Go to the [Python website](https://www.python.org/downloads/).
2. Download the latest version of Python.
3. Run the installer and make sure to check the option **“Add Python to PATH”** during the installation.
4. After installation, open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and type `python --version` to ensure Python is installed correctly.

### Step 2: Install Required Dependencies

This script uses a Python library called `tqdm` to show the loading bar. To install this library:

1. Open a terminal (Command Prompt on Windows or Terminal on macOS/Linux).
2. Run the following command:

```bash
pip install tqdm
