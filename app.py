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
df['predicted_er_visits'] = np.random.uniform(0, 5.5, size=100)  # ER visits ranging from 0 to 5.5
df['predicted_readmissions'] = np.random.uniform(0, 5.5, size=100)  # Readmissions ranging from 0 to 5.5

# Define new criteria for categorizing ER visits
def categorize_er_visits(pred):
    if pred >= 3:
        return 'Frequent flyers'
    elif 0.5 < pred < 3:
        return 'Likely returnees'
    else:
        return 'Unlikely to return'

# Define new criteria for categorizing Readmissions
def categorize_readmissions(pred):
    if pred >= 3:
        return 'Frequent readmissions'
    elif 0.5 < pred < 3:
        return 'Likely returnees'
    else:
        return 'Unlikely to return'

df['er_visits_category'] = df['predicted_er_visits'].apply(categorize_er_visits)
df['readmissions_category'] = df['predicted_readmissions'].apply(categorize_readmissions)

# Streamlit app
st.title('ER and Re-admissions predictions')

st.markdown("""

**Frequent flyers**: Predicted ER visits is 3 or greater.

**Likely returnees**: Predicted ER visits is greater than 0.5 and less than 3.

**Unlikely to return**: Predicted ER visits is 0.5 or less.

**Frequent readmissions**: Predicted readmissions is 3 or greater.

**Likely returnees**: Predicted readmissions is greater than 0.5 and less than 3.

**Unlikely to return**: Predicted readmissions is 0.5 or less.

 """)

# Section 1: Chronic Conditions and ER Visits
st.header('Chronic Conditions and ER Visits')

# Selectors for chronic conditions
chronic_condition_filter_1 = st.multiselect('Select Chronic Conditions', options=chronic_conditions, default=chronic_conditions)
filtered_df_1 = df[df['chronic_condition'].isin(chronic_condition_filter_1)]

# Selectors for ER visit categories
er_visits_categories = ['Frequent flyers', 'Likely returnees', 'Unlikely to return']
er_visits_category_filter = st.multiselect('Select ER Visit Categories', options=er_visits_categories, default=er_visits_categories)
filtered_df_1 = filtered_df_1[filtered_df_1['er_visits_category'].isin(er_visits_category_filter)]

# Display the filtered dataframe for Section 1
st.subheader('Chronic Conditions and ER Visits')
st.dataframe(filtered_df_1)

# Section 2: Chronic Conditions and Readmissions
st.header('Chronic Conditions and Readmissions')

# Selectors for chronic conditions
chronic_condition_filter_2 = st.multiselect('Select Chronic Conditions', options=chronic_conditions, default=chronic_conditions, key='readmissions')
filtered_df_2 = df[df['chronic_condition'].isin(chronic_condition_filter_2)]

# Selectors for readmissions categories
readmissions_categories = ['Frequent readmissions', 'Likely returnees', 'Unlikely to return']
readmissions_category_filter = st.multiselect('Select Readmissions Categories', options=readmissions_categories, default=readmissions_categories, key='readmissions_category')
filtered_df_2 = filtered_df_2[filtered_df_2['readmissions_category'].isin(readmissions_category_filter)]

# Display the filtered dataframe for Section 2
st.subheader('Chronic Conditions and Readmissions')
st.dataframe(filtered_df_2)
