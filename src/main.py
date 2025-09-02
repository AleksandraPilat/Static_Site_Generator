import os
import shutil

from copystatic import copy_directory


def main():
    copy_directory("/Users/alekdandrapilat/BbootdevProjects/static_site_generator/static",
                   "/Users/alekdandrapilat/BbootdevProjects/static_site_generator/public")


if __name__ == "__main__":
    main()
