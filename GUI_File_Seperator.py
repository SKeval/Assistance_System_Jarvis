import os,shutil

dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
'video_extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
'documents_extensions' : ('.doc','.pdf','.txt')
}


folderpath = input('enter folder path : ')

def file_finder(folder_path, file_extension):
    files = []
    
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    
    return files 
    # return [file for file in os.listdir(folder_path) for extension in file_extension  if file.endswith(extension)]           
            
            

for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
  
    for item in (file_finder(folderpath,extension_tuple)):
        item_path = os.path.join(folderpath,item)
        # if os.path.exists(item_path):
            
        if os.path.isdir(folder_path):
            item_newpath = os.path.join(folder_path,item)
            shutil.move(item_path,item_newpath)
        else:
            os.mkdir(folder_path)
            item_newpath = os.path.join(folder_path,item)
            shutil.move(item_path,item_newpath)
            
        
        
    # print("Calling File Finder")
    # print