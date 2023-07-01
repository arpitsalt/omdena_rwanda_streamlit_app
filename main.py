import stqdm
import pickle
import pandas as pd
from PIL import Image
from time import sleep
import streamlit as st
from stqdm import stqdm
import random
from streamlit_option_menu import option_menu

# Configuring Streamlit
st.set_page_config(page_title="Omdena Rwanda", page_icon="🇷🇼", initial_sidebar_state="expanded")

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

# Loading assets
img_banner = Image.open("assets/images/banner.png")
img_banner2 = Image.open("assets/images/banner2.png")
img_rwanda = Image.open("assets/images/rwanda-logo.png")


def home_page():
    st.write(f"""# Water Inspection System""", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(f"""<h2>The Problem</h2>   
    <p>Access to clean water is a critical challenge in many parts of the world, 
    including Rwanda. Water quality prediction is important for ensuring the availability of safe and clean water for 
    drinking, agriculture, and other purposes. However, traditional methods for water quality prediction are often 
    time-consuming and costly, and they may not provide accurate and timely information. To address this challenge, 
    the Omdena Rwanda Chapter has initiated a project to develop an automated water quality prediction system using 
    machine learning.</p> """, unsafe_allow_html=True)

    st.write(f"""<h2>Project goals</h2> <p>In this project, the Omdena Rwanda Chapter’s primary goal in this project 
    is to develop an accurate and efficient machine learning model that can predict water quality based on a range of 
    parameters such as Electrical conductivity of water, Amount of organic carbon in ppm, Amount of Trihalomethanes 
    in μg/L, and turbidity. The model will be trained on a large dataset of historical water quality data and will be 
    designed to provide predictions for water quality..</p> """, unsafe_allow_html=True)


def about_page():
    st.write("""<h1>Project background</h1><hr>
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


def model_section():
    st.write("""<h1>Predict Water Quality</h1>
    <p>Enter these values of the parameters to know if the water quality is suitable to drink or not.</p><hr>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        ColourTCU = st.number_input(label="Colour (TCU)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider0")
        TurbidityNTU = st.number_input(label="Turbidity (NTU)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                       key="test_slider1")
        pH = st.number_input(label="pH", min_value=0.0, max_value=1000.0, step=50.0, format="%f", key="test_slider2")
        ConductivityuS = st.number_input(label="Conductivity (uS/cm)", min_value=0.0, max_value=1000.0, step=50.0,
                                         format="%f", key="test_slider3")
        TotalDissolvedSolids = st.number_input(label="Total Dissolved Solids (mg/l)", min_value=0.0, max_value=1000.0,
                                               step=50.0, format="%f", key="test_slider4")
        TotalHardness = st.number_input(label="Total Hardness (mg/l as CaCO3)", min_value=0.0, max_value=1000.0,
                                        step=50.0, format="%f", key="test_slider5")

    with col2:
        Aluminium = st.number_input(label="Aluminium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider6")
        Chloride = st.number_input(label="Chloride (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                   key="test_slider7")
        Iron = st.number_input(label="Iron (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                               key="test_slider8")
        Sodium = st.number_input(label="Sodium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                 key="test_slider9")
        Sulphate = st.number_input(label="Sulphate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                   key="test_slider10")
        Zinc = st.number_input(label="Zinc (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                               key="test_slider11")

    with col3:
        Magnesium = st.number_input(label="Magnesium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider12")
        Calcium = st.number_input(label="Calcium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                  key="test_slider13")
        Potassium = st.number_input(label="Potassium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider14")
        Nitrate = st.number_input(label="Nitrate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                  key="test_slider15")
        Phosphate = st.number_input(label="Phosphate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider16")
        st.write("<br>", unsafe_allow_html=True)
        predict_button = st.button('  Predict Water Quality  ')

    dataframe = pd.DataFrame({'Colour (TCU)': [ColourTCU], 'Turbidity (NTU)': [TurbidityNTU], 'pH': [pH],
                              'Conductivity (uS/cm)': [ConductivityuS],
                              'Total Dissolved Solids (mg/l)': [TotalDissolvedSolids],
                              'Total Hardness (mg/l as CaCO3)': [TotalHardness], 'Aluminium (mg/l)': [Aluminium],
                              'Chloride (mg/l)': [Chloride], 'Total Iron (mg/l)': [Iron],
                              'Sodium (mg/l)': [Sodium], 'Sulphate (mg/l)': [Sulphate], 'Zinc (mg/l)': [Zinc],
                              'Magnesium (mg/l)': [Magnesium], 'Calcium (mg/l)': [Calcium],
                              'Potassium (mg/l)': [Potassium], 'Nitrate (mg/l)': [Nitrate],
                              'Phosphate (mg/l)': [Phosphate]})

    with open('assets/model.pkl', 'rb') as f:
        model = pickle.load(f)

    if predict_button:
        result = model.predict(dataframe)
        for _ in stqdm(range(50)):
            sleep(0.015)
        if result[0] == 1.0:
            st.error("This Water Quality is Non-Potable")
        else:
            st.success('This Water Quality is Potable')


def contributors_page():
    def contributors():
        for i in range(10):
            st.write("- contributor name")

    st.write("""<h1 style="text-align: center;">A heartfelt thankyou to all our contributors ❤️</h1><hr><br>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        contributors()
    with col2:
        contributors()
    with col3:
        contributors()


with st.sidebar:
    st.image(img_rwanda)
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "About", "Model", "Contributors"],
        icons=["house", "info-circle", "gear", "people"],  # optional
        styles=css_style
    )

if selected == "Home":
    home_page()

elif selected == "About":
    about_page()

elif selected == "Model":
    model_section()

elif selected == "Contributors":
    contributors_page()
