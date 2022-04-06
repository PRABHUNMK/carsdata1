import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect

sql='Select * from cars;'
record=pd.DataFrame(postgreconnect.runquery(sql))
record.columns=['Name','Miles_Per_Gallon','Cylinders','Displacement','Horsepower','Weight_In_Lbs','Acceleration','Year','Origin']
st.title('Cars Data - Sourced from Heroku')
st.table(record)
