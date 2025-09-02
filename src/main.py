import os
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "/Users/alekdandrapilat/BbootdevProjects/static_site_generator/static"
dir_path_public = "/Users/alekdandrapilat/BbootdevProjects/static_site_generator/public"
dir_path_content = "/Users/alekdandrapilat/BbootdevProjects/static_site_generator/content"
template_path = "/Users/alekdandrapilat/BbootdevProjects/static_site_generator/template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()
