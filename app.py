import streamlit as st
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("✈️ Flight Delay Prediction")

st.write("Enter flight details:")

# USER INPUTS (REALISTIC)
origin = st.selectbox("Origin", ["Delhi", "Mumbai", "Chennai", "Kolkata"])
destination = st.selectbox("Destination", ["Delhi", "Mumbai", "Chennai", "Kolkata"])
airline = st.selectbox("Airline", ["Indigo", "Air India", "SpiceJet"])
month = st.selectbox("Month", list(range(1, 13)))

# 🔥 CONVERT TO NUMBERS (VERY IMPORTANT)
origin_map = {"Delhi": 1, "Mumbai": 2, "Chennai": 3, "Kolkata": 4}
airline_map = {"Indigo": 1, "Air India": 2, "SpiceJet": 3}

origin_val = origin_map[origin]
dest_val = origin_map[destination]
airline_val = airline_map[airline]
month_val = month

# PREDICT
if st.button("Predict"):
    input_data = [[origin_val, dest_val, airline_val, month_val]]
    
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("❌ Flight Delayed")
    else:
        st.success("✅ Flight On Time")