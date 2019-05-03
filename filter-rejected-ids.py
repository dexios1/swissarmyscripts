import os
from pathlib import Path
import csv

path = Path("/media/dex/Data/Data/ics/uploads/test")
image_data_file= Path("/media/dex/Data/Data/ics/uploads/test/image_data.csv")
print("is {} a directory: {}".format(path.absolute(), path.is_dir()))

def filter_rejected_list():
    images = [x for x in path.glob('**/*') if x.is_file()]
    columns = ["Number"] + build_extensions_list(images)
    print(columns)
    image_data = build_image_set(images)
    return image_data

def build_image_data_file():
    image_data = filter_rejected_list()
    for key, value in image_data.items():
        with open(image_data_file, 'w', newline='') as data_file:
            wr = csv.writer(data_file, quoting=csv.QUOTE_ALL)
            temp_list = [key]+ list(value)
            print("writing {} to file".format(str(temp_list)))
            wr.writerow(temp_list)

# checks file list to build a set of a list of unique file extensions
def build_extensions_list(images):
    for image in images:
        extensions = set([])
        extensions.add(image.suffix)
        return list(extensions)

def build_image_set2(images):
    image_list = []
    phone_numbers = []
    for image in images:
        if image.stem not in phone_numbers:
            image_list[image.stem] = set([])
        image_list[image.stem].add(image.suffix)
    return image_list


def build_image_set(images):
    image_dict = dict()
    for image in images:
        if image.stem not in image_dict:
            image_dict[image.stem] = set([])
        image_dict[image.stem].add(image.suffix)
    return image_dict


build_image_data_file()
# for key, value in image_data.items():
#     print([key]+ list(value))
# print(image_data)
