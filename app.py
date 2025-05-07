import streamlit as st

# Header of the app
st.header('Tossing a Coin')

# Slider to select the number of trials
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)

# Button to start the experiment
start_button = st.button('Run')

# Action when the button is clicked
if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')

# Placeholder text for the app, currently under construction
st.write('It is not a functional application yet. Under construction.')

