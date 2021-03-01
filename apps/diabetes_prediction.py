# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:23:36
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 03:43:24

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pandas as pd
from PIL import Image

@st.cache(allow_output_mutation=True)
def load(scaler_path, model_path):
    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
    return sc , model

def inference(row, scaler, model, feat_cols):
    df = pd.DataFrame([row], columns = feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns = feat_cols)
    if (model.predict(features)==0):
        return 0,"Congratulations!!!. Based on our estimation we believe that you currently do not have diabetes. We however would like to ask you to stay safe and stay healthy."
    else: return 1,"We regret to inform you that based on our estimation we believe that you have chances of being diabetic. We request you to kindly visit a doctor."


def app():     
     st.markdown(
    """
    The following web application has been built to predict early stage Diabetes for women who are above the age of 21. Diabetes is in the list of **The Top 10 Causes of Death** as per the report by the **World Health Organization**
    """)
     st.write('Please fill in the following form click on the button below!')

     name = st.text_input('Name','Please Enter Your Name')
     phone = st.text_input('Mobile Number','Please Enter Your Mobile Number')
     email = st.text_input('Email','Please Enter Your Email')
     
     st.markdown("""### Age""")
     age = st.number_input("", 1, 150, 25, 1)
     st.markdown("""### Number of Pregnancies""")
     pregnancies = st.number_input("", 0, 20, 0, 1)
     st.markdown("""### GLUCOSE Level- (mm/dl)""")
     glucose = st.slider("", 0, 200, 25, 1)
     st.markdown("""### Skin Thickness - (mm)""")
     skinthickness = st.slider("", 0, 99, 20, 1)
     st.markdown("""### Blood Pressure - (mm Hg)""")
     bloodpressure = st.slider('', 0, 122, 69, 1)
     st.markdown("""### Insulin - (mu U/ml)""")
     insulin =       st.slider("", 0, 846, 79, 1)
     st.markdown("""### BMI - (weight in kg/(height in m)^2)""")
     bmi =           st.slider("", 0.0, 67.1, 31.4, 0.1)
     st.markdown("""### Diabetics Pedigree Function""")
     dpf =           st.slider("", 0.000, 2.420, 0.471, 0.001)

     row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]
     patient_data = [name,phone,email,age,pregnancies, glucose, skinthickness, bloodpressure,insulin, bmi, dpf]
     if (st.button('Check Health Status')):
         feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
         sc, model = load('models/scaler.joblib', 'models/model.joblib')
         pred,result = inference(row, sc, model, feat_cols)
         if pred == 0 :
            st.success(result)
            st.balloons()

         else :
            st.warning(result)
         patient_data.append(pred)
         patient_df = pd.read_csv('./patient_data.csv')
         patient_df.loc[len(patient_df)] = list(patient_data)
         patient_df.to_csv('./patient_data.csv',index=False)
