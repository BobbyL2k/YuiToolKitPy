import os

from random import randint


def get_file_list(path, as_path=False):
    "Return List of file in the provided path"
    file_list = [os.path.join(path, file_name) if as_path else file_name
                 for file_name in os.listdir(path)
                 if os.path.isfile(os.path.join(path, file_name))]
    file_list.sort()
    return file_list
