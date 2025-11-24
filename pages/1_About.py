import streamlit as st

st.set_page_config(
    page_title="About - ROI Optimization in Paid Campaigns",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
/* Body gradient background */
.main {
    background: linear-gradient(135deg, #d1e7ff 0%, #f0f8ff 100%);
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

/* Card container */
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

/* Headings inside cards */
.card h2 {
    color: #2c3e50;
    font-size: 1.8em;
    font-weight: 600;
    margin-bottom: 20px;
    position: relative;
    padding-left: 15px;
}

.card h2:before {
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

/* Paragraphs */
.card p {
    font-size: 16px;
    line-height: 1.7;
    color: #444;
    margin-bottom: 15px;
}

/* Highlighted sections */
.highlight {
    background-color: #f8f9fa;
    padding: 25px;
    border-left: 5px solid #4B8BBE;
    margin: 20px 0;
    border-radius: 15px;
    position: relative;
    transition: all 0.3s ease;
}

.highlight:hover {
    background-color: #e9f7ff;
    transform: translateX(5px);
}

/* Objectives */
.objective {
    background-color: #f8f9fa;
    padding: 25px;
    border-left: 5px solid #28a745;
    border-radius: 15px;
    margin: 20px 0;
    position: relative;
    transition: all 0.3s ease;
}

.objective:hover {
    background-color: #e8f5e9;
    transform: translateX(5px);
}

/* Icon for sections */
.section-icon {
    position: absolute;
    top: -15px;
    right: -15px;
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #4B8BBE, #28a745);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    z-index: 1;
}

/* Objective number */
.objective-number {
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

/* Strong text styling */
strong {
    color: #2c3e50;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>About ROI Optimization in Paid Campaigns</h1>", unsafe_allow_html=True)

# Animated progress bar
st.markdown("""
<div class="progress-container">
    <div class="progress-bar"></div>
</div>
""", unsafe_allow_html=True)

# Introduction card
st.markdown("""
<div class="card">
    <h2>Introduction</h2>
    <div class="highlight">
        <p>In today's digital landscape, businesses spend heavily on online ads, yet many campaigns fail to generate a good ROI. Low ROI often results from poor targeting, weak creatives, irrelevant messaging, or ineffective landing pages. This reduces profitability even as companies continue spending on ads, making ROI optimization essential.</p>
    </div>
    <div class="highlight">
        <p>This project uses data analytics and machine learning to study historical ad performance, analyze impressions, clicks, conversions, spend, and revenue, and identify factors that influence ROI. Predictive models estimate future conversions and ROI, helping marketers plan campaigns with less financial risk.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Problem Statement card
st.markdown("""
<div class="card">
    <h2>Problem Statement</h2>
    <div class="highlight">
        <p>Digital paid campaigns often fail to generate expected ROI due to wrong targeting, weak creatives, and poor landing pages. Businesses may invest heavily in ads but end up earning less revenue than spent, leading to financial losses.</p>
    </div>
    <div class="highlight">
        <p>This project analyzes marketing campaign data to identify the reasons behind low ROI and provides structured, data-driven insights for better decision-making.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Objectives card
st.markdown("""
<div class="card">
    <h2>Objectives</h2>
    <div class="objective">
        <div class="objective-number">1</div>
        <p><strong>Analyze campaign data and identify causes of low ROI:</strong><br>
        Study marketing metrics such as impressions, clicks, CTR, conversions, spend, and revenue to detect weak areas. Use visualizations and statistical methods to provide actionable insights.</p>
    </div>
    <div class="objective">
        <div class="objective-number">2</div>
        <p><strong>Develop a machine learning model for predicting campaign performance:</strong><br>
        Build predictive models using features like total spend, impressions, clicks, revenue, and conversions to estimate outcomes before further investment.</p>
    </div>
    <div class="objective">
        <div class="objective-number">3</div>
        <p><strong>Create a recommendation system for optimizing future advertising decisions:</strong><br>
        Suggest optimal channels, budget levels, and strategies based on past campaign performance and model predictions.</p>
    </div>
    <div class="objective">
        <div class="objective-number">4</div>
        <p><strong>Provide a unified data-driven framework for marketing efficiency:</strong><br>
        Combine analysis, prediction, and recommendations into a structured system that simplifies decision-making and improves ROI.</p>
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