# Simple Apps Project

Welcome to the **Simple Apps Project**! This repository contains a variety of small Python applications organized by categories. If you're completely new to programming, don't worry! This guide will help you step-by-step to get everything working.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Setting Up Python](#setting-up-python)
3. [Installing the Necessary Tools](#installing-the-necessary-tools)
4. [Running the Main Script](#running-the-main-script)
5. [Choosing an App to Run](#choosing-an-app-to-run)
6. [Fixing Common Issues](#fixing-common-issues)
7. [Where to Get More Help](#where-to-get-more-help)

---

## Getting Started

Before you can run any of the apps, you need to make sure your computer is ready. Below, you'll find instructions for setting up everything, even if this is your first time programming.

---

## Setting Up Python

### What is Python?

Python is a programming language that will allow your computer to run the apps in this project. First, you need to make sure Python is installed on your computer.

### Step 1: Check if Python is already installed

- Open your **Terminal** (Mac/Linux) or **Command Prompt** (Windows).
- Type the following command and press Enter:

    ```bash
    python --version
    ```

- If you see something like `Python 3.x.x`, you’re good to go. If not, follow the next step to install it.

### Step 2: Install Python

If Python isn't installed, you need to download and install it. Just search for "Python download" online, and download the latest version for your operating system. Follow the instructions to install it, and make sure to check the box that says "Add Python to PATH" during the installation.

Once it's installed, repeat Step 1 to check that Python is now recognized.

---

## Installing the Necessary Tools

### Step 1: Download the Project

You can download the entire project in two ways:

1. Click the **Download ZIP** button on the project page and extract the files to a folder.
2. If you're familiar with Git, you can clone the project to your computer.

### Step 2: Install the Required Libraries

The apps in this project use some extra tools (called "libraries") to work. Installing these tools is easy.

1. Open your **Terminal** (Mac/Linux) or **Command Prompt** (Windows).
2. Navigate to the folder where you saved the project using the `cd` command. For example:

    ```bash
    cd /path/to/your/project/folder
    ```

3. Now, install the required tools by running this command:

    ```bash
    pip install -r requirements.txt
    ```

   This will install everything the apps need to run.

### Step 3: Install ffmpeg (for media-related apps)

Some apps require **ffmpeg** for processing audio and video files. To install it:

- **Mac/Linux users**: Open your terminal and run:

    ```bash
    brew install ffmpeg
    ```

- **Windows users**: You can find a simple guide to install `ffmpeg` online by searching "install ffmpeg on Windows."

---

## Running the Main Script

### Step 1: Open the Terminal or Command Prompt

- **Windows**: Press `Win + R`, type `cmd`, and hit Enter.
- **Mac/Linux**: Open the Terminal app from your Applications folder.

### Step 2: Navigate to the Project Folder

Use the `cd` command to go to the folder where you saved the project. For example:

```bash
cd /path/to/your/project/folder
