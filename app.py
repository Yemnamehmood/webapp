import streamlit as st
import pandas as pd

# Set up the app
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1]

    # Read the file
    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Preview of Uploaded Data")
    st.dataframe(df.head())

    # Data Cleaning Options
    st.write("### Data Cleaning Options")
    if st.button("Drop Missing Values"):
        df.dropna(inplace=True)
        st.success("Missing values dropped successfully!")
        st.dataframe(df.head())

    if st.button("Drop Duplicates"):
        df.drop_duplicates(inplace=True)
        st.success("Duplicates dropped successfully!")
        st.dataframe(df.head())

    # Convert file format
    st.write("### Convert File Format")
    if st.button("Download as CSV"):
        df.to_csv("converted_file.csv", index=False)
        with open("converted_file.csv", "rb") as f:
            st.download_button("Download CSV", f, file_name="converted_file.csv")

    if st.button("Download as Excel"):
        df.to_excel("converted_file.xlsx", index=False)
        with open("converted_file.xlsx", "rb") as f:
            st.download_button("Download Excel", f, file_name="converted_file.xlsx")

    # Data Visualization
    st.write("### Data Visualization")
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())

    if st.checkbox("Show Column Names"):
        st.write(df.columns.tolist())

st.write("Upload a file to get started!")


