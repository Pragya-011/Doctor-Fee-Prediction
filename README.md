# Doctor-Fee-Prediction

Predicting consultation fees of doctors based on various attributes using machine learning and an interactive web application.

## Overview

The **Doctor's Fee Prediction** project focuses on predicting consultation fees for doctors based on attributes such as specialty, experience, location, and more. The project involves data extraction, preprocessing, model building, and an interactive web application.

## Table of Contents

- [Project Details](#project-details)
- [Data Extraction](#data-extraction)
- [Data Preprocessing](#data-preprocessing)
- [Machine Learning Modeling](#machine-learning-modeling)
- [Web Application](#web-application)
- [Presentation](#presentation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Project Details

This project utilizes Python libraries such as NumPy and Pandas for data cleaning and preprocessing purposes. Matplotlib and Seaborn are used for data analysis and visualization. Scikit-learn (sklearn) is employed for building the machine learning model. Flask, HTML, and CSS are used to built an interactive website.

The main objective is to predict doctor consultation fees based on the following attributes:

- `speciality_of_doctor`: Specialty of the doctor
- `degree_type`: Type of degree (e.g., MBBS, MD, BDS)
- `year_of_experience`: Total years of experience
- `Location`: Clinic location
- `city`: City of the clinic
- `dp_score`: Doctor patient experience score
- `npv_`: Number of people's votes

## Data Extraction

The data extraction phase involves collecting raw doctor information from online medical consultancy booking site Practo. 
`Data_Extraction` directory contains the extraction script and extracted CSV files. This is achieved using a Jupyter Notebook named `Scrapping.ipynb`. The collected data is stored in `raw_practo.csv`.

## Data Preprocessing

In the preprocessing phase data is cleaned, missing values are handled, and exploratory data analysis is performed. `Data_Preprocessing` directory includes the cleaning and visualization code and clean file. The cleaning and performing exploratory data analysis is carried out in a Jupyter Notebook named `Cleaning and EDA.ipynb`.  The cleaned data is saved in `clean_practo.csv`.

## Machine Learning Modeling

The machine learning model is built using Scikit-learn and is implemented in the `ML_Models.ipynb` Jupyter Notebook. This model predicts the consultation fee for doctors based on the provided attributes.

## Web Application

The project includes an interactive web application developed with Flask. The application allows users to input values for `speciality_of_doctor`, `degree_type`, `year_of_experience`, `Location`, `city`, `dp_score`, and `npv_` to obtain a predicted consultation fee for doctors. The machine learning model, stored as `model.pkl`, is integrated into the web application.

The `Web Application` directory houses the following files and subfolders for the interactive website:
- `app.py`: Flask application handling user inputs and serving the web page.
- `model.pkl`: Trained machine learning model for predicting consultation fees.
- `templates/`: Directory containing the HTML template for the interactive web application.
  - `index.html`: HTML template allowing users to input attributes and get predicted fees.

## Presentation

`Dr_Fee_Prediction_Presentation.pdf`: Presentation showcasing project details and insights.

`README.md`: Overview of the project, its structure, and usage instructions.

## Usage

1. Explore the data extraction process and raw data in the `Data Extraction` directory.
2. Review data preprocessing steps and cleaned data in the `Data Preprocessing` directory.
3. Understand the machine learning model creation in the `ML_Models` directory.
4. Run the web application using the code provided in the `Web Application` directory (`app.py`).
5. Input the required attributes on the web page to receive a predicted consultation fee.

## Acknowledgments

We extend our appreciation to the mentors and faculty members for their guidance and support throughout the project.
