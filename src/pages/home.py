import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def write():
    udisp.title_awesome(" x MOOC")
    
    
    keys = {
    "Coursera Dataset": './data/coursera.csv'
            }
    image = Image.open('./img/esteem.jpg')
    st.image(image, use_column_width=True)
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys))
    
        
    df = pd.read_csv(keys[pick], encoding='utf8')
    st.dataframe(df)
    #st.header("")
    #films = df["Title"].tolist()
    #st.header("")
    #st.header("Films")
    #tags = st.multiselect("Choose a Title", films)
    
    #for i in tags:
    #    filtered_data_vic = df[df['Title'] == str(i)]
    #    st.dataframe(filtered_data_vic)    
    
    #st.header("")
    #st.header("Group Dataset")
    #group = {
    #'Genre',
    #'Production Company',
    #'Production date'   
    #        }
    #pick_grp = st.selectbox("Groupby: ", list(group))
    
    #df3 = df.groupby(pick_grp).count()
    
    #df3 = df3[['Title']]
    #df3.columns = ['Count']
    
    #st.dataframe(df3)
    
    
    
    #df3['x-axis'] = df3.index
        
    #st.header("")
    #st.subheader("Line Graph of " + str(pick_grp) + " by count" )
    #fig2 = px.line(df3, x="x-axis", y="Count")
    #st.plotly_chart(fig2)
    
    
    #fig = px.scatter(df3, x="x-axis", y="Count")
    
    
    #st.header("")
    #st.subheader("Scatter Diagram of " + str(pick_grp) + " by count" )

    #st.plotly_chart(fig)
    
    #st.header("")
    #st.subheader("Pie Chart of " + str(pick_grp) + " by count" )
    
    #fig1 = go.Figure(data=[go.Pie(labels=df3['x-axis'], values=df3['Count'])])
    #st.plotly_chart(fig1)
