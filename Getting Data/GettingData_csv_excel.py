#/Users/christianbeaudrie/PythonProjects/data-wrangling-video/data/

#%% IMPORT CSV FILE
#Import packages
import csv, os
import pandas as pd

#%%
#Import data using DictReader
data_path = '../data/eu_revolving_loans.csv'
print("Current Working Directory " , os.getcwd())
my_reader = csv.DictReader(open('../data/eu_revolving_loans.csv', 'rt'))

for row in my_reader:
    print(row)

# %%
df = pd.read_csv('../data/eu_revolving_loans.csv', header=[1,2,4], index_col=0)
df.head()

# %% IMPORT EXCEL FILE
#Import Packages
from openpyxl import load_workbook
wb = load_workbook(filename='../data/climate_change_download_0.xlsx')
wb.get_sheet_names()
ws = wb.get_sheet_by_name('Data')

for row in ws.rows:
    for cell in row:
        print(cell.value)

#Read into Pandas df
# !open ../data/GHE_DALY_Global_2000_2012.xls
df = pd.read_excel('../data/GHE_DALY_Global_2000_2012.xls', sheet_name = 'Global2012', header = [4,5])
df.head()
df.to_excel('../CBs_files/my_new_excel.xlsx')
# %%
