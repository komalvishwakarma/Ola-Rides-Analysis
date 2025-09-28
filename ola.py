import streamlit as st
from PIL import Image

# Set the page to a wide layout
st.set_page_config(layout="wide")

# App title
st.title("Ola Ride Insights Project Showcase")

# --- Create Tabs for Each Dashboard Page ---
st.header("Power BI Dashboard Snapshots")
st.write("Click through the tabs below to see the different pages of the final dashboard.")

# Define the tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"])

# --- Add Content to Each Tab ---
with tab1:
    st.subheader("Overall Dashboard View")
    try:
        image = Image.open('overall.png')
        st.image(image, use_container_width=True) # Updated parameter
    except FileNotFoundError:
        st.error("Error: 'overall.png' not found. Please save your screenshot with this name in the same folder.")

with tab2:
    st.subheader("Vehicle Type Analysis")
    try:
        image = Image.open('vehicle_type.png')
        st.image(image, use_container_width=True) # Updated parameter
    except FileNotFoundError:
        st.error("Error: 'vehicle_type.png' not found. Please save your screenshot with this name.")

with tab3:
    st.subheader("Revenue Insights")
    try:
        image = Image.open('revenue.png')
        st.image(image, use_container_width=True) # Updated parameter
    except FileNotFoundError:
        st.error("Error: 'revenue.png' not found. Please save your screenshot with this name.")

with tab4:
    st.subheader("Cancellation Analysis")
    try:
        image = Image.open('cancellation.png')
        st.image(image, use_container_width=True) # Updated parameter
    except FileNotFoundError:
        st.error("Error: 'cancellation.png' not found. Please save your screenshot with this name.")

with tab5:
    st.subheader("Driver & Customer Ratings")
    try:
        image = Image.open('ratings.png')
        st.image(image, use_container_width=True) # Updated parameter
    except FileNotFoundError:
        st.error("Error: 'ratings.png' not found. Please save your screenshot with this name.")