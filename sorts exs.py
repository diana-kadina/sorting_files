import os
file = 'doc.Pdf'
name, ext = os.path.splitext(file)
print(f'name for file: {name}, extension for file: {ext}')
#we need to del '.' and use lower case
file_ext = ext[1:]
print(file_ext.lower())

name_of_file = 'netflix.MP4'
file = os.path.splitext(name_of_file)
file_extens = file[1][1:].lower()
print(file_extens)
