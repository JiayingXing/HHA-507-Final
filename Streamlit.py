 
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Part 2 Streamlit
import streamlit as st
import pandas as pd
import numpy as np
import time


@st.cache
def load_hospitals():
   hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospitaldf
@st.cache
def load_inpatient():
    inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatientdf
@st.cache
def load_outpatient():
    outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatientdf

# FAKE LOADER BAR TO STIMULATE LOADING 
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)  

st.title('HHA 507 - Final Assignment')
st.write('Jiaying Xing :sunglasses:') 
st.write('This app answers the following questions:')
st.write('1. How does Stony Brooks hospital type compare to the rest of New York?')
st.write('2. Which DRG code has the highest total discharges for New York?')
st.write('3. Which APC code has the largest number of services for New York?')
st.write('4. Which state has the largest number of hospitals?')
st.write('5. What is the most common type of hospital?')
st.write('6. Which hospital has the highest hospital overall rating in New York? ')

hospitaldf = load_hospitals()
inpatientdf = load_inpatient()
outpatientdf = load_outpatient()

st.header('Hospital Data Preview')
st.dataframe(hospitaldf)

st.header('Outpatient Data Preview')
st.dataframe(inpatientdf)

st.header('Inpatient Data Preview')
st.dataframe(outpatientdf)

SBU_hospital= hospitaldf[hospitaldf['hospital_name'] == 'STONY BROOK UNIVERSITY HOSPITAL']
st.header('Info for Stony Brook University Hospital')
st.markdown('This dataset shows information for Stony Brook University Hospital')
st.dataframe(SBU_hospital)

##create df
NY_hospital = hospitaldf[hospitaldf['state'] == 'NY']
st.header('Summary Info for Hospitals in New York')
st.markdown('This dataset shows hospitals located in New York, filtered out from the main hospital dataframe, excluding SBU hospital')
st.dataframe(NY_hospital)

#Q1 answer
table1 =  NY_hospital['hospital_type'].value_counts().reset_index()
st.header('1. How does Stony Brooks hospital type compare to the rest of New York?')
st.markdown('This dataset shows the 5 hospital types and their amounts for New York state.')
st.dataframe(table1)

##create df
SBU_inpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('2. Which DRG code has the highest total discharges for New York?')
st.markdown('This dataset shows Stony Brook University Hospital inpatient data which is filtered from the primary inpatient dataset')
st.dataframe(SBU_inpatient)

#Q2 answer
st.header('Q2. What is the most expensive inpatient DRGs code for Stony Brook University Hospital?')
SBU_inpatient_DRGs_pivot = SBU_inpatient.pivot_table(index=['provider_id','provider_name','drg_definition'],values=['average_total_payments'])
SBU_inpatient_DRGs = SBU_inpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')
st.dataframe(SBU_inpatient_DRGs)

##create df
SBU_outpatient = outpatientdf[outpatientdf['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.dataframe(SBU_outpatient)

#Q3 answer
st.header('Q3. What is the most expensive inpatient APCs code for Stony Brook University Hospital?')
SBU_outpatient_DRGs_pivot = SBU_outpatient.pivot_table(index=['provider_id','provider_name','apc'],values=['average_total_payments'])
SBU_outpatient_DRGs = SBU_outpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(SBU_outpatient_DRGs)

