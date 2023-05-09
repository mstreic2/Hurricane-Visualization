import numpy as np
from array import array
import os, gzip, shutil


data = array('f')

dir_name = "C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\gz"

def convert_to_raw(fileName):
    raw = ".raw"
    new_file = fileName.split('.',1)[0]
    new_file += raw
    
    with open(fileName, 'rb') as f:
        data = np.fromfile(f)
        f.close()
    
    with open(new_file, 'wb') as f:
        f.write(data)
        f.close()


def gz_extract(directory):
    extension = ".gz"
    os.chdir(directory)
    for item in os.listdir(directory): # loop through items in dir
        if item.endswith(extension): # check for ".gz" extension
            gz_name = os.path.abspath(item) # get full path of files
            file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] #get file name for file within
            with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        convert_to_raw(file_name)
        print(file_name + " unzipped and converted to .raw")

gz_extract(dir_name)

