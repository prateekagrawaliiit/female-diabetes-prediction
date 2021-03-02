# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:23:36
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 23:04:21

import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from PIL import Image
def app():
    st.title('About')
    st.write("""    
    ## What is diabetes

    According to the NIH, "Diabetes is a disease that occurs when your **blood glucose**,
     also called blood sugar, is **too high**. Blood **glucose** is your main source of
      energy and **comes from the food you eat**. **Insulin**, a hormone made from the pancreas,
       **helps glucose** from food get into your cells to be used for energy. Sometimes your 
       body doesn’t make enough or any insulin or doesn’t use insulin well. Glucose then stays 
       in your blood and doesn’t reach your cells.
    Over time, **having too much glucose in your blood** can cause health problems. """)

    st.write(
        """
        ### Health impact
Over time, diabetes can damage the heart, blood vessels, eyes, kidneys, and nerves.

* Adults with diabetes have a two- to three-fold increased risk of heart attacks and strokes(1).
* Combined with reduced blood flow, neuropathy (nerve damage) in the feet increases the chance of foot ulcers, infection and eventual need for limb amputation.
* Diabetic retinopathy is an important cause of blindness, and occurs as a result of long-term accumulated damage to the small blood vessels in the retina. Diabetes is the cause of 2.6% of global blindness(2).
* Diabetes is among the leading causes of kidney failure(3).
        """)

    st.write(
        """
        ### Key facts
* The number of people with diabetes rose from 108 million in 1980 to 422 million in 2014.
* The global prevalence of diabetes* among adults over 18 years of age rose from 4.7% in 1980 to 8.5% in 2014 (1).
* Between 2000 and 2016, there was a 5% increase in premature mortality from diabetes.
* Diabetes prevalence has been rising more rapidly in low- and middle-income countries than in high-income countries.
* Diabetes is a major cause of blindness, kidney failure, heart attacks, stroke and lower limb amputation.
* In 2016, an estimated 1.6 million deaths were directly caused by diabetes. Another 2.2 million deaths were attributable to high blood glucose in 2012.
* Almost half of all deaths attributable to high blood glucose occur before the age of 70 years. WHO estimates that diabetes was the seventh leading cause of death in 2016.
* A healthy diet, regular physical activity, maintaining a normal body weight and avoiding tobacco use are ways to prevent or delay the onset of type 2 diabetes.
* Diabetes can be treated and its consequences avoided or delayed with diet, physical activity, medication and regular screening and treatment for complications.
        """)

    
    