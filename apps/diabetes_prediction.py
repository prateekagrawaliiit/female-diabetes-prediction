# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:23:36
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 23:23:40

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
        return 0
    else: return 1,


def app():     
     st.markdown(
    """
    The following web application has been built to predict early stage Diabetes for women who are above the age of 21. Diabetes is in the list of **The Top 10 Causes of Death** as per the report by the **World Health Organization**
    """)
     st.write('Please fill in the following form click on the button below!')

     name = st.text_input('Please Enter Your Name','')
     phone = st.text_input('Please Enter Your Mobile Number','')
     email = st.text_input('Please Enter Your Email','')
     
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
         pred = inference(row, sc, model, feat_cols)
         if pred == 0 :
            st.success("""# Congratulations . 
            Based on your responses, we believe that you are not at a risk of being diabetic at present. Staying safe and engaging in a healthy lifestyle are proactive measures that keep diabetes at bay! """)
            st.balloons()
         else :
            st.warning("""Based on your responses, we recommend consulting a professional, as you might be at a risk of being diabetic. Please also check out the prevention page. We have some tips that might help you become healthy and fit.""")
         patient_data.append(pred)
         patient_df = pd.read_csv('./patient_data.csv')
         patient_df.loc[len(patient_df)] = list(patient_data)
         patient_df.to_csv('./patient_data.csv',index=False)

         st.markdown(
            """
            ## Prevention

            Simple lifestyle measures have been shown to be effective in preventing or delaying the onset of type 2 diabetes. To help prevent type 2 diabetes and its complications, people should:
            * achieve and maintain a healthy body weight;
            * be physically active – doing at least 30 minutes of regular, moderate-intensity activity on most days. More activity is required for weight control;
            * eat a healthy diet, avoiding sugar and saturated fats; and
            * avoid tobacco use – smoking increases the risk of diabetes and cardiovascular disease.
            """)
