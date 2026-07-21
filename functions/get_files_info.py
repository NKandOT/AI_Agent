import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_tar_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_tar_dir == False: return f'Error: Cannot list "{directory}" as it is outside the working directory'
    if os.path.isdir(target_dir) == False: return f'Error: "{directory}" is not a directory'
    list_dir = os.listdir(target_dir)
    success_output = ""
    try:
        for item in list_dir:
            item_path = os.path.join(target_dir, item)
            success_output += f"    - {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)} \n"
    except Exception as e:
        return f"Error: {e}"
    return success_output
    
    