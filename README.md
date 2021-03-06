# COVID-19 Tracking Educational Project

This repo is strictly for the educational purposes of Python training with a current and ongoing event. As COVID-19 ravages the world, especially the USA, this provides an opportunity to learn. This project will include data retrieval from multiple sources, correlating and manipulating data (non-sinister, any data scientist would understand this statement), trends and rates, data visualization and analysis.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Retrieval](#data-retrieval)
3. [Data Manipulation](#data-manipulation)
4. [Data Visualization](#data-visualization)
5. [Data Analysis](#data-analysis)
6. [Environment](#environment)

## Introduction

The **Severe Acute Respiratory Syndrome Coronavirus 2** (SARS-CoV-2), most commonly referred to as [COVID-19]([The species Severe acute respiratory syndrome-related coronavirus: classifying 2019-nCoV and naming it SARS-CoV-2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7095448/)) ("19" because the disease was first discovered in 2019), is the disease revaging the world as we know it. Many online tracking projects have been created in the wake of this historical disaster. Some are listed below:

- https://coronavirus.jhu.edu/

- https://covidtracking.com/

- [Coronavirus Pandemic (COVID-19) - Statistics and Research - Our World in Data](https://ourworldindata.org/coronavirus)
  
  

## Data Retrieval

Read data off website below instead of directly downloading files:

https://covid.ourworldindata.org/data/owid-covid-data.json

## Data Manipulation

Remove unnecessary metadata. Data we care about is:

- [x] Total cases

- [x] New cases

- [x] Total deaths

- [x] New deaths

- [x] Total tests

- [x] New tests

- [x] Hospital patients

- [x] Days since patient zero

- [x] Date

- [x] New Vaccinations

- [x] Total Vaccinations

- [x] People Vaccinated

- [x] People Fully Vaccinated

- [x] Testing Positivity

Identify outliers (if any).

## Data Visualization

Timeseries:

- [x] cummulative cases vs. day

- [x] new cases vs. day w/ 7 Day Moving Avg

- [x] cummulative deaths vs. day

- [x] new deaths vs. day w/ 7 Day Moving Avg

- [x] cummulative tests vs. day

- [x] new tests vs. day w/ 7 Day Moving Avg

- [x] hospital patients vs. day

- [x] New Vaccinations vs. day w/ 7 Day Moving Avg.

- [x] Total Vaccinations vs. day

- [x] People Vaccinated vs. day

- [x] People Fully Vaccinated vs. day

- [x] Testing Positivity vs. day

Correlation:

- [x] new tests vs. new cases



## Data Analysis

Smoothing: 
- [x] 7 Day moving average

- [x] Linear Least Squares Class

- [Gaussian Kernal Smoothing](https://en.wikipedia.org/wiki/Kernel_smoother)


Will include:

- trends

- rates of change (?)

Advanced:

- polyfit

- weibull distribution (?)

- fourier (?)



## Environment

TBD
