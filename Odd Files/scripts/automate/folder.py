import pyautogui
import time
import os

class FolderOpen:
    def __init__(self, base_path=os.getcwd()):
        """
        Initializes FolderOpen with an optional base path (defaults to current working directory).
        :param base_path: The base directory for relative paths.
        """
        self.base_path = base_path

    def open_folder(self, folder_path):
        """
        Opens a folder using its relative path by converting it to an absolute path.
        :param folder_path: The relative path to the folder to open.
        """
        # Convert the relative path to an absolute path
        absolute_path = os.path.join(self.base_path, folder_path)

        # Ensure the folder exists
        if not os.path.isdir(absolute_path):
            print(f"Error: The path {absolute_path} does not exist.")
            return
        
        # Step 1: Open the Run dialog (Windows shortcut: Win+R)
        pyautogui.hotkey('win', 'r')
        time.sleep(1)  # Wait for the Run dialog to appear

        # Step 2: Type the absolute path into the Run dialog
        pyautogui.write(absolute_path)
        pyautogui.press('enter')  # Press Enter to open the folder
        time.sleep(1)  # Wait for the folder to open

# Example Usage:
'''
folder = FolderOpen()  # Default base path is current working directory
folder.open_folder('filesDel')  # Relative path, e.g., 'Documents' folder inside current directory
'''
