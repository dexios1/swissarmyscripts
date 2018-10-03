import os
path = '/home/dex/Documents/MTN IPO/Upload 20092018'
files = os.listdir(path)
print(files)
prefix = '0'

for file in files:
  print('renaming ' + file)
  os.rename(os.path.join(path, file), os.path.join(path, prefix + file))
  print('success!')