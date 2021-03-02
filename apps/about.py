# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:23:36
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 22:44:50

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

    
    