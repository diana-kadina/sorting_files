import os
import shutil

path = 'your_path'
files = os.listdir(path)

exts_to_folder = {
    'Text': ['txt', 'doc', 'docx', 'pdf'], 
    'Image': ['jpg', 'jpeg', 'png', 'gif'], 
    'Audio': ['mp3', 'wav', 'aac', 'flac'], 
    'Video': ['mp4', 'mov', 'avi', 'mkv'], 
    'Jupyter': ['ipynb'], 
    'CSV': ['csv'], 
    'Excel': ['xls', 'xlsx'], 
    'ZIPS': ['zip'], 
    'PowerPoint': ['ppsx', 'ppt', 'pptm', 'pptx'],
    'Python': ['py']
}

#creating folders
for folder in exts_to_folder.keys():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path): 
        os.makedirs(folder_path) #creating folder if it does not exist


for file in files:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):  #checks is that a file
        file_ext = os.path.splitext(file) #name of file, exts
        file_ext = file_ext[1][1:].lower()  #getting extensions of files in lower case
        for folder, exts in exts_to_folder.items(): #key-value pairs
               if file_ext in exts: 
                    full_path=os.path.join(path, folder, file)
                    shutil.move(file_path, full_path)
                    print(f'{file} moved to Folder: {folder}')
                    break

print('done')
