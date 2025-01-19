import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as f:
    load_model = pickle.load(f)

def main():
    st.title("Disease Prediction")
    
    # List of symptoms (ensure this matches the features used during model training)
    symptoms = [
        "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", "chills",
        "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting", "vomiting",
        "burning_micturition", "spotting_urination", "fatigue", "weight_gain", "anxiety",
        "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
        "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
        "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin",
        "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation",
        "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine", "yellowing_of_eyes",
        "acute_liver_failure", "fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes",
        "malaise", "blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes",
        "sinus_pressure", "runny_nose", "congestion", "chest_pain", "weakness_in_limbs",
        "fast_heart_rate", "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool",
        "irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising", "obesity", "swollen_legs",
        "swollen_blood_vessels", "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails",
        "swollen_extremeties", "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips",
        "slurred_speech", "knee_pain", "hip_joint_pain", "muscle_weakness", "stiff_neck",
        "swelling_joints", "movement_stiffness", "spinning_movements", "loss_of_balance", "unsteadiness",
        "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort", "foul_smell_of_urine",
        "continuous_feel_of_urine", "passage_of_gases", "internal_itching", "toxic_look_(typhos)",
        "depression", "irritability", "muscle_pain", "altered_sensorium", "red_spots_over_body",
        "belly_pain", "abnormal_menstruation", "dischromic_patches", "watering_from_eyes",
        "increased_appetite", "polyuria", "family_history", "mucoid_sputum", "rusty_sputum",
        "lack_of_concentration", "visual_disturbances", "receiving_blood_transfusion",
        "receiving_unsterile_injections", "coma", "stomach_bleeding", "distention_of_abdomen",
        "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum",
        "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples",
        "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
        "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
    ]
    
    # Initialize input data
    input_data = {}

    # Render radio buttons for each symptom
    for idx, symptom in enumerate(symptoms):
        input_data[symptom] = st.radio(
            symptom, [0, 1], index=0, key=f"symptom_{idx}"
        )

    # Submit button for prediction
    if st.button('Submit'):
        try:
            # Convert input data to a DataFrame and reindex to match model's features
            input_df = pd.DataFrame([input_data])
            
            # Ensure input data matches the model's training features
            model_features = load_model.feature_names_in_  # Features used in the model
            input_df = input_df.reindex(columns=model_features, fill_value=0)

            # Make predictions
            result = load_model.predict(input_df)[0]

            # Mapping diseases to their predictions
            disease_mapping = [
                "Allergy", "GERD", "Chronic cholestasis", "Drug Reaction", "Peptic ulcer disease",
                "AIDS", "Diabetes", "Gastroenteritis", "Bronchial Asthma", "Hypertension",
                "Migraine", "Cervical spondylosis", "Paralysis (brain hemorrhage)", "Jaundice",
                "Malaria", "Chicken pox", "Dengue", "Typhoid", "hepatitis A", "Hepatitis B",
                "Hepatitis C", "Hepatitis D", "Hepatitis E", "Alcoholic hepatitis", "Tuberculosis",
                "Common Cold", "Pneumonia", "Dimorphic hemorrhoids (piles)", "Heart attack",
                "Varicose veins", "Hypothyroidism", "Hyperthyroidism", "Hypoglycemia",
                "Osteoarthritis", "Arthritis", "(vertigo) Paroxysmal Positional Vertigo",
                "Acne", "Urinary tract infection", "Psoriasis"
            ]
            
            # Display the result
            st.success(f"Prediction: {disease_mapping[result]} Detected")
        
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == '__main__':
    main()
