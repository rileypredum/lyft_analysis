# baywheels_lyft_analysis
Analysis of the baywheels data found and scraped from here: https://s3.amazonaws.com/baywheels-data/index.html

## Goals of this project
### Exploration
Exploration of the data to see what's possible

### Data cleaning/wrangling
Creating new features and wrangling data to create new analytical possibilities (ex: interpolating the cost of a ride based on website pricing information).

### Machine learning
Predicting the revenue of a ride or stop by gender and/or age, time, etc.

### Algorithms
Determining the best place to position the bikes/stops for maximum revenue

## Setup
You will need Python 3.7 and pip, the package manager. Please run a virtual environment and install the dependencies listed below:

### Necessary packages
Please run a virtual environment and install the dependencies listed below:
1. pandas
2. bs4 (BeautifulSoup)
3. Jupyter Notebook

The other packages are intrinsic to Python 3.x and should work with the import statements in the code.

## Layout and file/folder structures
All baywheels csv's are scraped from the link at the top of this readme.

These data are scraped and compiled in the baywheels-data folder (not included for repo size issues).

To access the data:
1. Run through `scraping to get all the CSVs.ipynb` and save them to your local directory of choice.
2. From there you can run `master_df_cleaning.ipynb` if you have lots of RAM, otherwise try `dev_df_data_cleaning.ipynb`.
**Note:** make sure to update the directory variables to the appropriate path on your computer!

The `server_script.py` file is used to take any large-scale process that may need to be run on a server 
or in the cloud.

The code in here is intended to be standalone, but does not yet output the resulting file desired.
