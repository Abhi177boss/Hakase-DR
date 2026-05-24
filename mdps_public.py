# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Multiple Disease Prediction System",
    layout="wide",
    page_icon="🩺"
)


# =========================
# Loading Saved Models
# =========================

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# =========================
# Sidebar Navigation
# =========================

with st.sidebar:

    selected = option_menu(
        'Hakase DR',

        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Prediction'],

        icons=['activity', 'heart', 'person'],
        default_index=0
    )


# =========================================================
# Diabetes Prediction Page
# =========================================================

if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction ')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input(
            'Number of Pregnancies',
            min_value=0.0
        )

    with col2:
        Glucose = st.number_input(
            'Glucose Level',
            min_value=0.0
        )

    with col3:
        BloodPressure = st.number_input(
            'Blood Pressure value',
            min_value=0.0
        )

    with col1:
        SkinThickness = st.number_input(
            'Skin Thickness value',
            min_value=0.0
        )

    with col2:
        Insulin = st.number_input(
            'Insulin Level',
            min_value=0.0
        )

    with col3:
        BMI = st.number_input(
            'BMI value',
            min_value=0.0
        )

    with col1:
        DiabetesPedigreeFunction = st.number_input(
            'Diabetes Pedigree Function value',
            min_value=0.0
        )

    with col2:
        Age = st.number_input(
            'Age of the Person',
            min_value=0.0
        )

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):

        diab_prediction = diabetes_model.predict([[
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)


# =========================================================
# Heart Disease Prediction Page
# =========================================================

if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction ')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0.0)

    with col2:
        sex = st.number_input('Sex', min_value=0.0)

    with col3:
        cp = st.number_input('Chest Pain types', min_value=0.0)

    with col1:
        trestbps = st.number_input(
            'Resting Blood Pressure',
            min_value=0.0
        )

    with col2:
        chol = st.number_input(
            'Serum Cholestoral in mg/dl',
            min_value=0.0
        )

    with col3:
        fbs = st.number_input(
            'Fasting Blood Sugar > 120 mg/dl',
            min_value=0.0
        )

    with col1:
        restecg = st.number_input(
            'Resting Electrocardiographic results',
            min_value=0.0
        )

    with col2:
        thalach = st.number_input(
            'Maximum Heart Rate achieved',
            min_value=0.0
        )

    with col3:
        exang = st.number_input(
            'Exercise Induced Angina',
            min_value=0.0
        )

    with col1:
        oldpeak = st.number_input(
            'ST depression induced by exercise',
            min_value=0.0
        )

    with col2:
        slope = st.number_input(
            'Slope of the peak exercise ST segment',
            min_value=0.0
        )

    with col3:
        ca = st.number_input(
            'Major vessels colored by flourosopy',
            min_value=0.0
        )

    with col1:
        thal = st.number_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',
            min_value=0.0
        )

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):

        heart_prediction = heart_disease_model.predict([[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)


# =========================================================
# Parkinson's Prediction Page
# =========================================================

if selected == "Parkinsons Prediction":

    st.title("Parkinson's Disease Prediction ")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)

    with col4:
        Jitter_percent = st.number_input(
            'MDVP:Jitter(%)',
            min_value=0.0
        )

    with col5:
        Jitter_Abs = st.number_input(
            'MDVP:Jitter(Abs)',
            min_value=0.0
        )

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0)

    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0)

    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0)

    with col4:
        Shimmer = st.number_input(
            'MDVP:Shimmer',
            min_value=0.0
        )

    with col5:
        Shimmer_dB = st.number_input(
            'MDVP:Shimmer(dB)',
            min_value=0.0
        )

    with col1:
        APQ3 = st.number_input(
            'Shimmer:APQ3',
            min_value=0.0
        )

    with col2:
        APQ5 = st.number_input(
            'Shimmer:APQ5',
            min_value=0.0
        )

    with col3:
        APQ = st.number_input(
            'MDVP:APQ',
            min_value=0.0
        )

    with col4:
        DDA = st.number_input(
            'Shimmer:DDA',
            min_value=0.0
        )

    with col5:
        NHR = st.number_input(
            'NHR',
            min_value=0.0
        )

    with col1:
        HNR = st.number_input(
            'HNR',
            min_value=0.0
        )

    with col2:
        RPDE = st.number_input(
            'RPDE',
            min_value=0.0
        )

    with col3:
        DFA = st.number_input(
            'DFA',
            min_value=0.0
        )

    with col4:
        spread1 = st.number_input(
            'spread1',
            min_value=0.0
        )

    with col5:
        spread2 = st.number_input(
            'spread2',
            min_value=0.0
        )

    with col1:
        D2 = st.number_input(
            'D2',
            min_value=0.0
        )

    with col2:
        PPE = st.number_input(
            'PPE',
            min_value=0.0
        )

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):

        parkinsons_prediction = parkinsons_model.predict([[
            fo,
            fhi,
            flo,
            Jitter_percent,
            Jitter_Abs,
            RAP,
            PPQ,
            DDP,
            Shimmer,
            Shimmer_dB,
            APQ3,
            APQ5,
            APQ,
            DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE
        ]])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
