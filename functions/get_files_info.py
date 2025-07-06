import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    work_dir = os.path.abspath(working_directory)
    target_dir = work_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(work_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(f'- {file}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(files_info)
    except Exception as e:
        return f'Error: Could not list files in "{directory}": {str(e)}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)