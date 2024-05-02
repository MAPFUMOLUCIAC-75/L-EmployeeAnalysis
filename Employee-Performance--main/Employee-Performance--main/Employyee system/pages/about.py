import streamlit as st

# Page title
st.title('About Lonestar Internation Employees System')

# Project description
st.header('Employee Performance Analysis and Prediction')
st.write('This project aims to analyze employees performance data,predict and provide insights into productivity trends and statistics.')

# Contributors
st.header('Contributors')
contributors = [
    {'name': 'Paida Mutize', 'id': 'R23222y'},
    {'name': 'Mapfumo Lucia Chido', 'id': 'R2113118T'},
    
]

for contributor in contributors:
    st.write(f"- {contributor['name']} ({contributor['id']})")

