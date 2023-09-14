<h1 align = "center">
  Doctor-Fee-Prediction
</h1>

<p align="center"><img src="https://user-images.githubusercontent.com/118491345/266513700-87067a09-c520-46e8-a4af-a333fec16500.gif" width="1100" ></p>
<br>

The **Doctor Fee Prediction** project focuses on predicting consultation fees for doctors based on attributes such as specialty, experience, location, and more. The project involves data extraction, preprocessing, model building, and an interactive web application.

<br>

## <h2 class="section-heading" id="usage"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="50" height="50"></a> User's Manual</h2>

| Files/Folder| Description |
| ------------- | ------------- |
| **[`Python File`](#Python%20File)** | Review the data extraction process and preprocessing steps |
| **[`Python File/ML_Models.ipynb`](#Python%20File/ML_Models.ipynb)** | Understand the machine learning model creation  |
| **[`DATA`](#Data)** | Explore the raw and cleaned data  |
| **[`Webpage`](#Webpage)** | Run the web page using the provided code |

<br>

## <img src="https://clipartmag.com/images/pictures-of-animated-books-20.gif" width="48" height="48"> **Table of Contents**

- [`User's Manual`](#usage)
- [`Project Overview`](#project-overview)
- [`Problems Aim to Solve`](#objective)
- [`Data Extraction`](#data-extraction)
- [`Data Preprocessing`](#data-preprocessing)
- [`Insights and Visualizations`](#insights-and-visualizations)
- [`Machine Learning Modeling`](#machine-learning-modeling)
- [`Web Application`](#web-application)
- [`Challenges and Learnings`](#challenges_and_learnings)
- [`Future Scope`](#future_scope)
- [`Conclusion`](#conclusion)

<br>

## <h2 class="section-heading" id="project-overview"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/74038190/216121952-63f41409-6eb1-4a81-8b47-0d5d7c8552a4.png" width="50" height="50"></a> Project Overview</h2>
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

## <h2 class="section-heading" id="objective"><a href="your_link_here"><img src="https://i.pinimg.com/originals/ca/d1/3b/cad13bab63529947fa266158bebf8c05.gif" width="50" height="50"></a> Problems Aim to Solve</h2>
This project primarily aims to benefit patients in the healthcare sector. It provides a user-friendly platform for patients to estimate doctor's fees, enabling informed decision-making about medical expenses. By analyzing data on doctor specializations, experience levels, and regional fee variations, the project empowers patients to navigate the complex healthcare cost landscape. Its ultimate goal is to enhance transparency and affordability in healthcare, promoting patient-centered access to quality medical services.


<br>

## <a href="#python-files"><img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="45" height="45"></a> **Python Files**

### Data Extraction
- The data extraction phase involved the use of Python libraries such as Selenium and BeautifulSoup to scrape valuable information from Practo, a healthcare website. This process enabled the collection of essential attributes including doctor specializations, years of experience, location, city, dp_score, consultation fees, and more, which formed the foundation of your analysis. This is achieved using the Jupyter Notebook [`Scrapping code`](#Python%20File/Scrapping%20code.ipynb`). The collected data is stored in `raw_practo.csv`.

### Data Preprocessing
- Once the data was gathered, the data preprocessing stage played a pivotal role in preparing it for analysis and machine learning. This encompassed tasks such as handling missing values, removing duplicates, and converting data types where necessary. In the preprocessing phase exploratory data analysis were also performed on cleaned data. The Jupyter Notebook [`Preprocessing EDA`](#Python%20File/Preprocessing_EDA.ipynb) includes the cleaning and visualization code. The cleaned data is saved in `clean_practo.csv`.

### Machine Learning Modeling
- In the model building phase of our project, we diligently prepared the data for training. This involved encoding categorical variables, such as doctor speciality and degree type, and applying feature scaling to ensure consistent feature scales. With the data ready, we split it into training and testing sets. Next, we delved into exploring various machine learning models to predict doctor's fees. Following extensive testing and evaluation, we identified the RandomForestRegressor as the top-performing model, boasting the highest accuracy among all alternatives. We conducted rigorous performance assessments using metrics like Mean Absolute Error (MAE) and Mean Squared Error (MSE). Ultimately, we chose the RandomForestRegressor as our model of choice and saved it using the Pickle library, marking the completion of our model-building process for future deployment.
The machine learning model is built using Scikit-learn and is implemented in the Jupyter Notebook [`ML Models`](#Python%20File/ML_Models.ipynb).

<br>

## <h2 class="section-heading" id="web-application"><a href="your_link_here"><img src="https://i.pinimg.com/originals/45/a1/b5/45a1b55abd622e5a3b41992325f175bf.gif" width="50" height="50"></a> Web Application</h2>
The project includes an interactive web application developed with Flask. The application allows users to input values for `speciality_of_doctor`, `degree_type`, `year_of_experience`, `Location`, `city`, `dp_score`, and `npv_` to obtain a predicted consultation fee for doctors. The machine learning model, stored as `model.pkl`, is integrated into the web application.

### Directory Structure for Web Application

- `app.py`: Flask application handling user inputs and serving the web page.
- `model.pkl`: Trained machine learning model for predicting consultation fees.
- `templates/`: Directory containing the HTML template for the interactive web application.
  - `index.html`: HTML template allowing users to input attributes and get predicted fees.

       <img align="center" alt="Coding" lenght = "500" width="600" src="https://user-images.githubusercontent.com/118491345/266401208-eae93f76-f82f-4015-a2fb-222ff60fde77.png">


<br>

## <h2 class="section-heading" id="insights-and-visualizations"><a href="your_link_here"><img src="https://media2.giphy.com/media/IateADsrO1rDOep6PY/giphy.gif?cid=6c09b952im399xndln3k3nwi7ts0zvuvxcg95q6yb6oe87sc&ep=v1_stickers_related&rid=giphy.gif&ct=s" width="50" height="50"></a> Insights and Visualizations</h2>
 - `Doctor Fee Prediction.pdf`: Presentation showcasing project details and insights.



<br>

## <h2 class="section-heading" id="challenges_and_learnings"><a href="your_link_here"><img src="https://media0.giphy.com/media/cExWgK1q0qha5oiuBb/giphy.gif?cid=6c09b952x5xjy8fxzog2yw0xljinbs7aw4jjwlay1r66t5w7&rid=giphy.gif&ct=s" width="50" height="50"></a> Challenges and Learnings</h2>
 


## <h2 class="section-heading" id="future_scope"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/74038190/214644145-264f4759-7633-441e-9d67-d8dda9d50d26.gif" width="60" height="60"></a> Future Scope</h2>



## <h2 class="section-heading" id="conclusion"><a href="your_link_here"><img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/25b24795113117.5e8f78637283d.gif" width="50" height="50"></a> Conclusion</h2>
