# generalutilities/FileHandler.py
import os

def read_file(file_path):
    """Reads a file and returns its contents as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Writes a string to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def create_directory(directory_path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
