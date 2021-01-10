'''
Summary:
Collect data recorded regarding the SARS-COV-2 (COVID-19) virus. Open file, select fields for use.

Date Created: 
(YYYY-MM-DD) 2021-1-3

Authors: 
Daniel Noirot, Brandon Noirot

Inputs:


Outputs:

'''
# import packages
import matplotlib.pyplot as plt
import numpy as np

# Python program to read json file 
import json 
  
# Opening JSON file 
f = open('owid-covid-data.json','r') 
  
# returns JSON object as a dictionary 
data = json.load(f) 

# Closing file 
f.close()


# Data Structure from JSON file:
### Country/Country Metadata/Days Since Patient Zero/Data

# pulling data for Country: USA
USA = data['USA']

# initialize array for Daily data: total_cases
total_cases = np.zeros((len(USA['data']),1))

# For loop going through Daily Data
for ii,day in enumerate(USA['data']):
    total_cases[ii] = day['total_cases']