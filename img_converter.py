"""Converts png, bmp and gif to jpg, removes descriptions and resizes the image to a maximum of 1920x1080."""

from PIL import Image
import os
from pathlib import Path
from shutil import move


path = Path('/home/dex/Documents/ICS/uploads/upload-08-apr-2019/client_master-chris/payload/')
trash_path = Path('/home/dex/Documents/ICS/uploads/upload-08-apr-2019/client_master-chris/payload_trash')
failed_path = Path('/home/dex/Documents/ICS/uploads/upload-08-apr-2019/client_master-chris/payload_fail')
# 18-feb-2019/images/

files = files = [x for x in path.glob('**/*') if x.is_file()]
print(files)
file_count = 0
fail_count = 0

for file in files:
  file_count += 1
  fail = False
  if file.suffix == '.bmp' or file.suffix == '.jpg' or file.suffix == 'jpeg':
      print(file.name)  
      try:
          image = Image.open(file)
          image.save(file.with_suffix('.png'), 'png')
      except IOError:
          print("error reading image file!")
          fail = True
          fail_count = fail_count + 1
          # file.rename(failed_path.joinpath(file.name))
          # print("failed to convert {}. Moved to {}".format(file.stem, file.absolute))
          pass
      print("{} converted to {}".format(file.suffix, file.name))
      filename = str(file.absolute)
    #   move file to trash folder
      if fail == True:
        file.rename(failed_path.joinpath(file.name))
        print("moved {} to {}".format(file.name, str(file.absolute() )) )
      # move(str(file.absolute), str(trash_path))
print("Fail count = {}".format(fail_count))