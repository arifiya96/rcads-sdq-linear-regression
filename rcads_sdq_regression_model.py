import streamlit as st
import numpy as np 
import pandas as pd 
import altair as alt
import base64

#Converting the json data to a dataframe
df = pd.read_json('data.json')

#Sidebar
st.sidebar.header('Completion filters')
st.sidebar.write('RCADS Clinical Ranges')
rcads_bandings = ['Low','Medium','High']
selected_rcads_banding = st.sidebar.multiselect('RCADS Bandings', rcads_bandings, rcads_bandings)
st.sidebar.write('SDQ Clinical Ranges')
sdq_bandings = ['Below Clinical Threshold','Borderline','Above Clinical Threshold']
selected_sdq_banding = st.sidebar.multiselect('SDQ Bandings', sdq_bandings, sdq_bandings)
st.sidebar.header('SDQ Total Score Predictor')
rcads_score = st.sidebar.slider('RCADS Total Score', 0, 130)
sdq_predicted_score = np.around((0.09*rcads_score) + 7.95)
st.sidebar.write('SDQ Predicted Score: ' + str(sdq_predicted_score)) 

#Filtering
df_selected = df[(df.rcads_banding.isin(selected_rcads_banding)) & (df.sdq_banding.isin(selected_sdq_banding))]

#Raw data section
st.title('RCADS SDQ Regression Model')
st.markdown("""
This interactive web app allows you to explore some of the RCADS and SDQ completions taken from patients who participated in low intensity therapy.
Feel free to explore some of the data and the regression model.  
""")
st.write('Raw Data - RCADS and SDQ scores')
st.write('Data Dimension: ' + str(df_selected.shape[0]) + ' rows and ' + str(df_selected.shape[1]) + ' columns')
st.write(df_selected)

#Linear regression model
st.title('Linear Regression - RCADS SDQ Completions')
scatter_chart = st.altair_chart(
    alt.Chart(df).mark_circle(size=60).encode(x='rcads_score_anx_dep_t2',y='sdq_total_t2',tooltip=['rcads_score_anx_dep_t2','sdq_total_t2']).interactive()
)
st.write('Regression Equation: SDQ_Score(Y) = 0.09x + 7.95')

