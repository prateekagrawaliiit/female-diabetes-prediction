import streamlit as st
from multiapp import MultiApp
from apps import about,diabetes_prediction
st.title('DIABETES PREDICTION')
app = MultiApp()
app.add_app("Health Check", diabetes_prediction.app)
app.add_app("About-Diabetes", about.app)
app.run()

