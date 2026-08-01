import os
from dotenv import load_dotenv


def get_file_content(working_directory: str, file_path: str) -> str:
    load_dotenv()
    max_chars = int(os.getenv("MAX_CHARS"))
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_tar_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if valid_tar_file == False: return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(target_file) == False: return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, "r") as file_contents:
            read_output = file_contents.read(max_chars)
            if file_contents.read(1):
                return f'[...File "{file_path}" truncated at {max_chars} characters] \n {read_output}'
            return read_output

    except Exception as e:
        return f"Error: {e}"