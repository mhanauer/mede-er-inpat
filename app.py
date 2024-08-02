import streamlit as st
import pandas as pd
import numpy as np

# Generate a dataframe with the required columns
data = {
    'member_id': range(1, 101),
    'age': np.random.randint(18, 85, size=100),
    'gender': np.random.choice(['Male', 'Female'], 100),
    'allowed_pmpm': np.random.uniform(100, 5000, size=100)
}

df = pd.DataFrame(data)

# Define a list of real chronic conditions
chronic_conditions = [
    'Diabetes', 'Hypertension', 'Chronic Kidney Disease', 'Asthma', 
    'COPD', 'Heart Failure', 'Depression', 'Arthritis'
]

# Assign real chronic condition names to the dataframe
df['chronic_condition'] = np.random.choice(chronic_conditions, 100)

# Add columns for ER visits and Re-admissions predictions
np.random.seed(42)  # For reproducibility
df['predicted_er_visits'] = np.random.uniform(0, 100, size=100)
df['predicted_readmissions'] = np.random.uniform(0, 100, size=100)

# Define criteria for categorizing ER visits and Re-admissions
def categorize_er_visits(pred):
    if pred >= 75:
        return 'Unavoidable ER'
    elif pred >= 35:
        return 'Impactable ER'
    else:
        return 'Unlikely ER'

def categorize_readmissions(pred):
    if pred >= 75:
        return 'Unavoidable Re-admissions'
    elif pred >= 35:
        return 'Impactable Re-admissions'
    else:
        return 'Unlikely Re-admissions'

df['er_visits_category'] = df['predicted_er_visits'].apply(categorize_er_visits)
df['readmissions_category'] = df['predicted_readmissions'].apply(categorize_readmissions)

# Streamlit app
st.title('Healthcare Claimants Analysis')

# Section 1: Chronic Conditions and ER Visits
st.header('Filter Data: Chronic Conditions and ER Visits')

# Selectors for chronic conditions
chronic_condition_filter_1 = st.multiselect('Select Chronic Conditions', options=chronic_conditions, default=chronic_conditions)
filtered_df_1 = df[df['chronic_condition'].isin(chronic_condition_filter_1)]

# Selectors for ER visit categories
er_visits_categories = ['Unavoidable ER', 'Impactable ER', 'Unlikely ER']
er_visits_category_filter = st.multiselect('Select ER Visit Categories', options=er_visits_categories, default=er_visits_categories)
filtered_df_1 = filtered_df_1[filtered_df_1['er_visits_category'].isin(er_visits_category_filter)]

# Display the filtered dataframe for Section 1
st.subheader('Filtered Dataframe: Chronic Conditions and ER Visits')
st.dataframe(filtered_df_1)

# Section 2: Chronic Conditions and Readmissions
st.header('Filter Data: Chronic Conditions and Readmissions')

# Selectors for chronic conditions
chronic_condition_filter_2 = st.multiselect('Select Chronic Conditions', options=chronic_conditions, default=chronic_conditions, key='readmissions')
filtered_df_2 = df[df['chronic_condition'].isin(chronic_condition_filter_2)]

# Selectors for readmissions categories
readmissions_categories = ['Unavoidable Re-admissions', 'Impactable Re-admissions', 'Unlikely Re-admissions']
readmissions_category_filter = st.multiselect('Select Readmissions Categories', options=readmissions_categories, default=readmissions_categories, key='readmissions_category')
filtered_df_2 = filtered_df_2[filtered_df_2['readmissions_category'].isin(readmissions_category_filter)]

# Display the filtered dataframe for Section 2
st.subheader('Filtered Dataframe: Chronic Conditions and Readmissions')
st.dataframe(filtered_df_2)

