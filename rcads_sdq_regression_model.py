import streamlit as st
import numpy as np 
import pandas as pd 

#Converting the json data to a dataframe
df = pd.read_json('data.json')

#Sidebar
st.sidebar.header('Completion filters')
st.sidebar.write('RCADS Clinical Ranges')
rcads_clinical_ranges = ['High','Medium','Low']
rcads_high = st.sidebar.checkbox(rcads_clinical_ranges[0])
rcads_medium = st.sidebar.checkbox(rcads_clinical_ranges[1])
rcads_low = st.sidebar.checkbox(rcads_clinical_ranges[2])
st.sidebar.write('SDQ Clinical Ranges')
sdq_clinical_ranges = ['Below Clinical Threshold','Borderline','Above Clinical Threshold']
sdq_below = st.sidebar.checkbox(sdq_clinical_ranges[0])
sdq_borderline = st.sidebar.checkbox(sdq_clinical_ranges[1])
sdq_above = st.sidebar.checkbox(sdq_clinical_ranges[2])

#Filtering


#Raw data section
st.title('RCADS SDQ Regression Model')
st.markdown("""
This interactive web app allows you to explore some of the RCADS and SDQ completions taken from patients who participated in low intensity therapy.
Feel free to explore some of the data and the regression model.  
""")
st.write('Raw Data - RCADS and SDQ scores')
st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns')
st.write(df)
