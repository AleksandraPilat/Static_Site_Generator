import shutil


def copy_directory(src: str, dst: str):
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Copied contents of '{src}' → '{dst}'")
    except FileNotFoundError:
        print(f"Source directory '{src}' not found.")
    except IOError as e:
        print(f"Error writing to destination '{dst}': {e}")
