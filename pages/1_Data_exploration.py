import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np


st.cache_data()
def load_data(csvfile):
    data = pd.read_csv(csvfile)
    return data

data = load_data('automobile.csv')

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-size: 50px; font-family: Helvetica'>CAR PRICE PREDICTION (DATA EXPLORATION)</h1>", unsafe_allow_html = True)

st.header('Project Background Information',divider = True)
st.write("This is vehicle price predictor based on entered inputs.")

st.markdown('<br>', unsafe_allow_html = True)
st.write('Below are charts used to explore on the data. The next page(app) allows you to enter relevant parameters about a vehicle and the app will predict the price of the vehicle')

def plotter(dataframe, col1, col2, col3, dep):
    plt.figure(figsize=(20,8))

    plt.subplot(1,3,1)
    st.subheader(f"{col1} vs {col2}, vs {dep}")
    col1plot = px.scatter_3d(data_frame= dataframe, x = col1, z  = col2, y = dep)
    st.plotly_chart(col1plot)
    
    st.markdown('<br>',  unsafe_allow_html=True)

    plt.subplot(1,3,2)
    st.subheader(f"{col2} vs {col3}, {dep}")
    col2plot = px.scatter_3d(data_frame= dataframe, x = col2, y=dep, z=col3)
    st.plotly_chart(col2plot)
  
    st.markdown('<br>',  unsafe_allow_html=True)

    plt.subplot(1,3,3)
    st.subheader(f"{col3} vs {col1}, {dep}")
    col3plot = px.scatter_3d(data_frame= dataframe, x = col3, y = dep, z=col1)
    st.plotly_chart(col3plot)

    st.markdown('<br>',  unsafe_allow_html=True)

plotter(data, 'symboling', 'wheel-base', 'length', 'price')
plotter(data, 'width', 'curb-weight', 'engine-size', 'price')	
    





