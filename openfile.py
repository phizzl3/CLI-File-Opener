__version__ = "1.1.0"

import os
import platform


def open_file(file_path: str) -> None:
    if platform.system() == "Windows":
        os.startfile(file_path)
    else:
        os.system(f'open "{file_path}"')
