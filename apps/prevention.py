# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 22:57:35
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 23:02:29

import streamlit as st
def app():
    st.title('Prevention Diagnosis and Treatment')
    st.markdown(
            """
            ## Prevention

            Simple lifestyle measures have been shown to be effective in preventing or delaying the onset of type 2 diabetes. To help prevent type 2 diabetes and its complications, people should:
            * achieve and maintain a healthy body weight;
            * be physically active – doing at least 30 minutes of regular, moderate-intensity activity on most days. More activity is required for weight control;
            * eat a healthy diet, avoiding sugar and saturated fats; and
            * avoid tobacco use – smoking increases the risk of diabetes and cardiovascular disease.
            """)

    st.write("""    
    ## Diagnosis and Treatment

    Early diagnosis can be accomplished through relatively inexpensive testing of blood sugar.
    
    Treatment of diabetes involves diet and physical activity along with lowering of blood glucose and the levels of other known risk factors that damage blood vessels. Tobacco use cessation is also important to avoid complications.
    Interventions that are both cost-saving and feasible in low- and middle-income countries include:
    * blood glucose control, particularly in type 1 diabetes. People with type 1 diabetes require insulin, people with type 2 diabetes can be treated with oral medication, but may also require insulin
    * blood pressure control and
    * foot care (patient self-care by maintaining foot hygiene; wearing appropriate footwear; seeking professional care for ulcer management; and regular examination of feet by health professionals). """)

    st.write(
        """
        ### Other cost saving interventions include:
        * screening and treatment for retinopathy (which causes blindness);
        * blood lipid control (to regulate cholesterol levels);
        * screening for early signs of diabetes-related kidney disease and treatment.
        """)

    
    
 

