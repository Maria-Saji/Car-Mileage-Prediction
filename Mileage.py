import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# Finding the min and max values from the Dataset
df=pd.read_excel(r"C:\Users\SK\Downloads\mtcars.xlsx")

min_max_values = {
    'cyl': (df['cyl'].min(), df['cyl'].max()),
    'disp': (df['disp'].min(), df['disp'].max()),
    'hp': (df['hp'].min(), df['hp'].max()),
    'drat': (df['drat'].min(), df['drat'].max()),
    'wt': (df['wt'].min(), df['wt'].max()),
    'qsec': (df['qsec'].min(), df['qsec'].max()),
    'gear': (df['gear'].min(), df['gear'].max()),
    'carb': (df['carb'].min(), df['carb'].max())
}

# Streamlit app
st.image(r"C:\Users\SK\Downloads\innomaticslogo.webp")
st.title('Car Mileage Prediction')

# Load the trained model
model = pickle.load(open(r"C:\Users\SK\Machine Learning\car.pkl", "rb"))

#Inputs
Cycle=st.number_input("Enter Number of Cylinders required ",min_value=min_max_values['cyl'][0],max_value=min_max_values['cyl'][1],step=1)
disp=st.number_input("Enter the Engine Displacment ",min_value=min_max_values['disp'][0],max_value=min_max_values['disp'][1],step=50.5)
hp=st.number_input("Enter the Horse Power of the Car",min_value=min_max_values['hp'][0],max_value=min_max_values['hp'][1],step=10)
drat=st.number_input("Enter the Rear axle ratio",min_value=min_max_values['drat'][0],max_value=min_max_values['drat'][1],step=0.5)
wt=st.number_input("Enter the Weight of the Car",min_value=min_max_values['wt'][0],max_value=min_max_values['wt'][1],step=0.5)
qsec=st.number_input("Enter the quarter-mile time of the Car",min_value=min_max_values['qsec'][0],max_value=min_max_values['qsec'][1],step=0.5)
vs=st.radio("Enter the Engine Shape",['V-shaped Engine','Straight'])
shape=0 if vs=='V-shaped Engine' else 1 
am=st.radio("Enter the type of Transmission Required",['Automatic','Manual'])
type=0 if am=="Automatic" else 1
gear=st.number_input("Enter the Number of Gears required for the Car",min_value=min_max_values['gear'][0],max_value=min_max_values['gear'][1],step=1)
carb=st.number_input("Enter the Number of Carburetors required for the Car",min_value=min_max_values['carb'][0],max_value=min_max_values['carb'][1],step=1)


# Predict button
if st.button('Predict Mileage'):
    mpg=model.predict([[Cycle,disp,hp,drat,wt,qsec,shape,type,gear,carb]])[0]
    st.write("The Requirments matched and the Mileage of the Car is :",round(mpg,3),"miles per gallon")



