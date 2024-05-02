import streamlit as st
import pandas as pd

# Read the dataset from Excel
data = pd.read_csv("C://Users//angels.makuwerere//Desktop//Employee-Performance--main//Employee-Performance--main//Employyee system//pages//employee records.csv")

# Page title
st.title('Employee data Statistics')

# Display the dataset as a table
st.subheader('Data Table')
st.write(data)

# Calculate statistics
statistics = {
    'Total Crimes': data.iloc[:, 3:].sum().sum(),
   
    'Total Employees': data['Catagories'].nunique(),
    'Total Categories': data['Category'].nunique()
}

# Display the statistics
st.subheader('Statistics')
for stat_name, stat_value in statistics.items():
    st.write(f'- {stat_name}: {stat_value}')

# Bar chart for total performance by month
st.subheader('Total Performance by Month')
month_columns = [col for col in data.columns if col.startswith('20')]
monthly_total = data[month_columns].sum()
st.bar_chart(monthly_total)

## Bar chart for total performance by employee
st.subheader('Total Performance by Employee')
employee_total = data.groupby('Employee name')[month_columns].sum()
st.bar_chart(employee_total)

# Bar chart for total performance by category
st.subheader('Total Performance by Category')
category_total = data.groupby('Category')[month_columns].sum()
st.bar_chart(category_total)

