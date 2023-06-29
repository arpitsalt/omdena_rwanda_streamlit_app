import streamlit as st
from PIL import Image
import streamlit_option_menu

st.set_page_config(page_title="Omdena Rwanda", page_icon=":rwanda:", initial_sidebar_state="expanded")
img_banner = Image.open("assets/banner.png")
img_banner2 = Image.open("assets/banner2.png")
img_rwanda = Image.open("assets/rwanda-logo.png")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}


def home_page():
    st.write(f"""# Water Inspection System""", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(f"""<h1>The Problem</h1> 
            <p>Access to clean water is a critical challenge in many parts of the world, 
            including Rwanda. Water quality prediction is important for ensuring the availability of safe and clean water for 
            drinking, agriculture, and other purposes. However, traditional methods for water quality prediction are often 
            time-consuming and costly, and they may not provide accurate and timely information. To address this challenge, 
            the Omdena Rwanda Chapter has initiated a project to develop an automated water quality prediction system using 
            machine learning.</p> """, unsafe_allow_html=True)

    st.write(f"""<h1>Project goals</h1> <p>In this project, the Omdena Rwanda Chapter’s primary goal in this project 
            is to develop an accurate and efficient machine learning model that can predict water quality based on a range of 
            parameters such as Electrical conductivity of water, Amount of organic carbon in ppm, Amount of Trihalomethanes 
            in μg/L, and turbidity. The model will be trained on a large dataset of historical water quality data and will be 
            designed to provide predictions for water quality..</p> """, unsafe_allow_html=True)


def about_section():
    st.write(f"""<h1>Project background</h1>""", unsafe_allow_html=True)
    st.write("""
        <p>Rwanda is a landlocked country located in East Africa, 
        with a population of approximately 13 million people. Despite efforts to improve access to clean water, 
        access remains a critical challenge, particularly in rural areas. According to UNICEF, only 47% of the population 
        has access to basic water services, and only 32% have access to safely managed drinking water services. One of 
        the challenges in ensuring access to clean water is predicting and monitoring water quality. Traditional water 
        quality prediction and monitoring methods are often time-consuming, costly, and may not provide timely and 
        accurate information. This can lead to delays in identifying and addressing water quality issues, putting public 
        health and agricultural productivity at risk. <br> <br> Machine learning has the potential to revolutionize water 
        quality prediction and monitoring by providing a faster, more accurate, and cost-effective method for predicting 
        water quality. By analyzing large datasets of water quality parameters, machine learning models can identify 
        patterns and relationships between different parameters, enabling accurate predictions of water quality.</p><br>
    """, unsafe_allow_html=True)
    st.image(img_banner2)



def model_page():
    st.error("No models to show for now.")


def contributors_page():
    def contributors():
        for i in range(10):
            st.write("- contributor name")

    col1, col2, col3 = st.columns(3)
    with col1:
        contributors()
    with col2:
        contributors()
    with col3:
        contributors()


with st.sidebar:
    st.image(img_rwanda)
    selected = streamlit_option_menu.option_menu(
        menu_title=None,  # required
        options=["Home", "About", "Model", "Contributors"],
        icons=["house", "info-circle", "gear", "people"],  # optional
        styles=css_style
    )

if selected == "Home":
    home_page()

if selected == "About":
    about_section()

if selected == "Model":
    model_page()

if selected == "Contributors":
    st.write("## A heart felt thankyou to all of our contributors <br><br>", unsafe_allow_html=True)
    contributors_page()
