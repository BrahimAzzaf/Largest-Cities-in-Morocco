import pandas as pd 
import streamlit as st
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title='Largest Cities in Morocco')
st.header('Largest Cities in Morocco')
 
excel_file ="Largest Cities in Morocco.xlsx"
sheet_name ="LCM"
Image = Image.open('images/mosque.png')
st.image(Image,
         width=300)


# Image = Image.open('images/mosque.png')
# st.image(Image,
#          width=300)

                
df_City_Name=pd.read_excel(excel_file,
                  sheet_name=sheet_name,
                  usecols='B:c',
                  header=1)


st.dataframe(df_City_Name)

pie_chart =px.pie(df_City_Name,
                  title='Largest Cities in Morocco',
                  values= 'POPULATION',
                  names='CITY NAME')

st.plotly_chart(pie_chart)

