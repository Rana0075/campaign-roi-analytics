import streamlit as st

st.set_page_config(
    page_title="Model Info - Campaign ROI Recommender",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
/* Body gradient background */
.main {
    background: linear-gradient(135deg, #e6f3ff 0%, #ffffff 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
}

/* Page title */
h1 {
    color: #2c3e50;
    text-align: center;
    font-size: 3.2em;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 40px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    position: relative;
    display: inline-block;
    width: 100%;
}

h1:after {
    content: "";
    display: block;
    width: 150px;
    height: 4px;
    background: linear-gradient(90deg, #4B8BBE, #28a745);
    margin: 15px auto 0;
    border-radius: 2px;
}

/* Subheaders */
h2 {
    color: #2c3e50;
    margin-bottom: 15px;
    font-size: 1.8em;
    font-weight: 600;
    position: relative;
    padding-left: 15px;
}

h2:before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 5px;
    height: 25px;
    background: #4B8BBE;
    border-radius: 3px;
}

/* Card container for steps */
.card {
    background-color: white;
    border-radius: 20px;
    padding: 30px;
    margin: 25px auto;
    max-width: 900px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border: 1px solid rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

.card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 8px;
    height: 100%;
    background: linear-gradient(to bottom, #4B8BBE, #28a745);
    border-radius: 4px 0 0 4px;
}

/* Individual method step */
.method-step {
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 15px;
    margin: 20px 0;
    position: relative;
    transition: all 0.3s ease;
    border-left: 5px solid #4B8BBE;
}

.method-step:hover {
    background-color: #e9f7ff;
    transform: translateX(5px);
}

/* Alternating step colors */
.method-step:nth-child(odd) {
    background-color: #e9f7ff;
    border-left-color: #4B8BBE;
}

.method-step:nth-child(even) {
    background-color: #e8f5e9;
    border-left-color: #28a745;
}

/* Paragraphs inside steps */
.method-step p {
    font-size: 16px;
    line-height: 1.7;
    color: #444;
    margin: 0;
}

/* Step number indicator */
.step-number {
    position: absolute;
    top: -15px;
    left: -15px;
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, #4B8BBE, #28a745);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    z-index: 1;
}

/* Introduction card special styling */
.intro-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9f7ff 100%);
    border-left: none;
}

.intro-card:before {
    width: 100%;
    height: 8px;
    top: 0;
    left: 0;
    border-radius: 20px 20px 0 0;
    background: linear-gradient(90deg, #4B8BBE, #28a745);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 16px;
    color: #555;
    margin-top: 50px;
    padding: 20px;
    background: rgba(255,255,255,0.7);
    border-radius: 15px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

/* Team name highlight */
.team-name {
    font-weight: 700;
    color: #4B8BBE;
    font-size: 18px;
}

/* Animated progress bar */
.progress-container {
    width: 100%;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    margin: 30px auto;
    max-width: 800px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #4B8BBE, #28a745);
    border-radius: 4px;
    width: 100%;
    animation: progress 2s ease-in-out;
}

@keyframes progress {
    0% { width: 0; }
    100% { width: 100%; }
}
</style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>Project Methodology</h1>", unsafe_allow_html=True)

# Animated progress bar
st.markdown("""
<div class="progress-container">
    <div class="progress-bar"></div>
</div>
""", unsafe_allow_html=True)

# Introduction card
st.markdown("""
<div class="card intro-card">
    <div class="method-step">
        <div class="step-number">0</div>
        <p>In this project, the work was carried out in a structured, step-by-step manner to analyze digital ad campaigns, understand factors affecting ROI, and build a system that predicts performance and provides recommendations.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Steps cards
steps = [
    ("Data Collection", "Public datasets from Kaggle and open sources containing impressions, clicks, conversions, spend, CTR, revenue, and ROI were collected to simulate real campaign scenarios."),
    ("Data Preparation and Cleaning", "Data cleaning was done using Pandas and NumPy. Missing values, inconsistent entries, and unnecessary columns were handled to make the dataset ready for EDA and ML."),
    ("Exploratory Data Analysis (EDA)", "Visualizations and correlation analysis were performed to understand campaign performance and identify factors that most influence ROI."),
    ("Machine Learning Model Development", "Random Forest Regressor was trained to predict conversions/ROI using features like impressions, clicks, spend, CTR, revenue, and campaign duration. Model evaluation used MSE, RMSE, MAE, and R²."),
    ("Recommendation System Creation", "A system was built to suggest budget allocations, improvements, and optimizations based on EDA and ML predictions, guiding smarter decisions."),
    ("Visualization & Reporting", "All results, model outputs, and recommendations were summarized in dashboards and plots to present actionable insights in a clear format.")
]

for i, (title, desc) in enumerate(steps):
    st.markdown(f"""
    <div class="card">
        <h2>{title}</h2>
        <div class="method-step">
            <div class="step-number">{i+1}</div>
            <p>{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    <p>Developed by <span class="team-name">Team: 25O4034 - WhileLoop</span></p>
    <p>ROI Optimization in Paid Campaigns</p>
</div>
""", unsafe_allow_html=True)
