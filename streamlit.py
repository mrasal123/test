import streamlit as st
import json

from snowflake.snowpark import Session, version, Window, Row

# connect to Snowflake
with open('creds.json') as f: # check the creds-fake.json file for format
    connection_parameters = json.load(f)  
session = Session.builder.configs(connection_parameters).create()

# get Snowflake table data
employeeDf = session.table("employee")

# main entry form
with st.form("my_form"):
    st.write("### Enter employee details")

    name_val = st.text_input("Name")
    age_val = st.slider("Age",18,99,30)