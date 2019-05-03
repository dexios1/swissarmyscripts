import os
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("-f", "--folder", dest="path", help="input folder",
                    default="")
parser.add_argument("-p", "--prefix", dest="prefix", help="prefix to append to files for renaming",
                    default="")
args = parser.parse_args()

path = Path(args.path)

# get files into array
files = files = [x for x in path.glob('**/*') if x.is_file()]

for file in files:
    file.suffix = "no"
    print(file.suffix)

print(path)