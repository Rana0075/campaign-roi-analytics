import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Predict - Campaign ROI Recommender", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
/* Main container */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #e6f3ff, #ffffff) !important;
    font-family: 'Arial', sans-serif;
    color: #333;
}

/* Page title */
h1 {
    color: #4B8BBE;
    text-align: center;
    font-size: 3em;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 30px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* Card styling */
.card {
    background-color: white;
    border-radius: 20px;
    padding: 30px;
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    transition: transform 0.2s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.2);
}

/* Inputs */
input, select {
    border: 2px solid #4B8BBE;
    border-radius: 8px;
    padding: 8px;
    font-size: 16px;
    margin-bottom: 15px;
    width: 100%;
}

/* Button */
div.stButton > button {
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 10px;
}
div.stButton > button:hover {
    background-color: #218838;
}

/* Table */
.stTable {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Warning card */
.warning-card {
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeaa7;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Load trained pipeline ---
data = joblib.load("C:\\Users\\DELL\\major project\\pipeline.pkl")
pipeline = data["pipeline"]
meta = data["metadata"]

goals = meta["goals"]
channels = meta["channels"]
durations = meta["durations"]
age_ranges = meta["age_ranges"]
min_budget = meta["min_budget"]
max_budget = meta["max_budget"]

# Recommendation function
def recommend_campaign_vectorized(budget, goal, model=pipeline):
    if budget < min_budget:
        return f"Budget too low. Minimum recommended budget is {min_budget}."
    
    all_combinations = pd.DataFrame(
        [(goal, dur, ch, age, budget)
         for ch in channels
         for dur in durations
         for age in age_ranges],
        columns=["Campaign_Goal", "Duration(days)", "Channel_Used", "Age_Range", "Total_spend"]
    )
    
    all_combinations["Predicted_ROI"] = model.predict(all_combinations)
    best = all_combinations.loc[all_combinations["Predicted_ROI"].idxmax()]
    return best

# --- UI ---
st.markdown("<h1>Campaign ROI Recommender</h1>", unsafe_allow_html=True)

# Initialize session state variables
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'result' not in st.session_state:
    st.session_state.result = None

# Create columns for centering
col1, col2, col3 = st.columns([1, 6, 1])

# Input Card
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Enter Campaign Details")
    
    goal = st.selectbox("Select Campaign Goal", goals)
    
    budget = st.number_input(
        "Enter Budget ($)",
        min_value=min_budget,
        max_value=max_budget,
        value=min_budget,
        step=100
    )
    
    if st.button("Recommend Campaign"):
        st.session_state.result = recommend_campaign_vectorized(budget, goal)
        st.session_state.show_result = True
    
    st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.show_result:
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Recommended Campaign")
        
        if isinstance(st.session_state.result, str):
            st.markdown(f'<div class="warning-card">{st.session_state.result}</div>', unsafe_allow_html=True)
        else:
            st.table(st.session_state.result.to_frame().T)
        
        st.markdown('</div>', unsafe_allow_html=True)