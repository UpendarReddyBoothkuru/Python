import os
import time
#from datetime import datetime
# datetime object containing current date and time
time_str = time.strftime("%Y%m%d_%H%M%S")
current_time = time.time()
filename='C:/Users/uboothkuru/Documents/test/logfile_' + time_str + '.log'
f = open(filename, 'w')
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
        if age_of_file_in_minutes > 60:
            print(f"age of the file {file_path} is: {age_of_file_in_minutes} minutes ")
            #time =os.path.getctime(file_path)
            #print(time)
            f.write( file_path + '\n')
            ##os.remove(file_path)
f.close()