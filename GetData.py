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
# Python program to read json file 
import json 
  
# Opening JSON file 
f = open('owid-covid-data.json','r') 
  
# returns JSON object as a dictionary 
data = json.load(f) 
  
# Iterating through the json list 
for i in data['USA']: 
    print(i) 
  
# Closing file 
f.close()
