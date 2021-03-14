'''
Summary: Collect, analyze, and visualize data regarding SARS-COV-2 

Date Created: 3/7/2021
Date Modified: 3/7/2021

Authors: Daniel Noirot, Brandon Noirot
'''

# Functions: 7 Day Moving Average
def WeekAvg(week):
    avg = sum(week)/len(week)
    return avg

def CasePositivity(cases, tests):
    return cases/tests*100


if __name__ is '__main__':
    # Packages
    import matplotlib.pyplot as plt
    import numpy as np 
    import json 
    import urllib3

    # Read JSON file

    with urllib3.PoolManager() as url:
        f = url.request('GET', 'https://covid.ourworldindata.org/data/owid-covid-data.json')
        data = json.loads(f.data.decode('utf-8'))

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
    new_vacs = total_cases.copy()
    new_vacs_avg = total_cases.copy()
    total_vacs = total_cases.copy()
    people_vacs = total_cases.copy()
    people_full_vacs = total_cases.copy()
    positivity = total_cases.copy()

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
        if 'new_vaccinations' in day:
            new_vacs[ii] = day['new_vaccinations']
        if 'total_vaccinations' in day:
            total_vacs[ii] = day['total_vaccinations']
        if 'people_vaccinated' in day:
            people_vacs[ii] = day['people_vaccinated']
        if 'people_fully_vaccinated' in day:
            people_full_vacs[ii] = day['people_fully_vaccinated']


    for ii in range(len(new_cases)):
        if new_tests[ii] != 0:
            positivity[ii] = CasePositivity(new_cases[ii], new_tests[ii])

    # Data Masking

   
    # 7-Day moving averages
    for ii in range(len(new_cases)):
        if ii > 5:
            new_cases_avg[ii] = WeekAvg(new_cases[ii-6:ii+1])
            new_deaths_avg[ii] = WeekAvg(new_deaths[ii-6:ii+1])
            new_tests_avg[ii] = WeekAvg(new_tests[ii-6:ii+1])
            new_vacs_avg[ii] = WeekAvg(new_vacs[ii-6:ii+1])

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

    plt.figure()
    plt.plot(day_num, new_vacs, label = 'Daily Count')
    plt.plot(day_num, new_vacs_avg, label = '7-Day Moving Avg')
    plt.xlabel('Days Since Patient Zero')
    plt.ylabel('Daily New Vaccinations')
    plt.legend()

    plt.figure()
    plt.plot(day_num, total_vacs)
    plt.xlabel('Days Since Patient Zero')
    plt.ylabel('Cumulative Vaccinations')

    plt.figure()
    plt.plot(day_num, people_vacs, label = 'Partial & Fully')
    plt.plot(day_num,people_full_vacs, label = 'Fully')
    plt.xlabel('Days Since Patient Zero')
    plt.ylabel('People Vaccinated')
    plt.legend()

    plt.figure()
    plt.plot(day_num, positivity)
    plt.xlabel('Days Since Patient Zero')
    plt.ylabel('Testing Positivity [%]')