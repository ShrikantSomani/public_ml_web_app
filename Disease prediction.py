# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 10:31:12 2025

@author: shrik
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


loaded_model=pickle.load(open('trained_model.sav','rb'))
loaded_model1=pickle.load(open('trained_model1.sav','rb'))
 
with st.sidebar:
    selected=option_menu(
        'Multiple Disease Prediction',
        ['Diabetes Prediction','Heart Disease Prediction'],
        icons=['activity','heart']
        )
    
if(selected=='Diabetes Prediction'):
    st.title('Diabeties Prediction System')
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('BloodPressure')
    with col1:
        SkinThickness=st.text_input('SkinThickness')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    with col2:
        Age=st.text_input('Age')
        
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        diab_pred=loaded_model.predict([[Pregnancies,	Glucose,	BloodPressure	,SkinThickness,	Insulin,	BMI	,DiabetesPedigreeFunction	,Age]])
        if(diab_pred==0):
            diab_diagnosis='The person is not  diabetic'
        if(diab_pred==1):
            diab_diagnosis='The person is diabetic'
    st.success(diab_diagnosis)
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction System')
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Cp')
    with col1:
        trestbps=st.text_input('TrestBps')
    with col2:
        chol=st.text_input('Cholestrol')
    with col3:
        fbs=st.text_input('FBS')
    with col1:
        restecg=st.text_input('ResTecg')
    with col2:
        thalach=st.text_input('Thalach')
    with col3:
        exang=st.text_input('exang')
    with col1:
        oldpeak=st.text_input('oldpeak')
    with col2:
        slope=st.text_input('slope')
    with col3:
        ca=st.text_input('ca')
    with col1:
        thal=st.text_input('thal')
        
    heart_diagnosis=''
    if st.button('Heart Disesase Results'):
        heart_pred=loaded_model1.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_pred==0):
            heart_diagnosis='The person do not have heart disease'
        if(heart_pred==1):
            heart_diagnosis='The person has heart disease'
    st.success(heart_diagnosis)
    
       