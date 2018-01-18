#Extracting data from Archive API

import os
import argparse
import requests
import os
import json
import datetime

#Function to ensure if a directory exists in the path or not;if not create one
def ensure_dir(file_path,directory_name):
    if not os.path.exists(file_path+"/"+directory_name):
        os.mkdir(file_path+"/"+directory_name)
    return file_path+"/"+directory_name

cwd = os.getcwd() #To access the path of current working directory
#print('CWD: ' ,cwd)
root_dir_path=os.path.abspath(os.path.join(cwd, os.pardir)) #To get the parent directory of cwd
#print('Root Directory Path: ', root_dir_path)
parent_directory="Data"

basepath=ensure_dir(root_dir_path,parent_directory)

#Input from user
parser = argparse.ArgumentParser()
parser.add_argument("--year", dest="year", help="Enter the year",type=str)
parser.add_argument("--month", dest="month", help="Enter the month number",type=str)
args = parser.parse_args()
year=args.year
month=args.month

#Converting month number to month name
monthinteger=int(month)
month_name = datetime.date(1900, monthinteger, 1).strftime('%B')
#print(month_name)


data=[]
h={'apikey': 'dea1f660f70f46acb72e8ba21ed38afb'}

#Requesting data 
data.append(requests.get('https://api.nytimes.com/svc/archive/v1/'+year+'/'+month+'.json',headers=h).json())

#Creating hierarchy of folder structure with year and month

path1=ensure_dir(basepath,'NYT') #To check for a folder with name 'NYT'
path2=ensure_dir(path1,'Archive_API') #To check for a folder with name 'Archive_API'
path3=ensure_dir(path2,year) #To check for a folder with year
path4=ensure_dir(path3,month_name) #To check for a folder with month name
    
with open(path4+'/'+'Archive_'+year+'_'+month_name+'.json', 'w') as outfile:
    json.dump(data, outfile)
    print("Json dumped in folder")

