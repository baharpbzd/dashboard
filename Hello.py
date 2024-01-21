import streamlit as st
import pandas as pd
import numpy as np
#import bs4 as bs
import re
import matplotlib.pyplot as plt

# Load the MIX.xlsx file
mix_df = pd.read_excel("MIX.xlsx")

# Load the keywords and other necessary data
Normal_ID = pd.read_excel("Normal_ID.xlsx")
Overweight_ID = pd.read_excel("Overweight_ID.xlsx")
Obese_ID = pd.read_excel("Obese_ID.xlsx")

keys1 = pd.read_excel("Final_Keywords_History.xlsx")
keys2 = pd.read_excel("Final_Keywords_Alcohol.xlsx")
keys3 = pd.read_excel("Final_Keywords_Signs.xlsx")
keys4 = pd.read_excel("Final_Keywords_Diet.xlsx")
keys5 = pd.read_excel("Final_Keywords_Exercise.xlsx")
keys6 = pd.read_excel("Final_Keywords_Medication.xlsx")

# Function to calculate scores
def calculate_scores(sample, keys, freq_normal, freq_overweight, freq_obese):
    proc1 = []
    proc2 = []
    for i in range(len(sample)):
        parsed_sample = bs.BeautifulSoup(sample.iloc[i])
        paragraphs = parsed_sample.find_all('p')
        article_text = ""
        for p in paragraphs:
            article_text += p.text
            processed_article = article_text.lower()
            processed_article = re.sub('[^a-zA-Z]', ' ', processed_article)
            processed_article = re.sub(r'\s+', ' ', processed_article)
        proc1 = processed_article
        proc2.append(proc1)
    mystring = ' '.join(map(str, proc2))

    counts = []
    COUNT = []
    for j in range(len(keys)):
        counts = mystring.count(keys.keywords[j])
        COUNT.append(counts)

    freq_normal_ = (freq_normal - np.min(freq_normal)) / (np.max(freq_normal) - np.min(freq_normal))
    freq_overweight_ = (freq_overweight - np.min(freq_overweight)) / (np.max(freq_overweight) - np.min(freq_overweight))
    freq_obese_ = (freq_obese - np.min(freq_obese)) / (np.max(freq_obese) - np.min(freq_obese))
    COUNT_ = (COUNT - np.min(COUNT)) / (np.max(COUNT) - np.min(COUNT))

    return COUNT_, freq_normal_, freq_overweight_, freq_obese_

# Streamlit app header
st.title('Patient Analysis Streamlit App')

# Display the loaded MIX.xlsx DataFrame
st.write('### Data from MIX.xlsx')
st.write(mix_df)

# Select a patient group
selected_group = st.selectbox('Select a patient group:', ['Normal', 'Overweight', 'Obese'])

# Filter data based on the selected group
if selected_group == 'Normal':
    group_data = Normal_ID
    group_keys = keys1
elif selected_group == 'Overweight':
    group_data = Overweight_ID
    group_keys = keys2
else:
    group_data = Obese_ID
    group_keys = keys3

# Calculate scores
COUNT, freq_normal, freq_overweight, freq_obese = calculate_scores(group_data['TEXT'], group_keys, keys1.freq_normal, keys1.freq_overweight, keys1.freq_obese)

# Plotting
st.write('### Visualization of Patient Scores')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(COUNT, freq_normal, label=f'{selected_group} Group')

ax.set_xlabel('Count')
ax.set_ylabel('Difference')
ax.legend()
st.pyplot(fig)

# Display final scores
st.write('### Final Scores')
st.write(f'{selected_group} History score is: {np.trapz(COUNT, dx=5)}')
st.write(f'and the population normalized score is: {np.trapz(freq_normal, dx=5)}')

# Additional analysis or visualizations can be added here
