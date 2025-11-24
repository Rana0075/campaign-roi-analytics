import streamlit as st

st.set_page_config(page_title="Campaign ROI Recommender", layout="wide")

# Enhanced CSS
st.markdown("""
<style>
/* Body gradient background */
.main {
    background: linear-gradient(135deg, #e6f3ff 0%, #e8f5e9 100%);
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
.card-container {
    background-color: white;
    border-radius: 20px;
    padding: 40px;
    margin: 30px auto;
    max-width: 900px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    text-align: center;
    transition: all 0.3s ease;
    border: 1px solid rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
}

.card-container:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

.card-container:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 8px;
    background: linear-gradient(90deg, #4B8BBE, #28a745);
    border-radius: 20px 20px 0 0;
}

/* Image styling */
.card-container img {
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    width: 100%;
    margin: 25px 0;
    transition: all 0.3s ease;
}

.card-container img:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 25px rgba(0,0,0,0.2);
}

/* Card text */
.card-text {
    font-size: 18px;
    line-height: 1.7;
    color: #444;
    margin-bottom: 25px;
    position: relative;
}

/* Welcome badge */
.welcome-badge {
    display: inline-block;
    background: linear-gradient(135deg, #4B8BBE, #28a745);
    color: white;
    font-weight: 600;
    padding: 8px 20px;
    border-radius: 30px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    font-size: 16px;
}

/* Navigation hint */
.nav-hint {
    background-color: #f8f9fa;
    border-left: 5px solid #4B8BBE;
    padding: 15px 20px;
    border-radius: 8px;
    margin-top: 25px;
    display: inline-block;
    text-align: left;
    transition: all 0.3s ease;
}

.nav-hint:hover {
    background-color: #e9f7ff;
    transform: translateX(5px);
}

/* Icon for navigation */
.nav-icon {
    margin-right: 10px;
    color: #4B8BBE;
    font-size: 20px;
    vertical-align: middle;
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
st.markdown("<h1>Campaign ROI Recommender</h1>", unsafe_allow_html=True)

# Animated progress bar
st.markdown("""
<div class="progress-container">
    <div class="progress-bar"></div>
</div>
""", unsafe_allow_html=True)

# Centered card using columns
col1, col2, col3 = st.columns([1, 8, 1])  # side columns to center
with col2:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Welcome badge
    st.markdown('<div class="welcome-badge">Welcome to Your Marketing Assistant</div>', unsafe_allow_html=True)
    
    # Main text
    st.markdown("<p class='card-text'>This powerful tool helps you predict campaign ROI, optimize budget allocation, and make smarter marketing decisions based on data-driven insights.</p>", unsafe_allow_html=True)
    
    # Image with caption
    st.image("C:/Users/DELL/major project/vis.png", use_column_width=True, caption="Campaign Performance Dashboard")
    
    # Navigation hint
    st.markdown("""
    <div class="nav-hint">
        <span class="nav-icon">📋</span>
        <strong>Navigation Tip:</strong> Use the sidebar to explore different sections including prediction, methodology, and about information.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)