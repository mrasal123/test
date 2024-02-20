import streamlit as st
from snowflake.snowpark import Session

st.title('❄️ Connect Streamlit to a Snowflake database')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")


# Load data table
@st.cache_data

def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)
    
    ## Do some computation on it
    table = table.limit(20)
       
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "ADIDAS.PUBLIC.ADIDAS"

## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)

st.button("Filter data")

RETAILER_ID_shelter = ['1185732', '001', '002', '003']
RETAILER_ID = st.text_input('Type an RETAILER_ID')
if st.button('Check availability'):
    have_it = RETAILER_ID.lower() in RETAILER_ID_shelter
    'We have that RETAILER_ID!' if have_it else 'We don\'t have that RETAILER_ID.'