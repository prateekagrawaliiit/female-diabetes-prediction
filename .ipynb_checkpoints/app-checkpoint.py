# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 00:46:59
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 01:15:44

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

name = st.text_input("Name:")
pregnancy = st.number_input("No. of times pregnant:")
glucose = st.number_input("Plasma Glucose Concentration :")
bp =  st.number_input("Diastolic blood pressure (mm Hg):")
skin = st.number_input("Triceps skin fold thickness (mm):")
insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
dpf = st.number_input("Diabetes Pedigree Function:")
age = st.number_input("Age:")
submit = st.button('Predict')

temp = pd.DataFrame([pregnancy, glucose, bp, skin, insulin, bmi, dpf, age])
temp
if submit:
        st.title(temp)
        prediction = classifier.predict(temp)
        if prediction == 0:
            st.write('Congratulation',name,'You are not diabetic')
        else:
            st.write(name," we are really sorry to say but it seems like you are Diabetic.")