import pandas
import os
from shutil import copyfile
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-s", "--src", dest="src_path", help="input folder",
                    default="/media/dex/Data/ics/uploads/18-feb-2019/upload/")
parser.add_argument("-d", "--dst", dest="dst_path",
                    default="/home/dex/Documents/ICS/uploads/upload-21-mar-2019/payload_v/",
                    help="output folder")
parser.add_argument("-f", "--csv", dest="import_list_path",
                    default="/home/dex/Documents/ICS/filters/21-mar-2019.csv",
                    help="path to csv file containing filtered numbers")
args = parser.parse_args()
src_path = args.src_path
dst_path = args.dst_path
import_list_path = args.import_list_path
src_files = os.listdir(src_path)

# set up pandas list from csv files
print('reading import list')
colnames = ['MSISDN', 'Present']
data = pandas.read_csv(import_list_path, names=colnames)
upload_list = data['MSISDN']
src_file_list = []
indices = list(data.index.values)
# format upload list
for item in upload_list:
    item = str(item)
    print("read upload list item: " + item)
# build src file list
for file in src_files:
    src_file_list.append(file[:10])
    print("added {0} to list".format(file[:10]))

# filter and copy files for upload
print('copying files')
count = 0
n = 0
for upload_item in upload_list:
    n = 0
    for src_file in src_files:
        if str(upload_item) in src_file:
            count = count + 1
            print("{0} match found for {1}. Copying. . .".format(count, upload_item))
            copyfile(src_path+src_file, dst_path+src_file)
            data['Present'][n] = 'Yes'
        else:
            data['Present'][n] = 'No'
data.to_csv(import_list_path)
print("done for {0} images".format(count))