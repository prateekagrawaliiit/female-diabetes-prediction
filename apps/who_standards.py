# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 22:37:41
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 22:51:29

import streamlit as st

def app():
    st.title('About')
    st.write("""    
    ## World Health Organization Standards

    ### Glucose

    The expected values for normal fasting blood glucose concentration are between **70 mg/dL** and **100 mg/dL**. When fasting blood glucose is between **100** to **125 mg/dL**, changes in lifestyle and monitoring glycemia are recommended. 

    ### Blood Pressure

    A Blood Pressure below **140/90 mm Hg** should be recommended for all diabetic individuals, and around **135/85 mm Hg** for most people on average.
    
    """)
