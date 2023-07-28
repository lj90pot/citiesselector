# European Cities Recommender

## Introduction

Welcome to the European Cities Recommender! This repository contains the source code and materials for an Streamlit app that recommends you the best city in Europe to live. Always regarding your inputs in certain variables. This is the final Project for Ironhack Data Analytics bootcamp. The files and the folders are organize in a way that all derivables are easy to access.

## Folders

The repository is organized into the following folders:

- **Data**: [Mainly data outputs]
- **PPT**: [Powerpoint presentation]
- **Python**: [Python codes]
- **Streamlit**: [Streamlit application code]
- **Tableau**: [Tableau dashboard]

## Data

The source data from Eurostat is not included in the repository
The raw data contained no headers. These were added later. A dictionary was created for this purpose. 
The data for each city was splitted in years. Fur the purpose of this exercise the most updated data for each city was selected to build the model. 
The final dataset contains one row per city and the nulls are filled with the value for that variable in the country where the city is located. 

## Code Explanation

In this section, you will find an overview of the main code files in the repository and their functionalities:

- **`01_import_data.ipynb`**: [This file is used to import the raw data and create a dictionary and a csv with all the raw data]
- **`02_data_cleaning bueno.ipynb`**: [This file cleans the data, handle the nulls and select the features to use]
- **`03_EDA.ipynb`**: [This file explore the variables chosen, check for outliers and distributions]
- **`04_KMeans.ipynb`**: [This file is used to compare models and select the best one to use. ]

## Tableau dashboard

A tableau dashboard is provided to help the exploration of the data and the distribution of the cities. 
A dashboard shows the final clusterig of the cities and the variables values in each city. 

## Streamlit Explanation

The repository includes a Streamlit application. The following files are related to the Streamlit app:

- **`main.py`**: [This is the Streamlit app. Run this file from the terminal. The browser will open a tab with the application]

## Trello Organization

- [https://trello.com/b/oVlUVj2n/european-cities-recommender] Trello organizer

## Acknowledgments

* [Xisca](https://www.linkedin.com/in/xisca-sorell-llull-39128949/)
* [Sabina](https://www.linkedin.com/in/sabina-firtala/)
* [Laz](https://www.linkedin.com/in/lazarus-kon-27549880/)
* [Camille](https://www.linkedin.com/in/camillecoeurjoly/)
* All my colleagues


