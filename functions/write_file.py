import os

def write_file(working_directory, file_path, content):
    work_dir = os.path.abspath(working_directory)
    target_file = work_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(work_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory {e}"
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: {file_path} is a directory, not a file'

    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Could not write to file "{file_path}": {str(e)}'