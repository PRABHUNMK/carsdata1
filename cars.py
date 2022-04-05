import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2-binary as psycopg2

#Connect to the heroku postgresql database
connection=psycopg2.connect(user="yfxpgallicmvhs",
                            password="b42a0e5bddc705436e3b39271057b781cc398451ad2292d785d2311927cfbfa1",
                            host="ec2-52-54-212-232.compute-1.amazonaws.com",
                            database="dc802bu83sg0v6")

#Create a cursor to perform database operations
cursor=connection.cursor()


#Execute SQL Query
cursor.execute ("Select * from public.cars;")

#Fetch result
record=pd.DataFrame(cursor.fetchall())
st.write(record)

cursor.close()
connection.close()
