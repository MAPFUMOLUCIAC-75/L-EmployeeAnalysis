

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset from Excel
data = pd.read_csv(r'C:\Users\LogicFiveZW\Desktop\Employyee system\pages')


# Page title
st.title('Employee Data')

# Sidebar filter
display_option = st.sidebar.radio("Display Option", ('Employee Perfromance Data', 'Total Crimes Per Each Employee', 'Total Perfomance Per month'))

# Filtered display
if display_option == 'Employee Data':
    # Display the dataset as a table
    st.subheader('Employee Data')
    st.write(data)

elif display_option == 'Total Perfomance Per Each Employee':
    # Group the data by category and calculate the sum of each month
    grouped_data = data.groupby('Category').sum().drop(['Employee name', 'surname'], axis=1)

    # Line chart for performance trends by category over the years
    st.subheader('Performance Trends by Employee')
    fig, ax = plt.subplots()
    lines = sns.lineplot(data=grouped_data.T, ax=ax)
    plt.xlabel('Month')
    plt.ylabel('Number of Performances')
    plt.xticks(rotation=45)

    # Add legend with categories beside the line graph
    categories = grouped_data.index
    lines.legend(labels=categories, title='Employees', loc='center left', bbox_to_anchor=(1, 0.5))

    st.pyplot(fig)
elif display_option == 'Total CATAGORIES Per Year':
    # Group the data by category and calculate the sum of each month
    grouped_data = data.groupby('Category').sum().drop(['Province', 'Major cities'], axis=1)

    # Bar chart for total crimes by month
    st.subheader('Total Performance by month')
    fig, ax = plt.subplots()
    grouped_data.sum().plot(kind='bar', ax=ax)
    plt.xlabel('Year')
    plt.ylabel('Number of catagories')
    plt.xticks(rotation=45)
    st.pyplot(fig)




