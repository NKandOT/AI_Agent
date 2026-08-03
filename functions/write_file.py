import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_tar_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if valid_tar_file == False: return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(target_file) == False:
        os.makedirs(target_file, exist_ok=True)
        with open(target_file, "w") as create:
            create.write("")
    if os.path.isdir(target_file) == True: return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        with open(target_file, "w") as write_content:
            write_content.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"