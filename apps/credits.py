# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 22:37:41
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 23:25:34

import streamlit as st

def app():
    st.title(' Credits')

    st.write("""The following web application is built and maintained by **Prateek Agrawal** for the sole purpose of learning and displaying the power and usage of machine learning in the field of healthcare. He believes that the Artificial Intelligence and Machine Learning can truly help make the world a better place to live in.""")

    st.write("""

    ## Data

    The datasets consist of several medical predictor (independent) variables and one target (dependent)
    variable, Outcome. Independent variables include the number of pregnancies the patient has had,
    their BMI, insulin level, age, and so on. 
    [link of data in kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)""")
    st.write("""

    ## Columns

    |Columns|Description|
    |-------|------------|
    |Pregnancies|Number of times pregnant|
    |Glucose|Plasma glucose concentration for 2 hours in an oral glucose tolerance test|
    |BloodPressure|Diastolic blood pressure (mm Hg)|
    |SkinThickness|Triceps skin fold thickness (mm)|
    |Insulin|2-Hour serum insulin (mu U/ml)|
    |BMI|Body mass index (weight in kg/(height in m)^2)|
    |DiabetesPedigreeFunction|Diabetes pedigree function|
    |Age|Age (years)|
    |Outcome|Class variable (0 or 1) 268 of 768 are 1, the others are 0|


    ## Information

    ### WHO Website 
    * https://www.who.int/health-topics/diabetes#tab=tab_1
    * https://www.who.int/news-room/fact-sheets/detail/diabetes

    ### Machine Learning related info

    * https://www.kaggle.com/uciml/pima-indians-diabetes-database/code
    * https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2

 
    """)