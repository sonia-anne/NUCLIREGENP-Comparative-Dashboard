import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Config general
st.set_page_config(page_title="NUCLIREGEN-P | Advanced Dashboard", layout="wide", page_icon="🧬")

# Dark theme custom style
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0d1117;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding: 2rem;
        }
        h1, h2, h3, h4, h5 {
            color: #00ffff;
        }
        .stDataFrame th {
            background-color: #111827;
            color: #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧬 NUCLIREGEN-P: Triple-Enhanced Comparative Analysis")

# Data
df = pd.DataFrame({
    "Metric": [
        "Efficacy (%)", "Safety (1-10)", "Cost (USD)", "Reversibility (1-10)",
        "Toxicity (%)", "Permanence (1-10)", "Specificity (%)", "Nuclear Repair (%)", 
        "Activation Time (min)", "Off-Target (%)"
    ],
    "NEUCLIREGEN-P": [78, 9.5, 8000, 9.2, 0, 7.8, 99.7, 85, 15, 0.002],
    "Lonafarnib": [28, 6.2, 100000, 3.0, 5.2, 4.0, 43, 10, 120, 3.8],
    "CRISPR": [45, 5.1, 500000, 2.1, 12.4, 10.0, 70, 35, 90, 12.0],
    "Progerinina": [22, 4.0, 60000, 6.0, 8.7, 3.5, 51, 12, 75, 6.1]
})

# Advanced bar heatmap
st.subheader("🌡️ Dynamic Metric Heatmap")

heatmap_df = df.set_index("Metric")
fig_heatmap = px.imshow(
    heatmap_df,
    color_continuous_scale="Viridis",
    text_auto=True,
    aspect="auto",
    labels=dict(x="Therapy", y="Metric", color="Score")
)
fig_heatmap.update_layout(
    height=700,
    font=dict(color="white", size=14),
    paper_bgcolor='#0d1117',
    plot_bgcolor='#0d1117',
    margin=dict(l=20, r=20, t=40, b=20)
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# Radar chart
st.subheader("🕸️ Multi-Axis Radar Visualization")
radar_data = df.set_index("Metric").T.reset_index().rename(columns={"index": "Therapy"})
metrics = df["Metric"].tolist()

radar_fig = go.Figure()
for _, row in radar_data.iterrows():
    radar_fig.add_trace(go.Scatterpolar(
        r=row[1:].tolist(),
        theta=metrics,
        fill='toself',
        name=row["Therapy"]
    ))

radar_fig.update_layout(
    polar=dict(
        bgcolor='rgba(0,0,0,0)',
        radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='white')),
        angularaxis=dict(tickfont=dict(color='white'))
    ),
    showlegend=True,
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    title="NUCLIREGEN-P vs Other Therapies"
)
st.plotly_chart(radar_fig, use_container_width=True)

# Enhanced static table without Styler (to avoid matplotlib requirement)
st.subheader("📊 Scientific Comparative Table")
st.dataframe(df, use_container_width=True, height=600)

# Footer
st.markdown("""
    <hr style='border: 1px solid #00ffff;'>
    <p style='text-align: center; color: #888;'>Powered by NUCLIREGEN-P Comparative AI Model | Visualization for Scientific Evaluation</p>
""", unsafe_allow_html=True)
