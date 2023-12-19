"""
Open a specified (passed) file path in it's default application
based on detected Operating System.
Supports Windows, Mac, & Linux.
"""

import platform
import subprocess


def open_file(file_path: str) -> None:
    """Open specified file based on detected Operating System.
    Supports Windows, Mac, & Linux.

    Args:
        file_path (str): File path for the file to be opened.
    """
    # Get Operating System
    operating_system = platform.system()
    # Operating Systems and their associated commands.
    command = {
        "Windows": f"start {file_path}",
        "Darwin": f"open {file_path}",
        "Linux": f"xdg-open {file_path}",
        "NA": "echo \"Operating System not supported\""
    }
    # Run open command based on above.
    subprocess.run(command.get(operating_system,
                   command["NA"]), check=True, shell=True)
