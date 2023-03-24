import logging
import codecs
from pathlib import Path


def load_code(path: str) -> str:
    """
    This is a function for load code from file.
    """
    logging.warning("Executing load_code")
    try:
        with codecs.open(path, "r", "utf-8") as file:
            code = file.read()
            return code
    except Exception as e:
        print("No se puede abrir el archivo")
        print(e)


def save_code(path, name, code):
    """
    This is a function for save code to file.
    """
    logging.warning("Executing save_code")

    make_folders(path)

    # carpeta = Path(folder)
    # carpeta.mkdir(exist_ok=True)

    try:
        with codecs.open(f"{path}/{name}.py", "w", "utf-8") as file:
            file.write(code)
    except Exception as e:
        print("No se puede guardar el archivo")
        print(e)


def make_folders(path: str) -> list:
    """
    This is a function for make folders.
    in case they do not exist.
    """
    logging.warning("Executing make_folders")
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print("No se puede crear el directorio")
        print(e)
