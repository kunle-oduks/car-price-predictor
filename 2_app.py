import pandas as pd
import numpy as np
import streamlit as st
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = 'Main Page'
)
st.title('Main Page')
st.sidebar.success('Choose a page above')

st.sidebar.image('pngwing.com (8).png')

st.cache_data()
def load_data(csvfile):
    data = pd.read_csv(csvfile)
    return data



data = load_data('automobile.csv')

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-size: 60px; font-family: Helvetica'>CAR PRICE PREDICTOR APP</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By Gomycode Data Science</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)
st.image('pngwing.com (7).png', width = 400,  caption = 'CAR PRICE PREDICTION PROJECT')

sel_cols = ['curb-weight', 'symboling', 'normalized-losses', 'make', 'body-style', 'city-mpg','length', 'price' ]

curb_weight = st.sidebar.number_input('Enter curb weight', min_value = data['curb-weight'].min(), max_value = data['curb-weight'].max())
symboling = st.sidebar.slider('Symboling', min_value = data['symboling'].min(), max_value = data['symboling'].max())
normalized_losses = st.sidebar.number_input('normalized-losses', min_value = data['normalized-losses'].min(), max_value = data['normalized-losses'].max())
make = st.sidebar.selectbox('Enter Make of Car', options = data['make'].unique())
body_style = st.sidebar.selectbox('Enter body style', options = data['body-style'].unique())
city_mpg = st.sidebar.number_input('Enter city', min_value = data['city-mpg'].min(), max_value = data['city-mpg'].max())
length = st.sidebar.slider('Enter Length of car', min_value = data['length'].min(), max_value = data['length'].max())

st.markdown("<br>", unsafe_allow_html=True)
user_input = pd.DataFrame()
user_input['curb-weight'] = [curb_weight]
user_input['symboling'] = [symboling]
user_input['normalized-losses'] = normalized_losses
user_input['make'] = make
user_input['body-style'] = body_style
user_input['city-mpg'] = city_mpg
user_input['length'] = length

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-size: 20px; font-family: Helvetica'>USER INPUTS</h1>", unsafe_allow_html = True)
st.dataframe(user_input, use_container_width = True)

#download model and encoders
@st.cache_data()
def download_models(encoder_file):
    encoder_name = joblib.load(encoder_file)
    return encoder_name

make_encoder = download_models('make_encoder.pkl')
body_style_encoder = download_models('body-style_encoder.pkl')

model_rfn = download_models('model_rfn.pkl')
model_xgb = download_models('model_xgb.pkl')

user_input['make'] = make_encoder.transform(user_input[['make']])
user_input['body-style'] = body_style_encoder.transform(user_input[['body-style']])
#user_input['TOP_PACK'] = Tpacks_encoder.transform(user_input[['TOP_PACK']])

st.markdown('<br>', unsafe_allow_html = True)
st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-size: 20px; font-family: Helvetica'>TRANSFORMED INPUTS INPUTS</h1>", unsafe_allow_html = True)

st.dataframe(user_input, use_container_width = True)

c =st.container(border = True)

def predict():
    price_predict = model_xgb.predict(user_input).round(2)
    c.write(f"Price of {make} with details inputted is estimated to be ${price_predict[0]:,.2f}")


c.button('Predict', on_click = predict)
