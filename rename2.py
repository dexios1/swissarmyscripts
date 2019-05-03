import os
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-f", "--folder", dest="path", help="input folder",
                    default="")
parser.add_argument("-p", "--prefix", dest="prefix", help="prefix to append to files for renaming",
                    default="0")
args = parser.parse_args()

path = args.path

files = os.listdir(path)
print(files)
prefix = args.prefix
file_count = 0

for file in files:
  file_count += 1
  new_file_name = file.lower()
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
    