"""

Open a specified (passed) file path in it's default application
based on detected Operating System.
Supports Windows, Mac, & Linux.

"""

__version__ = "1.0.0"


import os
import platform
import subprocess


def openfile(file_path: str) -> None:
    """Open specified file based on detected Operating System.
    Supports Windows, Mac, & Linux.

    Args:
        file_path (str): File path for the file to be opened.
    """
    # Get Operating System
    operating_system = platform.system()
    # Subprocess Operating Systems and their associated commands.
    subprocess_commands = {
        "Darwin": f"open \"{file_path}\"",
        "Linux": f"xdg-open \"{file_path}\"",
    }
    # Open based on detected operating system.
    if operating_system == "Windows":
        os.startfile(file_path)
    if operating_system in subprocess_commands:
        subprocess.run(subprocess_commands[operating_system],
                       check=False, shell=True)
