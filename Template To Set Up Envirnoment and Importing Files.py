#!/usr/bin/env python
# coding: utf-8

# In[164]:


# Python 3
# Yvonne Beirne FitzGerald
# Template to Setting up Envirnoment and Importing Files 

# Prep the session to use numpy, pandas, seaborn, matplot and use excel

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




from pandas import Series, DataFrame



# ############################################ Bring File In

# Set File Location
FilePath ='FILEPATH'

# Set File Name
FileName = 'FILE NAME.xlsx'

# Set File
ActiveFile = FilePath + FileName

# Read File In
OrginalExcelFile = pd.read_excel(ActiveFile)

# Getting Info On File Row and Columns
#OrginalExcelFile.shape

# Pass the first 5 rows
#OrginalExcelFile.head

# Pass the last 5 rows
#OrginalExcelFile.tail

# Get Some Statiscial Data
# OrginalExcelFile.describe()

# display file opened
# OrginalExcelFile

# ############################################# Processing


# Extracting a specific column name
InstrumentRepaired = OrginalExcelFile["COLUMN NAME"]


# Give repair class grouped by instrument repair, counts and sorts high to low
InstrumentRepairedSummary =InstrumentRepaired.value_counts()

# Gets Row CountInstrumentRepairedSummary
RepartWorkOrderCount = len(InstrumentRepaired)


# Create DataFrame will having Instrument Repair Type, Count and Percentage then add pareto principle

# Creates DataFrame
dfInstrumentRepairedSummary  = pd.concat([InstrumentRepairedSummary], axis=1)

# Rename Column Title
dfInstrumentRepairedSummary.rename(columns={'Product Model Reason: Product Model Reason Name':'RepairCount'}, inplace=True)


# Add Round Repair Percent to 1 decimal
dfInstrumentRepairedSummary = dfInstrumentRepairedSummary['RepairPercent'] = dfInstrumentRepairedSummary['RepairCount']/RepartWorkOrderCount*100






# In[ ]:




