# Disease_Prediction

This model is deployed on streamlit you can check by clicking on this link: https://diseaseprediction-gds6zhpfpwca9cpxjqrtpd.streamlit.app/

# Disease Detection System

This project is aimed at predicting the type of disease a person may have based on various symptoms. The system takes in a set of symptoms and outputs a predicted disease. The disease categories include conditions such as allergies, infections, chronic diseases, and other common health issues.

## Features

The system uses a set of symptoms to determine the disease. The features (symptoms) include:

- Itching
- Skin Rash
- Nodal Skin Eruptions
- Continuous Sneezing
- Shivering
- Chills
- Joint Pain
- Stomach Pain
- Acidity
- Ulcers on Tongue
- Muscle Wasting
- Vomiting
- Burning Micturition
- Spotting Urination
- Fatigue
- Weight Gain
- Anxiety
- Cold Hands and Feet
- Mood Swings
- Weight Loss
- Restlessness
- Lethargy
- Patches in Throat
- Irregular Sugar Level
- Cough
- High Fever
- Sunken Eyes
- Breathlessness
- Sweating
- Dehydration
- Indigestion
- Headache
- Yellowish Skin
- Dark Urine
- Nausea
- Loss of Appetite
- Pain Behind the Eyes
- Back Pain
- Constipation
- Abdominal Pain
- Diarrhoea
- Mild Fever
- Yellow Urine
- Yellowing of Eyes
- Acute Liver Failure
- Fluid Overload
- Swelling of Stomach
- Swelled Lymph Nodes
- Malaise
- Blurred and Distorted Vision
- Phlegm
- Throat Irritation
- Redness of Eyes
- Sinus Pressure
- Runny Nose
- Congestion
- Chest Pain
- Weakness in Limbs
- Fast Heart Rate
- Pain During Bowel Movements
- Pain in Anal Region
- Bloody Stool
- Irritation in Anus
- Neck Pain
- Dizziness
- Cramps
- Bruising
- Obesity
- Swollen Legs
- Swollen Blood Vessels
- Puffy Face and Eyes
- Enlarged Thyroid
- Brittle Nails
- Swollen Extremities
- Excessive Hunger
- Extra Marital Contacts
- Drying and Tingling Lips
- Slurred Speech
- Knee Pain
- Hip Joint Pain
- Muscle Weakness
- Stiff Neck
- Swelling Joints
- Movement Stiffness
- Spinning Movements
- Loss of Balance
- Unsteadiness
- Weakness of One Body Side
- Loss of Smell
- Bladder Discomfort
- Foul Smell of Urine
- Continuous Feel of Urine
- Passage of Gases
- Internal Itching
- Toxic Look (Typhos)
- Depression
- Irritability
- Muscle Pain
- Altered Sensorium
- Red Spots Over Body
- Belly Pain
- Abnormal Menstruation
- Dischromic Patches
- Watering from Eyes
- Increased Appetite
- Polyuria
- Family History
- Mucoid Sputum
- Rusty Sputum
- Lack of Concentration
- Visual Disturbances
- Receiving Blood Transfusion
- Receiving Unsterile Injections
- Coma
- Stomach Bleeding
- Distention of Abdomen
- History of Alcohol Consumption
- Fluid Overload
- Blood in Sputum
- Prominent Veins on Calf
- Palpitations
- Painful Walking
- Pus-Filled Pimples
- Blackheads
- Scurring
- Skin Peeling
- Silver-Like Dusting
- Small Dents in Nails
- Inflammatory Nails
- Blister
- Red Sore Around Nose
- Yellow Crust Ooze

## Output (Diseases)

Based on the symptoms provided, the system can predict the following diseases:

- Allergy
- GERD (Gastroesophageal Reflux Disease)
- Chronic Cholestasis
- Drug Reaction
- Peptic Ulcer Disease
- AIDS
- Diabetes
- Gastroenteritis
- Bronchial Asthma
- Hypertension
- Migraine
- Cervical Spondylosis
- Paralysis (Brain Hemorrhage)
- Jaundice
- Malaria
- Chicken Pox
- Dengue
- Typhoid
- Hepatitis A
- Hepatitis B
- Hepatitis C
- Hepatitis D
- Hepatitis E
- Alcoholic Hepatitis
- Tuberculosis
- Common Cold
- Pneumonia
- Dimorphic Hemorrhoids (Piles)
- Heart Attack
- Varicose Veins
- Hypothyroidism
- Hyperthyroidism
- Hypoglycemia
- Osteoarthritis
- Arthritis
- (Vertigo) Paroxysmal Positional Vertigo
- Acne
- Urinary Tract Infection
- Psoriasis

## How It Works

1. **Data Collection**: The symptoms are collected from the user in a questionnaire format or through data entry.
2. **Preprocessing**: Data is processed and encoded for the model.
3. **Model Training**: A machine learning model is trained using labeled data to predict the disease based on the symptoms.
4. **Prediction**: When the user inputs their symptoms, the model predicts the most likely disease.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/disease-detection.git

2. Navigate to the project directory:
    ```bash
    cd disease-detection

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the system:
    ```bash
    python app.py
