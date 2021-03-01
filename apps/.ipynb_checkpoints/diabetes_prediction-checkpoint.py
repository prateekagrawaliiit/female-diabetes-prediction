# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:23:36
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 02:23:43

import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('About')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")
    
    st.write(df)