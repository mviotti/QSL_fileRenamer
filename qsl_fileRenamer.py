import os
import sys

if len(sys.argv) != 2:
    print('ERROR: Must the path to the QSLs. e.g.: python qsl_fileRenamer.py c:/qsl_images/')
    exit()

folder = sys.argv[1]

# append / to the folder
if folder[-1] != '/':
    folder += '/'

count = 0

for file_name in os.listdir(folder):
    name = file_name.split('.')[0] 
    ext = file_name.split('.')[1]
    current_name = name.split('_')[0]
    new_name = current_name + '.' + ext

    source = folder + file_name
    destination = folder + new_name
    if os.path.isfile(new_name):
        print(new_name + "The file already exists")
    else:
        print(source + " -> " + destination)
        os.rename(source, destination)
    
    count += 1

print(str(count) + ' files renamed')
