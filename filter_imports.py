import pandas
import os
from shutil import copyfile
from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument("-s", "--src", dest="src_path", help="input folder",
                    default="/media/dex/Data/ics/uploads/18-feb-2019//")
parser.add_argument("-d", "--dst", dest="dst_path",
                    default="/home/dex/Documents/ICS/uploads/upload-21-mar-2019/payload/",
                    help="output folder")
parser.add_argument("-f", "--csv", dest="import_list_path",
                    default="/home/dex/Documents/ICS/filters/21-mar-2019",
                    help="path to csv file containing filtered numbers")
args = parser.parse_args()
src_path = args.src_path
dst_path = args.dst_path
import_list_path = args.import_list_path
src_files = os.listdir(src_path)

# fix paths
if dst_path.endswith('/') == False:
    dst_path = dst_path + "/"
if src_path.endswith('/') == True:
    src_path = src_path + "/"
# set up pandas list from csv files
print('reading import list')
colnames = ['MSISDN', 'Present']
data = pandas.read_csv(import_list_path, names=colnames)
upload_list = data['MSISDN']
src_file_list = []
# format upload list
for item in upload_list:
    print(item)
    item = "0" + item
    print("read upload list item: " + item)
# build src file list
for file in src_files:
    src_file_list.append(file[:10])
    print("added {0} to list".format(file[:10]))

# filter and copy files for upload
print('copying files')
count = 0
files = []
for upload_item in upload_list:
    present = False
    for src_file in src_files:
        if str(upload_item) in src_file:
            count = count + 1
            print("{0} match found for {1}. Copying. . .".format(count, upload_item))
            copyfile(src_path+src_file, dst_path+src_file)
            present = True
    files.append({'MSISDN': str(upload_item), 'Present': present})
for file in files:
    if file['Present'] == True:
        print(file)
# print(upload_list)
keys = files[0].keys()
with open('/home/dex/Documents/ICS/uploads/upload-08-apr-2019/upload_sheet.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(files)
print("done for {0} images".format(count))