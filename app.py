import pandas as pd
import streamlit as st
from markdown import markdown

st.set_page_config(page_title="Credit Default Analysis", page_icon="favicon.png", layout="wide", initial_sidebar_state="expanded", menu_items=None)

#Preparing Features for Visualization
def balTobin(val):
    if val >= 200000:
        toReturn = "High"
    elif val >= 80000 and val < 200000:
        toReturn = "Medium"
    else:
        toReturn = "Low"
    return toReturn

def eduTobin(val):
    if val == 1:
        toReturn = "Graduate"
    elif val == 2:
        toReturn = "University"
    elif val == 3:
        toReturn = "High School"
    else:
        toReturn = "Other"
    return toReturn

def marTobin(val):
    if val == 1:
        toReturn = "Married"
    elif val == 2:
        toReturn = "Single"
    else:
        toReturn = "Other"
    return toReturn

def ageTobin(val):
    if val >= 34:
        toReturn = "Old"
    else:
        toReturn = "Young"
    return toReturn

def sexTobin(val):
    if val == 2:
        toReturn = "Female"
    else:
        toReturn = "Male"
    return toReturn

#Reading Data
df = pd.read_csv(r'D:\Interview Prep\Project\Credit Default\UCI_Credit_Card.csv')

#Preparing Features for Visualization
df['LIMIT_BAL'] = df['LIMIT_BAL'].apply(balTobin)
df['SEX'] = df['SEX'].apply(sexTobin)
df['EDUCATION'] = df['EDUCATION'].apply(eduTobin)
df['MARRIAGE'] = df['MARRIAGE'].apply(marTobin)
df['AGE'] = df['AGE'].apply(ageTobin)

#Only Keeping the columns we need for Visualization
df = df[["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "default.payment.next.month"]]

#Streamlit
selected_educations = []
selected_limit_bal_values = []
selected_sex_values = []
selected_marriage_values = []
selected_age_values = []

# Use the sidebar to create checkboxes for each unique value in the EDUCATION and LIMIT_BAL columns
sidebar = st.sidebar

# Add some text to organize the checkboxes
sidebar.subheader("Education")

# Create checkboxes for the education values
education_values = df["EDUCATION"].unique()
for value in education_values:
    if sidebar.checkbox(value, key=f"{value}EDUCATION", value =True): #Was producing key value error, as MARRIAGE and EDUCATION have 'Other'
        selected_educations.append(value)

# Add some text to organize the checkboxes
sidebar.markdown("---")
sidebar.subheader("Amount of Credit")

# Create checkboxes for the credit card limits
limit_bal_values = df["LIMIT_BAL"].unique()
for value in limit_bal_values:
    if sidebar.checkbox(value, key=value, value =True):
        selected_limit_bal_values.append(value)

# Add some text to organize the checkboxes
sidebar.markdown("---")
sidebar.subheader("Sex")

# Create checkboxes for the sex values
sex_values = df["SEX"].unique()
for value in sex_values:
    if sidebar.checkbox(value, key=value, value =True):
        selected_sex_values.append(value)

# Add some text to organize the checkboxes
sidebar.markdown("---")
sidebar.subheader("Marriage")

# Create checkboxes for the marriage values
marriage_values = df["MARRIAGE"].unique()
for value in marriage_values:
    if sidebar.checkbox(value, key=value, value =True):
        selected_marriage_values.append(value)

# Add some text to organize the checkboxes
sidebar.markdown("---")
sidebar.subheader("Age")

# Create checkboxes for the age values
age_values = df["AGE"].unique()
for value in age_values:
    if sidebar.checkbox(value, key=value, value =True):
        selected_age_values.append(value)

# Filter the DataFrame using the selected education levels, credit card limits, sex, marriage, and age
filtered_df = df[df["EDUCATION"].isin(selected_educations) & df["LIMIT_BAL"].isin(selected_limit_bal_values) & df["SEX"].isin(selected_sex_values) & df["MARRIAGE"].isin(selected_marriage_values) & df["AGE"].isin(selected_age_values)]

#title and short description explaining the project
st.title("Credit Default Analysis")
st.write("This is an interactive application that allows you to filter and analyze data on credit defaults.")

# Compute the average of the default.payment.next.month column
default_probability = filtered_df["default.payment.next.month"].mean()

# Use st.markdown() to display the average with bold text
st.markdown(markdown(f"Default probability of the selection : **<ins>{default_probability*100:.2f}%</ins>**"), unsafe_allow_html=True)

# Display the filtered DataFrame
st.dataframe(filtered_df, 1200, 600)

st.write("---")
st.subheader("Visualizations")

# Use st.columns() to create two columns
col1, col2 = st.columns(2)

with col1:
    # Display the first three bar charts
    for column in filtered_df.columns[:3]:
        # Skip the default.payment.next.month column
        if column == "default.payment.next.month":
            continue

        # Compute the count of each unique value in the column
        column_counts = filtered_df[column].value_counts()

        # Divide each count by the total number of rows in the DataFrame
        column_percentages = column_counts / len(filtered_df)

        st.write("---")

        # Use the st.bar_chart() method to create a bar chart
        st.bar_chart(column_percentages, width=400, height=400, use_container_width=False)

with col2:
    # Display the last two bar charts
    for column in filtered_df.columns[3:]:
        # Skip the default.payment.next.month column
        if column == "default.payment.next.month":
            continue

        # Compute the count of each unique value in the column
        column_counts = filtered_df[column].value_counts()

        # Divide each count by the total number of rows in the DataFrame
        column_percentages = column_counts / len(filtered_df)

        st.write("---")

        # Use the st.bar_chart() method to create a bar chart
        st.bar_chart(column_percentages, width=400, height=400, use_container_width=False)