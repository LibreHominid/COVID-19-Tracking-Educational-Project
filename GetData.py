'''
Summary:
Basic script to collect, analyze and portray COVID-19 data in the USA.

Date Created: 2021-01-03
Date Updated: 2021-03-04

Authors: 
~ Daniel Noirot
~ Brandon Noirot
'''
# Packages
import matplotlib.pyplot as plt
import numpy as np 
import json 
  
# Read JSON file
f = open('owid-covid-data.json','r') 
data = json.load(f) 
f.close()

############################################################################
# NOTE - Data Structure from JSON file:
# Country / Country Metadata / Days Since Patient Zero / Data
USA = data['USA']

# Initialize arrays
total_cases = np.zeros((len(USA['data']),1))
new_cases = total_cases.copy()
new_cases_avg = total_cases.copy()
total_deaths = total_cases.copy()
new_deaths = total_cases.copy()
new_deaths_avg = total_cases.copy()
total_tests = total_cases.copy()
new_tests = total_cases.copy()
new_tests_avg = total_cases.copy()
hosp_patients = total_cases.copy()
day_num = total_cases.copy()
date = np.empty(total_cases.shape,dtype=np.dtype('U25'))

# Categorize and append data
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

# 7-Day moving averages
for ii in range(len(new_cases)):
    if ii > 5:
        new_cases_avg[ii] = sum( new_cases[ii-6:ii+1] ) / len( new_cases[ii-6:ii+1] )
        new_deaths_avg[ii] = sum( new_deaths[ii-6:ii+1] ) / len( new_deaths[ii-6:ii+1] )
        new_tests_avg[ii] = sum( new_tests[ii-6:ii+1] ) / len( new_tests[ii-6:ii+1] )

############################################################################
plt.figure()
plt.plot(day_num, total_cases)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cummulative Cases')

plt.figure()
plt.plot(day_num, new_cases, label = 'Daily Count')
plt.plot(day_num, new_cases_avg, label = '7-Day Moving Avg')
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Cases')
plt.legend()

plt.figure()
plt.plot(day_num, total_deaths)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cumulative Deaths')

plt.figure()
plt.plot(day_num, new_deaths, label = 'Daily Count')
plt.plot(day_num, new_deaths_avg, label = '7-Day Moving Avg')
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Deaths')
plt.legend()

plt.figure()
plt.plot(day_num, total_tests)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Cumulative tests')

plt.figure()
plt.plot(day_num, new_tests, label = 'Daily Count')
plt.plot(day_num, new_tests_avg, label = '7-Day Moving Avg')
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Daily New Tests')
plt.legend()

plt.figure()
plt.plot(day_num, hosp_patients)
plt.xlabel('Days Since Patient Zero')
plt.ylabel('Hospitalized Patients')

plt.figure()
plt.scatter(new_tests, new_cases)
plt.xlabel('Daily New Tests')
plt.ylabel('Daily New Cases')
