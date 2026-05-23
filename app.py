import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Page setup
st.set_page_config(layout="wide")

# Load CSV file
df = pd.read_csv("abu.csv")

# CSS style
st.markdown("""
<style>
div.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Streamlit Dashboard")

# Image (make sure file exists)
image = Image.open("sun_logo.jpg")
st.image(image, width=200)

# Show data
st.subheader("Data Table")
st.dataframe(df)

# Chart (only if enough columns)
if len(df.columns) >= 2:
    fig = px.bar(df, x=df.columns[0], y=df.columns[1])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("CSV must have at least 2 columns")
