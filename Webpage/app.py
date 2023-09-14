# Importing important libraries
from flask import Flask,request,render_template
import numpy as np
import pickle  
import pandas as pd
import os

# Load a machine learning model named "model.pkl" from the "Webpage" directory using pickle
model = pickle.load(open("Webpage/model.pkl",'rb'))

# create a list of distinct location names for selection in the web page
distinct_location = ['Koramangala 7 Block', 'Bandra West', 'Kandivali West',
                        'Koramangala 3 Block', 'Koramangala 5 Block', 'Basaveshwaranagar',
                        'Vasant Kunj', 'Malleswaram', 'Malviya Nagar', 'Dwarka',
                        'Pitampura', 'HSR Layout', 'Jayanagar 4 Block', 'Sarjapur Road',
                        'Electronics City', 'Basavanagudi', 'Banaswadi',
                        'JP Nagar 6 Phase', 'Mahadevapura', 'Seegehalli', 'Whitefield',
                        'Sadashivanagar', 'Rajajinagar', 'Indiranagar', 'JP Nagar',
                        'Horamavu', 'Jayanagar 7 Block', 'Kasturi nagar', 'Domlur',
                        'Koramangala', 'West Of Chord Road', 'Varthur', 'Murugeshpalya',
                        'Singasandra', 'Yelahanka', 'HAL 2nd Stage', 'Hegde Nagar',
                        'Bannerghatta Road', 'Bellandur', 'Chandra Layout',
                        'Vidyaranyapura', 'BTM Layout 2nd Stage', 'Hennur',
                        'JP Nagar 5 Phase', 'Richmond Town', 'CV Raman Nagar',
                        'Banashankari 1st Stage', 'JP Nagar 2 Phase', 'Jalahalli',
                        'KR Puram', 'Ulsoor', 'Sahakaranagar', 'RT Nagar', 'Vijayanagar',
                        'Kundalahalli', 'Banashankari 3rd Stage', 'Jayanagar',
                        'Kaggadasapura', 'Wilson Garden', 'HRBR Layout', 'Yeshwanthpur',
                        'Munnekollal', 'Hebbal', 'Jeevanbhimanagar', 'Frazer Town',
                        'Ramamurthy Nagar', 'Upparahalli', 'Mathikere - BEL',
                        'Thanisandra', 'Lingarajapuram', 'Marathahalli', 'Belathur',
                        'Millers Road', 'Langford Road', 'Koramangala 4 Block', 'Harlur',
                        'BTM Layout 1st Stage', 'Kalyan Nagar', 'T Dasarahalli',
                        'Chamarajpet', 'Nagarbhavi', 'Bommanahalli', 'Vasanthnagar',
                        'Koramangala 1 Block', 'Hanumanthnagar', 'Hebbal Kempapura',
                        'JP Nagar 1 Phase', 'Jayanagar 2 Block', 'Kammana Halli',
                        'Viveknagar', 'Nagarbhavi 2nd Stage', 'JP Nagar 7 Phase',
                        'Brigade Road', 'Yelachenahalli', 'Bagalur', 'Begur',
                        'RMV 2nd Stage', 'Akshaya nagar', 'Yelahanka New Town',
                        'JP Nagar 3 Phase', 'Kanakpura Road', 'Sanjay Nagar', 'Hosur Road',
                        'Greater Kailash Part 2', 'Punjabi Bagh', 'Chattarpur',
                        'Mayur Vihar Ph-III', 'Sarita Vihar', 'Pusa Road',
                        'Patel Nagar West', 'Lajpat Nagar', 'Ashok Vihar', 'CR Park',
                        'Mukherjee Nagar', 'Karol Bagh', 'Vasant Vihar', 'Vikas Puri',
                        'Patparganj', 'Kalkaji', 'Vijaynagar', 'Alaknanda', 'Jangpura',
                        'Vishnu Garden', 'Katwaria Sarai', 'Kamla Nagar', 'Tilak Nagar',
                        'Rohini Sector 18', 'Mayur Vihar Ph-II', 'Rohini', 'Saket',
                        'Paschim Vihar', 'Dwarka Sector 7', 'Kilokri', 'South Extension 2',
                        'Defence Colony', 'Rohini Sector 7', 'Hari Nagar',
                        'Dwarka Sector 12', 'New Rajendra Nagar', 'Dwarka Sector 6',
                        'Kingsway Camp', 'Panchsheel Enclave', 'Gujranwala Town',
                        'Kirti Nagar', 'Rohini Sector 16', 'Durga Puri', 'Prashant Vihar',
                        'Mayur Vihar', 'Kapashera', 'Munirka', 'Shalimar Bagh',
                        'New Friends Colony', 'Rajouri Garden', 'Madangir',
                        'Vasundhra Enclave', 'Dilshad Garden', 'Karkardooma', 'Nangloi',
                        'Meera Bagh', 'Dwarka Sector 3', 'Okhla', 'Panchsheel Park',
                        'Dashrath Puri', 'Model Town 1', 'Rohini Sector 24',
                        'Safdarjung Enclave', 'Greater Kailash Part 1', 'Rohini Sector 15',
                        'Dwarka Sector 11', 'Dwarka Sector 19', 'Greater Kailash',
                        'RK Puram', 'Jagriti Enclave', 'Krishna Nagar', 'Janakpuri',
                        'Sukhdev Vihar', 'Khanpur', 'Laxmi Nagar', 'Kalyan Vihar',
                        'Uttam Nagar', 'Pandav Nagar', 'Zakir Nagar', 'Ghatkopar East',
                        'Matunga', 'Worli', 'Chembur', 'Vileparle East', 'Borivali West',
                        'Mulund West', 'Powai', 'Borivali East', 'Vileparle West',
                        'Prabhadevi', 'Dahisar East', 'Chembur East', 'Goregaon West',
                        'Versova', 'Kandivali East', 'Andheri West', 'Marol',
                        'Cumballa Hill', 'Lower Parel', 'Santacruz West', 'Ghatkopar',
                        'Nariman Point', 'Jacob Circle', 'Jogeshwari', 'Colaba',
                        'Kemps Corner', 'Oshiwara', 'Umerkhadi', 'Bhandup West',
                        'Mulund East', 'Fort', 'Malad', 'Andheri East', 'Wadala',
                        'Mira Bhayandar', 'Mira Road', 'Lokhandwala', 'Khar West',
                        'Tardeo', 'Peddar Road', 'Malad West', 'Goregaon East',
                        'Dadar West', 'Dadar East', 'Cuffe Parade', 'Matunga East', 'Juhu',
                        'Lamington Road', 'Walkeshwar', 'Chinchpokli', 'Sakinaka',
                        'Ghatkopar West', 'Parel', 'Girgaon', 'Vidyavihar', 'Govandi',
                        'Grant Road', 'Sion', 'Charni Road', 'Dahisar West', 'Opera House',
                        'Nagpada', 'Bhandup', 'Khetwadi', 'Kanjurmarg', 'Kurla West',
                        'Mahim', 'Santacruz East', 'Padmanabhanagar', 'Vikhroli West',
                        'Old Airport Road', 'Nagawara', 'Arekere', 'Sion West',
                        'Rajarajeshwarinagar', 'Anand Niketan', 'Old Rajendra Nagar',
                        'Nandini Layout', 'New BEL Road', 'Koramangala 8 Block',
                        'Bommasandra', 'Banashankari 2nd Stage', 'Jayanagar 5 Block',
                        'Brookefield', 'Gubbalala', 'New Thippasandra', 'Dwarka Sector 23',
                        'South Extension 1', 'Dwarka Sector 9', 'East Of Kailash',
                        'IP Extension', 'Lal baug', 'Turner Road', 'JB Nagar',
                        'Jayanagar 9 Block', 'Panathur', 'Kengeri', 'Jayanagar 3 Block',
                        'Sampangiramnagar', 'Chitra Vihar', 'Mazgaon', 'Chandivali',
                        'VV Puram', 'Sheikh Sarai', 'Mahalakshmi Layout', 'Tri Nagar',
                        'Shahdara', 'Malabar Hill', 'Green Park', 'Moti Nagar',
                        'HBR Layout', 'Jakkur', 'Kadugodi', 'Ramesh Nagar', 'Chanakyapuri',
                        'Dwarka Sector 22', 'Kothanur', 'Hoodi', 'Uttarahalli',
                        'Rohini Sector 8', 'Nizamuddin East', 'Siddapura', 'Kudlu',
                        'AECS Layout', 'JP Nagar 8 Phase', 'Yelenahalli', 'Ashoknagar',
                        'Preet Vihar', 'BTM Layout', 'Malleshpalya', 'Bilekahalli',
                        'Seshadripuram', 'Model Town 2', 'Shivaji Nagar', 'DLF Newtown',
                        'Doddanekundi', 'Tagore Garden', 'Mayur Vihar Ph-I',
                        'Rohini Sector 3', 'Jogeshwari East', 'Mira-Bhayandar Road',
                        'Kailash Colony', 'Kadubeesanahalli', 'Koramangala 6 Block',
                        'Jigani', 'Kasavanahalli', 'L B Sashtrinagar', 'Shantinagar',
                        'Sunkadakatte', 'Hulimavu', 'Nagasandra', 'Gulmohar Park',
                        'Jamia Nagar', 'Dadar', 'Malad East', 'Andheri', 'Hajiali',
                        'Borivali', 'Kandivali', 'Dhobi Talao', 'Peenya',
                        'Safdarjung Development Area', 'Dasarahalli', 'Mahipalpur',
                        'Churchgate', 'Linking Road', 'Anand Vihar', 'Patel Nagar',
                        'Vikhroli', 'Dwarka Sector 14', 'Hauz Khas', 'Rajanukunte',
                        'Siri Fort Road', 'Bandra', 'Ghitorni', 'Shastri Nagar',
                        'Mehrauli', 'Connaught Place', 'Banashankari', 'Shakti Nagar',
                        'Rohini Sector 11', 'Dwarka Sector 1', 'Chirag Delhi',
                        'HAL 3rd Stage', 'Nana Chowk', 'Magrath Road', 'Matunga West',
                        'Madhu Vihar', 'Model Town 3', 'Hazrat Nizamuddin', 'Naraina',
                        'Patel Nagar East', 'Lajpat Nagar 4', 'Azadpur', 'Kurla East',
                        'Kodichikkanahalli', 'Rana Pratap Bagh', 'Subhash Nagar',
                        'MS Palya', 'Mumbai Central', 'Burari', 'Bali Nagar', 'MG Road',
                        'Konanakunte', 'Bhattarahalli', 'Ashok Vihar Phase 3',
                        'Dwarka Sector 13', 'Gunjur', 'Mahavir Enclave', 'Vishwas Nagar',
                        'Bandra East', 'Surajmal Vihar', 'Kumara Park West',
                        'Doddakammanahalli', 'Naraina Vihar', 'Vikhroli East', 'Neb Sarai',
                        'Dwarka Sector 17', 'Chembur West', 'Dwarka Sector 8', 'Jasola',
                        'Harsh Vihar', 'Kalina', 'Rohini Sector 4', 'Paschim Puri',
                        'Sion East', 'Jogeshwari West', 'Pulikeshi Nagar',
                        'Okhla Industrial Estate', 'Mahalaxmi', 'Ram Nagar',
                        'Chira Bazaar', 'Vivek Vihar', 'Rohini Sector 9', 'Jhandewalan',
                        'Marine Lines', 'BEL Layout', 'Rohini Sector 5', 'Shivalik',
                        'Kumaraswamy Layout', 'Santacruz', 'Adarsh Nagar',
                        'Ashok Vihar Phase 1', 'Hongasandra', 'Avalahalli',
                        'Sarvodaya Enclave', 'Ram Vihar', 'Rohini Sector 22', 'Kurla',
                        'Ansari Nagar', 'Bhogal', 'Tuglakabad', 'Banashankari 6th Stage',
                        'Jayanagar 8 Block', 'Nelamangala', 'Rohini Sector 6', 'Gamdevi',
                        'Goregaon', 'Vinayaka Nagar', 'JP Nagar 9 Phase', 'Nehru Place',
                        'Marine Drive', 'Nirman Vihar', 'Dahisar', 'Mulund', 'Gulabi Bagh',
                        'Uday Park', 'Yojana Vihar', 'Maharani Bagh']

# create a list of distinct_speciality for selection in the web page
distinct_speciality = ['Dietitian/Nutritionist', 'Dentist', 'Physiotherapist',
       'Chiropractor', 'Dermatologist', 'Gynecologist',
       'Infertility Specialist', 'Pediatrician', 'Orthopedist',
       'Pulmonologist', 'Cardiologist', 'Rheumatologist',
       'Gastroenterologist', 'Neurologist', 'Bariatric Surgeon',
       'Urologist', 'Neurosurgeon', 'Ophthalmologist', 'Psychiatrist']

# create a list of distinct_degrees for selection in the web page
distinct_degrees = ['BSc', 'BAMS', 'BDS', 'MDS', 'PhD', 'BHMS', 'BNYS', 'BPTh/BPT',
       'MPTh/MPT', 'MSc', 'DDVL', 'DGO', 'DNB', 'MD', 'Diploma', 'MBBS',
       'DDPHN', 'DDHN', 'DM', 'Doctorate', 'DOMS', 'DPM', 'FCPS',
       'Fellowship', 'FRCP', 'FRCS', 'Masters', 'MCh', 'MS', 'PG', 'PGD']

# create a list of distinct_cities for selection in the web page
distinct_cities = ['Bangalore','Delhi','Mumbai']

# Define a function to prepare input data
def prepare_input(Year_of_experience, dp_score, npv, Degree, Speciality, Location, city):

    # Create a mapping for distinct degrees
    degree_mapping = {}
    for i, c in enumerate(distinct_degrees):
        degree_mapping[c] = i
    
    # Create a mapping for distinct specialties
    speciality_mapping = {}
    for i, c in enumerate(distinct_speciality):
        speciality_mapping[c] = i

    # Create a mapping for distinct location
    location_mapping = {}
    for i, c in enumerate(distinct_location):
        location_mapping[c] = i
    
    # Create a mapping for distinct cities
    city_mapping = {}
    for i, c in enumerate(distinct_cities):
        city_mapping[c] = i

    # Initialize variables with default values
    degree_binary = -1
    speciality_binary = -1
    location_binary = -1
    city_binary = -1

# Check if the input values exist in their respective mappings and assign binary values
    if Degree in degree_mapping:
        degree_binary = degree_mapping[Degree]
        
    if Speciality in speciality_mapping:
        speciality_binary = speciality_mapping[Speciality]
        
    if Location in location_mapping:
        location_binary = location_mapping[Location]
        
    if city in city_mapping:
        city_binary = city_mapping[city]

# Return the input variables along with their corresponding binary values
    return Year_of_experience, dp_score, npv, degree_binary, speciality_binary, location_binary, city_binary

# Create a Flask app instance
app=Flask(__name__)
# Define a route to render the main page
@app.route('/')
def index():
    return render_template("index.html")

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
        # Retrieve user input from the HTML 
    Speciality = request.form.get('speciality_of_doctor')
    Degree = request.form.get('degree_type')
    YrEx = int(request.form.get('year_of_experience'))
    Location = request.form.get('location')
    City = request.form.get('city')
    DP = int(request.form.get('dp_score'))
    NVP = int(request.form.get('npv'))

    # Print user input (optional for debugging)
    print(Speciality, Degree, YrEx, Location, City, DP, NVP, sep="\n")

    # Prepare input features using the prepare_input function
    input_features = prepare_input(YrEx, DP, NVP, Degree, Speciality, Location, City)

    # Make a prediction using the loaded machine learning model
    prediction = model.predict([input_features])

    # Round the prediction to an integer value
    # prediction_text = f"Predicted Fee: {prediction[0]}"
    rounded_prediction = round(prediction[0])
    rounded_prediction_int = int(rounded_prediction)

    # Create the prediction text with the rounded integer value
    prediction_text = f"Predicted Fee: {rounded_prediction_int}"

    # Render the main page with the prediction result
    return render_template('index.html', prediction_text=prediction_text)

# Run the Flask app
if __name__=="__main__":
    app.run(debug=True)