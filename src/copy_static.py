import os
import shutil


def clear_destination_contents(destination_dir: str) -> None:
    destination_dir_contents = os.listdir(destination_dir)
    if destination_dir_contents:
        for path in destination_dir_contents:
            full_path = os.path.join(destination_dir, path)
            if os.path.isfile(full_path):
                os.remove(full_path)
            else:
                shutil.rmtree(full_path)

def copy_static_contents_to_public(source_dir: str, destination_dir: str) -> None:
    source_dir_contents = os.listdir(source_dir)
    if not source_dir_contents:
        raise ValueError(f"The source directory must contain contents: {source_dir}")
    for path in source_dir_contents:
        source_dir_path = os.path.join(source_dir, path)
        destination_dir_path = os.path.join(destination_dir, path)
        if os.path.isdir(source_dir_path):
            os.mkdir(destination_dir_path)
            copy_static_contents_to_public(source_dir_path, destination_dir_path)
        else:
            shutil.copy(source_dir_path, destination_dir_path)
            print(f"Copied {source_dir_path} to {destination_dir_path}")

def copy_static_to_public(source_dir: str, destination_dir: str) -> str:
    try:
        source_dir_abs = os.path.abspath(source_dir)
        destination_dir_abs = os.path.abspath(destination_dir)
        if not os.path.exists(source_dir_abs):
            raise FileNotFoundError(f"File path does not exist: {source_dir}")
        if not os.path.exists(destination_dir_abs):
            raise FileNotFoundError(f"File path does not exist: {destination_dir}")
        if not os.path.isdir(source_dir_abs):
            raise NotADirectoryError(f"Path is not a directory: {source_dir}")
        if not os.path.isdir(destination_dir_abs):
            raise NotADirectoryError(f"Path is not a directory: {destination_dir}")
        clear_destination_contents(destination_dir_abs)
        copy_static_contents_to_public(source_dir_abs, destination_dir_abs)
        return f"Successfully copied contens of {source_dir} to {destination_dir}"
    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        return f"Error: {str(error)}"
    