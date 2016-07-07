import cv2


def load_images(file_list):
    result = []
    for file in file_list:
        result.append(cv2.imread(file))
    return result
