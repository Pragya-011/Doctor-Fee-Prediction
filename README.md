<h1 align = "center">
  Doctor-Fee-Prediction
</h1>

<p align="center"><img src="https://cutewallpaper.org/24/medical-gif/medical-animation-by-gurmeet-singh-on-dribbble.gif" width="1000" ></p>
<br>

##  <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/25b24795113117.5e8f78637283d.gif" width="45" height="45"> **Overview**

The **Doctor's Fee Prediction** project focuses on predicting consultation fees for doctors based on attributes such as specialty, experience, location, and more. The project involves data extraction, preprocessing, model building, and an interactive web application.

<br>

##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="45" height="45"> **User's Manual**

| Files/Folder| Description |
| ------------- | ------------- |
| **`Python Files`** | Review the data extraction process and preprocessing steps |
| **`Python Files/ML_Models.ipynb`** | Understand the machine learning model creation  |
| **`DATA`** | Explore the raw and cleaned data  |
| **`Web Application`** | Run the web application using the provided code |

<br>

## <img src="https://clipartmag.com/images/pictures-of-animated-books-20.gif" width="48" height="48"> **Table of Contents**

- [Project Details](#project-details)
- [Data Extraction](#data-extraction)
- [Data Preprocessing](#data-preprocessing)
- [Machine Learning Modeling](#machine-learning-modeling)
- [Web Application](#web-application)
- [Presentation](#presentation)
- [Acknowledgments](#acknowledgments)

<br>

## <h2 class="section-heading" id="project-details"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/74038190/216121952-63f41409-6eb1-4a81-8b47-0d5d7c8552a4.png" width="50" height="50"></a> Project Details</h2>

This project utilizes Python libraries such as NumPy and Pandas for data cleaning and preprocessing purposes. Matplotlib and Seaborn are used for data analysis and visualization. Scikit-learn (sklearn) is employed for building the machine learning model. Flask, HTML, and CSS are used to build an interactive website.

The main objective is to predict doctor consultation fees based on the following attributes:

<img align="right" alt="Coding" width="220" src="https://www.suyogcare.in/assets/img/%E2%81%ADgif2.gif">

- `speciality_of_doctor`: Specialty of the doctor
- `degree_type`: Type of degree (e.g., MBBS, MD, BDS)
- `year_of_experience`: Total years of experience
- `Location`: Clinic location
- `city`: City of the clinic
- `dp_score`: Doctor-patient experience score
- `npv_`: Number of people's votes

<br>

## <a href="#python-files"><img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="45" height="45"></a> **Python Files**

### Data Extraction
- The data extraction phase involves collecting raw doctor information from the online medical consultancy booking site Practo. This is achieved using the Jupyter Notebook `Scrapping code.ipynb`.

### Data Preprocessing
- In the preprocessing phase data is cleaned, missing values are handled, and exploratory data analysis is performed. The Jupyter Notebook `Preprocessing_EDA.ipynb` includes the cleaning and visualization code.

### Machine Learning Modeling
- The machine learning model is built using Scikit-learn and is implemented in the Jupyter Notebook `ML_Models.ipynb`. This model predicts the consultation fee for doctors based on the provided attributes.

<br>

## <a href="#Data"><img src="https://ps.w.org/post-to-csv/assets/icon-256x256.gif?rev=2620179" width="50" height="50"></a> **Data**

### Raw Data
- The collected data is stored in `raw_practo.csv`.

### Cleaned Data
- The cleaned data is saved in `clean_practo.csv`.

<br>

## <h2 class="section-heading" id="web-application"><a href="your_link_here"><img src="https://media2.giphy.com/media/IateADsrO1rDOep6PY/giphy.gif?cid=6c09b952im399xndln3k3nwi7ts0zvuvxcg95q6yb6oe87sc&ep=v1_stickers_related&rid=giphy.gif&ct=s" width="50" height="50"></a> Web Application</h2>

The project includes an interactive web application developed with Flask. The application allows users to input values for `speciality_of_doctor`, `degree_type`, `year_of_experience`, `Location`, `city`, `dp_score`, and `npv_` to obtain a predicted consultation fee for doctors. The machine learning model, stored as `model.pkl`, is integrated into the web application.

### Directory Structure for Web Application

- `app.py`: Flask application handling user inputs and serving the web page.
- `model.pkl`: Trained machine learning model for predicting consultation fees.
- `templates/`: Directory containing the HTML template for the interactive web application.
  - `index.html`: HTML template allowing users to input attributes and get predicted fees.

       <img align="center" alt="Coding" lenght = "500" width="600" src="https://user-images.githubusercontent.com/118491345/266401208-eae93f76-f82f-4015-a2fb-222ff60fde77.png">


<br>

## <h2 class="section-heading" id="presentation"><a href="your_link_here"><img src="https://media.tenor.com/Tw7ociOZPzkAAAAM/spreadsheet-animated.gif" width="55" height="55"></a> Presentation</h2>

- `Doctor Fee Prediction.pdf`: Presentation showcasing project details and insights.

- `README.md`: Overview of the project, its structure, and usage instructions.

<br>

## <h2 class="section-heading" id="acknowledgments"><a href="your_link_here"><img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/3364a095113117.5e8f786372e94.gif" width="50" height="50"></a> Acknowledgments</h2>

We extend our appreciation to the mentors and faculty members for their guidance and support throughout the project.
