<h1 align = "center">
  Doctor-Fee-Prediction
</h1>

<p align="center"><img src="https://user-images.githubusercontent.com/118491345/266513700-87067a09-c520-46e8-a4af-a333fec16500.gif" width="1100" ></p>
<br>

The **Doctor Fee Prediction** project revolutionizes healthcare decision-making. The data was harnessed from Practo, a leading healthcare platform, and advanced data analysis and machine learning were applied to empower patients with accurate doctor fee estimates. By considering factors like specialization and experience, our user-friendly tool enhances transparency and aids in cost-effective healthcare choices. Explore how data science transforms the healthcare landscape, from data collection to predictive modeling and deployment of an interactive web application.
<br>

## <h2 class="section-heading" id="usage"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="50" height="50"></a> User's Manual</h2>

| Files/Folder| Description |
| ------------- | ------------- |
| **[`Python File`](Python%20File)** | Review the data extraction process and preprocessing steps |
| **[`Python File/ML_Models.ipynb`](Python%20File/ML_Models.ipynb)** | Understand the machine learning model creation  |
| **[`DATA`](Data)** | Explore the raw and cleaned data  |
| **[`Webpage`](Webpage)** | Run the web page using the provided code |
| **[`Project Presentation`](Doctor%20Fee%20Prediction.pdf)** | Gain deeper insights from the presentation and findings|

<br>

## <img src="https://clipartmag.com/images/pictures-of-animated-books-20.gif" width="60" height="60"> **Table of Contents**

- [`User's Manual`](#usage)
- [`Problems Aim to Solve`](#objective)
- [`Project Overview`](#project-overview)
- [`Data Extraction`](#data-extraction)
- [`Data Preprocessing`](#data-preprocessing)
- [`Insights and Visualizations`](#insights-and-visualizations)
- [`Machine Learning Modeling`](#machine-learning-modeling)
- [`Web Application`](#web-application)
- [`Challenges and Learnings`](#challenges_and_learnings)
- [`Future Scope`](#future_scope)
- [`Conclusion`](#conclusion)

<br>

## <h2 class="section-heading" id="objective"><a href="your_link_here"><img src="https://i.pinimg.com/originals/ca/d1/3b/cad13bab63529947fa266158bebf8c05.gif" width="50" height="50"></a> Problems Aim to Solve</h2>
This project primarily aims to benefit patients in the healthcare sector. It provides a user-friendly platform for patients to estimate doctor's fees, enabling informed decision-making about medical expenses. By analyzing data on doctor specializations, experience levels, and regional fee variations, the project empowers patients to navigate the complex healthcare cost landscape. Its ultimate goal is to enhance transparency and affordability in healthcare, promoting patient-centered access to quality medical services.

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

## <h2 class="section-heading" id="data-extraction"><a href="your_link_here"><img src="https://www.formsright.ai/images/icons/gif/file-transfer.gif" width="50" height="50"></a> Data Extraction</h2>
The data extraction phase involved the use of Python libraries such as Selenium and BeautifulSoup to scrape valuable information from Practo, a healthcare website. This process enabled the collection of essential attributes including doctor specializations, years of experience, location, city, dp_score, consultation fees, and more, which formed the foundation of the analysis. [`Scraping code`](Python%20File/Scraping%20code.ipynb) directory contains thr python script for web scraping. The collected data can be found in [`Raw practo`](Data/raw_practo.csv).

## <h2 class="section-heading" id="data-preprocessing"><a href="your_link_here"><img src="https://cdn-images-1.medium.com/fit/t/1600/480/1*mf619XEdHd1O2MlyhEKcig.gif" width="50" height="50"></a> Data Preprocessing</h2>
Once the data was gathered, the data preprocessing stage played a pivotal role in preparing it for analysis and machine learning. This encompassed tasks such as handling missing values, removing duplicates, and converting data types where necessary. In the preprocessing phase, exploratory data analysis was also performed on cleaned data. The Jupyter Notebook [`Preprocessing and EDA`](Python%20File/Preprocessing_EDA.ipynb) includes the cleaning and visualization code. The cleaned data can be found in [`Clean practo`](Data/clean_practo.csv).

## <h2 class="section-heading" id="machine-learning-modeling"><a href="your_link_here"><img src="https://bugfender.com/wp-content/uploads/2018/10/automated.gif" width="50" height="50"></a> Machine Learning Modeling</h2>
`In the model-building phase the data for training were diligently prepared. This involved the following process:`
  - Encoding of categorical variables, such as doctor speciality and degree type, and applying feature scaling to ensure consistent feature scales.
  - With the data ready, splitting was done into training and testing sets.
  - Next, various machine learning models were explored to predict doctor's fees.
  - Following extensive testing and evaluation, the `RandomForestRegressor` was identified as the top-performing model, boasting the highest accuracy among all alternatives.
  - Then rigorous performance assessments were conducted using metrics like Mean Absolute Error (MAE) and Mean Squared Error (MSE).
  - Ultimately, the RandomForestRegressor became the model of choice and it was saved using the Pickle library, marking the completion of the model-building process for future deployment.
The machine learning model is built using `Scikit-learn` and can be found in the Jupyter Notebook [`ML Models`](Python%20File/ML_Models.ipynb).

<br>

## <h2 class="section-heading" id="web-application"><a href="your_link_here"><img src="https://i.pinimg.com/originals/45/a1/b5/45a1b55abd622e5a3b41992325f175bf.gif" width="50" height="50"></a> Web Application</h2>
The project includes an interactive web application developed with `Flask`. The application allows users to input values for `speciality_of_doctor`, `degree_type`, `year_of_experience`, `Location`, `city`, `dp_score`, and `npv_` to obtain a predicted consultation fee for doctors. The machine learning model, stored as [`Model`](Webpage/model.pkl), is integrated into the web application.

### Directory Structure for Web Page

- [`Application`](Webpage/app.py): Flask application handling user inputs and serving the web page.
- [`Model`](Webpage/model.pkl): Trained machine learning model for predicting consultation fees.
- [`Webpage`](Webpage/templates): Directory containing the HTML template for the interactive web application.
  - [`Webpage Templates`](Webpage/templates/index.html): HTML template allowing users to input attributes and get predicted fees.
  - [`Webpage Requirements`](Webpage/requirements.txt): Requirements of all necessary libraries.

       <img align="center" alt="Coding" lenght = "500" width="600" src="https://user-images.githubusercontent.com/118491345/266401208-eae93f76-f82f-4015-a2fb-222ff60fde77.png">


<br>

## <h2 class="section-heading" id="insights-and-visualizations"><a href="your_link_here"><img src="https://media2.giphy.com/media/IateADsrO1rDOep6PY/giphy.gif?cid=6c09b952im399xndln3k3nwi7ts0zvuvxcg95q6yb6oe87sc&ep=v1_stickers_related&rid=giphy.gif&ct=s" width="50" height="50"></a> Insights and Visualizations</h2>
<br>

 - **`Geographical Distribution`**: Approximately 50% of the doctors are located in Bangalore, highlighting the city's significance in healthcare services.
 - **`Common Degrees`**: MBBS and BDS emerge as the most prevalent degrees among the doctors in the dataset, underscoring their popularity and importance in the medical field.
 - **`Dentistry Dominance`**: Dentists, as indicated by the high count, appear to be a prominent group, reflecting the relevance of dental care in the healthcare system.
 - **`Experience Range`**: The majority of doctors fall within the 20-25 years of experience range, indicating a substantial presence of seasoned professionals.
 - **`Specialization Experience`**: Among different specializations, bariatric surgeons have the highest average years of experience, likely due to the complexity and specialized nature of their field. In contrast, chiropractors have the lowest average years of experience, possibly due to the nature of their practice, which may attract newer professionals.
   
<br>
<p align="center"><img src="https://github.com/Pragya-011/Doctor-Fee-Prediction/assets/118491345/e0a3984f-a673-4bc9-972c-4ca48acfd573" height="400" width="400"></p>
<br>
<p align="center"><img src="https://github.com/Pragya-011/Doctor-Fee-Prediction/assets/118491345/6a18ae83-cb10-4d3b-9a1f-9f7636922753" ></p>
<br>
<p align="center"><img src="https://github.com/Pragya-011/Doctor-Fee-Prediction/assets/118491345/0905ba6e-b8cf-4647-a41a-44fa194ad091" ></p>


<br>

## <h2 class="section-heading" id="challenges_and_learnings"><a href="your_link_here"><img src="https://media0.giphy.com/media/cExWgK1q0qha5oiuBb/giphy.gif?cid=6c09b952x5xjy8fxzog2yw0xljinbs7aw4jjwlay1r66t5w7&rid=giphy.gif&ct=s" width="50" height="50"></a> Challenges and Learnings</h2>
 - Effective Data Scraping: Mastering the art of efficient web data collection using Selenium and BeautifulSoup.
 - Feature Engineering Proficiency: Developing expertise in selecting and transforming relevant features for machine learning models.
 - Model Evaluation Skills: Gaining a deeper understanding of model evaluation metrics and techniques, particularly in the context of regression tasks.
 - Web Scraping Complexity: Facing challenges when dealing with the dynamic nature of Practo's website during data scraping, including potential structural changes.
 - Data Cleaning Effort: Overcoming obstacles related to data cleaning, especially when handling missing data and format inconsistencies.
 - Feature Selection Dilemma: Navigating the complexity of feature selection and experimenting to determine essential features for accurate fee prediction.
 


## <h2 class="section-heading" id="future_scope"><a href="your_link_here"><img src="https://user-images.githubusercontent.com/74038190/214644145-264f4759-7633-441e-9d67-d8dda9d50d26.gif" width="60" height="60"></a> Future Scope</h2>
 - Real-Time Data Updates: Incorporate real-time data sources for up-to-the-minute fee estimations.
 - Geographic Expansion: Extend coverage to more cities and regions to provide a broader service.
 - Multi-Criteria Estimation: Enhance the model to consider patient reviews, clinic ratings, and appointment availability.
 - Mobile Application: Create a user-friendly mobile app for convenient access to fee estimates.
 - Provider Integration: Collaborate with healthcare providers to embed the tool into their platforms.
 - Patient Feedback System: Implement a feedback mechanism to refine the model's accuracy and improve user experience over time.


## <h2 class="section-heading" id="conclusion"><a href="your_link_here"><img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/25b24795113117.5e8f78637283d.gif" width="50" height="50"></a> Conclusion</h2>

In summary, our project has successfully addressed key challenges in healthcare decision-making by providing patients with a user-friendly tool to estimate doctor's fees accurately. Leveraging data from Practo, information was analyzed and processed, revealing insightful trends such as the dominance of MBBS and BDS degrees, the prevalence of dentists, and the varying years of experience across specializations. The machine learning model, with the RandomForestRegressor as the top-performing choice, empowers patients to make informed choices, enhances transparency, and fosters cost-effective healthcare decisions. This project exemplifies the transformative potential of data science in healthcare, offering a practical solution that benefits both patients and healthcare providers.
