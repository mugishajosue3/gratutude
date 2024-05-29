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

def execute_command_after_delay(command, delay):
    time.sleep(delay)
    subprocess.Popen(command, shell=True)

def main():
    while True:
        document_path = select_document()
        if not document_path:
            # No file selected, exit the loop
            break
        
        process = open_document(document_path)
        display_time = 10  # Display time in seconds
        time.sleep(display_time)
        close_document(process)
        
        # Execute the command after 3 seconds
        command = "echo 'Command executed after 3 seconds'"  # Replace with your command
        execute_command_after_delay(command, 3)

    # Destroy the Tkinter root window
    tk.Tk().destroy()

if __name__ == "__main__":
    main()
