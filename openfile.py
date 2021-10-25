"""
Open an output file based on detected Operating System.
Supports Windows, Mac, & Linux.
"""

import platform


def openfile(f_path: str) -> None:
    """Open an output file based on Operating System.
    Supports Windows, Mac, & Linux.

    Args:
        f_path (str): Filepath for the file to be opened.
    """
    operating_system = platform.system()

    if operating_system == "Windows":
        import os
        os.startfile(f_path)
    else:
        import subprocess
        if operating_system == "Darwin":
            subprocess.run(f'open "{f_path}"', shell=True)
        elif operating_system == "Linux":
            subprocess.run(f'xdg-open "{f_path}"', shell=True)
