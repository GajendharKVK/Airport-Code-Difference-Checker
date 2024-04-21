import streamlit as st
import re

def process_input(input_string):
    # Normalize and extract airport codes
    input_string = re.sub(r'[^A-Z]+', ',', input_string.upper())
    return list(filter(None, input_string.split(',')))

def calculate_difference(set_a, set_b):
    # Convert strings to sets of airport codes
    set_a = set(process_input(set_a))
    set_b = set(process_input(set_b))
    # Calculate difference
    difference = sorted(list(set_a - set_b))
    return ','.join(difference)

# Streamlit UI components
st.title("Airport Code Difference Checker")

# Input areas for sets A and B
input_a = st.text_area("Enter Airline Zones in Bunker Database: (A)", height=150)
input_b = st.text_area("Enter Airport Codes in the Rate Sheet: (B)", height=150)

# Button to calculate difference
if st.button("Calculate Difference"):
    if input_a and input_b:  # Check if input is not empty
        result = calculate_difference(input_a, input_b)
        # Display results
        st.text_area("Difference Results: (A-B)", value=result, height=100)
        # Count of airport codes
        st.write(f"Total Codes in A: {len(process_input(input_a))}")
        st.write(f"Total Codes in B: {len(process_input(input_b))}")
        st.write(f"Total Codes in Result: {len(result.split(',')) if result else 0}")
    else:
        st.error("Please enter airport codes in both fields.")

# Display custom quote at the bottom right
st.markdown("<style>.reportview-container .main footer {visibility: hidden;}</style>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        center: 10px;
        bottom: 10px;
        color: grey;
        font-size: medium;  /* Larger font size */
        font-weight: bold;  /* Bold font weight */
        font-style: italic; /* Italic style */
    }
    </style>
    <div class='footer'>Made by Gaj</div>
    """, unsafe_allow_html=True)
