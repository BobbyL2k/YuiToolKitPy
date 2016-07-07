import os.path.isfile
import os.path.join
import os.listdir

from random import randint


def get_file_list(path):
    "Return List of file in the provided path"
    file_list = [file_name
                 for file_name in os.listdir(path)
                 if os.path.isfile(os.path.join(path, file_name))]
    file_list.sort()
    return file_list
