import pandas
import os
from shutil import copyfile
from pathlib import Path
import csv

path = Path("/media/dex/Data/Data/ics/uploads/test")
files = [x for x in path.glob('**/*') if x.is_file()]


def rename_image_files():
    for file in files:
        file_count += 1
        file.suffix().lower()
        new_file_name = file[:10] + file[-4:].lower()
        print("renaming   " + file)
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
        file = new_file_name
        print("renamed to " +file)
        
        if not file.startswith( '0' ):
            print('appending 0 to ' + file)
            os.rename(os.path.join(path, file), os.path.join(path, prefix + file))
            print('success!')
        else:
            print(file + ' name already clean! Skipping')
            print('File count = '+ str(file_count))