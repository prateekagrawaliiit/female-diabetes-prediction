import streamlit as st
from multiapp import MultiApp
from apps import about,diabetes_prediction,who_standards
from PIL import Image
st.markdown("<h1 style='text-align: center; color: green;'>EARLY DIABETES DETECTION</h1>", unsafe_allow_html=True)
app = MultiApp()
image = Image.open('data/diabetes_image.jpg')
    # st.image(image, use_column_width=False)

st.sidebar.image(image, width=300)
app.add_app("Health Check", diabetes_prediction.app)
app.add_app("About-Diabetes", about.app)
app.add_app("WHO-Standards", who_standards.app)
app.run()

