import tkinter as tk
from tkinter import filedialog
import subprocess
import time
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
        subprocess.call(["taskkill", "/F", "/PID", str(process.pid)])
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        process.terminate()

def main():
    opened_processes = []

    while True:
        document_path = select_document()
        if not document_path:
            # No file selected, exit the loop
            break
        
        process = open_document(document_path)
        opened_processes.append(process)
        time.sleep(120)  # Keep the document open for 10 seconds
        close_document(process)
    
    # Wait for 3 seconds before executing the taskkill command
    time.sleep(3)

    # Execute the taskkill command to kill all running tasks
    if platform.system() == "Windows":
        subprocess.call('taskkill /F /FI "STATUS eq RUNNING"', shell=True)

    # Close all opened files
    for process in opened_processes:
        close_document(process)
    
    # Destroy the Tkinter root window
    tk.Tk().destroy()

if __name__ == "__main__":
    main()
