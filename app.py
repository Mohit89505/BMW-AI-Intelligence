import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import urllib.parse

# 1. Database Connection ki settings
user = "root"
password = "YOUR Password"
encoded_password = urllib.parse.quote_plus(password)
host = "localhost"
db_name = "bmw_db"

# Engine setup
engine = create_engine(f"mysql+mysqlconnector://{user}:{encoded_password}@{host}/{db_name}")

st.set_page_config(page_title="BMW AI Intelligence", layout="wide")
st.title("BMW Customer Intelligence & AI Strategy (Live SQL)")

# 2. Data Load from mysql
@st.cache_data 
def fetch_data_from_sql(): 
    query = "SELECT * FROM customer_analytics"
    df = pd.read_sql(query, engine)
    return df

try:

    df = fetch_data_from_sql() 
    
    st.sidebar.header("Geography Filter")
    cities = st.sidebar.multiselect("Select Cities", df['city'].unique(), default=df['city'].unique())
    f_df = df[df['city'].isin(cities)]

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Leads", len(f_df))
    m2.metric("Avg. Income", f"{round(f_df['income_lpa'].mean(),1)}L")
    m3.metric("Conversion Rate", f"{round((f_df['purchase'].sum()/len(f_df))*100,1)}%")

    st.divider()

    # Visuals
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Customer Personas")
        fig1 = px.pie(f_df, names='persona', color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig1, use_container_width=True)
    
    with c2:
        st.subheader("Income vs Age (Cluster View)")
        fig2 = px.scatter(f_df, x="age", y="income_lpa", color="persona", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

    # Next Best Action Table
    st.subheader("Targeted Marketing: Next Best Actions")
    if 'next_action' in f_df.columns:
        st.table(f_df[['customer_id', 'persona', 'journey_stage', 'next_action']].head(10))
    else:
        st.info(" IN MySQL table 'next_action' column not found. RUN PIPELINE BEFORE PROCEED!")

except Exception as e:
    st.error(f"❌ Connection Error: {e}")
    st.info("PLEASE ENSURE THA THE TABLE IN  MySQL  'bmw_db' OR 'customer_analytics' ARE PRESENT.")
