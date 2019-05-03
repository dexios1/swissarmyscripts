import os
from os.path import splitext
from PIL import Image

def rename():
	path = input("Enter file path (eg: C:\\Users\\Chris\\Docs\\Inflexion): ")
	tups = ('1','2','3','4','5','6','7','8','9')
	with os.scandir(path) as current_dir:
		for entry in current_dir:
			if entry.name.startswith(tups) and entry.is_file():
				filename, extension = splitext(os.path.basename(entry))
				new_filename = filename.split('_')[0]
				try:
					print('Converting...')
					new_filename = '0' + new_filename
					im = Image.open(os.path.join(path,filename + extension))
					im.save(os.path.join(path,new_filename + '.png'))
					os.remove(os.path.join(path,filename + extension))
				except OSError:
					print('Something went wrong converting {file}'.format(file=entry))
		print('\n All file names seem fine')
rename()