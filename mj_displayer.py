import tkinter as tk
from tkinter import filedialog
import subprocess
import time
import os
import platform

def select_document():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Document")
    return file_path

def open_document(file_path):
    if platform.system() == "Windows":
        return subprocess.Popen(["start", "", file_path], shell=True)
    elif platform.system() == "Darwin":  # macOS
        return subprocess.Popen(["open", file_path])
    else:  # Linux
        return subprocess.Popen(["xdg-open", file_path])

def close_document(process):
    if platform.system() == "Windows":
        os.system(f"taskkill /F /PID {process.pid}")
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        process.terminate()

def main():
    document_path = select_document()
    if document_path:
        process = open_document(document_path)
        display_time = 10  # Display time in seconds
        time.sleep(display_time)
        close_document(process)

if __name__ == "__main__":
    main()
