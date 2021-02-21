'''
Summary:
Collect data recorded regarding the SARS-COV-2 (COVID-19) virus. Open file, select fields for use.

Date Created: 
(YYYY-MM-DD) 2021-01-03

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

# Initializations

# initialize array for Daily data: total_cases
total_cases = np.zeros((len(USA['data']),1))

#initialize array for Daily data: new_cases
new_cases = total_cases.copy()

#initialize array for Daily data: total_deaths
total_deaths = total_cases.copy()

#initialize array for Daily data: new_deaths
new_deaths = total_cases.copy()

#initialize array for Daily data: total_tests
total_tests = total_cases.copy()

#initialize array for Daily data: new_tests
new_tests = total_cases.copy()

#initialize array for Daily data: hosp_patients
hosp_patients = total_cases.copy()

#initialize array for Daily data: days_since_patient_zero
day_num = total_cases.copy()

#initialize array for Daily data: date
date = np.empty(total_cases.shape,dtype=np.dtype('U25'))


# For loop going through Daily Data: all fields
for ii,day in enumerate(USA['data']):
    if 'total_cases' in day:
        total_cases[ii] = day['total_cases']
    if 'new_cases' in day:
        new_cases[ii] = day['new_cases']
    if 'total_deaths' in day:
        total_deaths[ii] = day['total_deaths']
    if 'new_deaths' in day:
        new_deaths[ii] = day['new_deaths']
    if 'total_tests' in day:
        total_tests[ii] = day['total_tests']
    if 'new_tests' in day:
        new_tests[ii] = day['new_tests']
    if 'hosp_patients' in day:
        hosp_patients[ii] = day['hosp_patients']
    day_num[ii] = ii
    if 'date' in day:
        date[ii] = day['date']


### Data Visualizations

## Time Series
# cummulative cases vs. day: total_cases and day_num
plt.figure()
plt.plot(day_num, total_cases)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cummulative Cases')

# new cases vs. day: new_cases and day_num
plt.figure()
plt.plot(day_num, new_cases)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Cases')

#total deaths vs. day: total_deaths and day_num
plt.figure()
plt.plot(day_num, total_deaths)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cumulative Deaths')

#new deaths vs. day: new_deaths and day_num
plt.figure()
plt.plot(day_num, new_deaths)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Deaths')

# cummulative tests vs. day: total_tests and day_num
plt.figure()
plt.plot(day_num, total_tests)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cumulative tests')

# new tests vs. day: new_tests and day_num
plt.figure()
plt.plot(day_num, new_tests)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Tests')

# hospital patients vs. day: hosp_patients and day_num
plt.figure()
plt.plot(day_num, hosp_patients)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Hospitalized Patients')

## Correlation:

# new tests vs. new cases
plt.figure()
plt.scatter(new_tests, new_cases)
plt.xlabel('Daily New Tests')
plt.ylabel('Daily New Cases')
