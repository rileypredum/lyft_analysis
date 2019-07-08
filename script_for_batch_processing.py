############################# THIS SECTION IS DATA COLLECTION FROM THE WEB ##############################
# Get all of the data from the directory and pull it into the local directory

import os
import requests
from bs4 import BeautifulSoup
import re

# Move to the data folder for this project
os.chdir('C:/Users/riley/Documents/Coding/DSC/datas/baywheels-data/')

# Get the main URL and turn it into XML soup
r = requests.get("https://s3.amazonaws.com/baywheels-data/")
data = r.text
soup = BeautifulSoup(data, "xml")

# The data file URLs are in the <Key> node so find that
keys = soup.find_all('Key')

key_list = []

# Grab the name of each file by taking the text attribute of the key node
for key in keys:
    key_list.append(key.text)
    
# Slice off the trailing file, index.html
key_list_final = key_list[:-1]


# Downloads all files in the list of filenames.
# Deal with extracting them in the next cell.

import zipfile, urllib.request, shutil

for key in key_list_final:

    url = 'https://s3.amazonaws.com/baywheels-data/' + key
    file_name = key

    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

# For all items ending in .zip in the dir_name, 
# extract their contents to dir_name and delete the original zip folder.

extension = ".zip"
dir_name = 'C:/Users/riley/Documents/Coding/DSC/datas/baywheels-data'

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file

############################### THIS SECTION IS DATAFRAME CREATION FROM THE RESULTING DIRECTORY ##############################

# Create a list of all CSVs in the directory to iterate over and make
# dataframes from.

import os

# This first section gets the master dataframe from all the csv's contained in dir_name

dir_name = 'C:/Users/riley/Documents/Coding/DSC/datas/baywheels-data/'

# List of all .csv filenames to be read into dataframes
csv_list = os.listdir(dir_name)

# Build a list of dataframe names by removing .csv
df_names = []

for csv in csv_list:
    df_name = csv.replace('.csv', '')
    df_names.append(df_name)

# Names of DFs and the filenames
df_dict_names = dict(zip(df_names, csv_list))

import pandas as pd

# Actual dictionary of dataframes
dict_of_dataframes = {}
for i in range(len(df_names)):
    dict_of_dataframes[df_names[i]] = pd.read_csv(csv_list[i])

# Concatenate the dataframes together
master_df = pd.concat(dict_of_dataframes.values()

