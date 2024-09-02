import os
import time
current_time = time.time()
for path, subdirs, files in os.walk("C:/Users/uboothkuru/Documents/test/"):
    #print(path)
    #print(subdirs)
    #print(files)
    for name in files:
        file_path =os.path.join(path, name)
        #print(file_path)
        #print(os.path.getmtime(file_path))
        age_of_file_in_minutes = (current_time - os.path.getmtime(file_path))/60
        #print(f"age of the file {file_path} is: {age_of_file_in_minutes} ")
        if age_of_file_in_minutes > 100:
            print(f"age of the file {file_path} is: {age_of_file_in_minutes} ")
