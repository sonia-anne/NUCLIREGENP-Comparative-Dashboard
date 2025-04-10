import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# PAGE CONFIG
st.set_page_config(page_title="NUCLIREGEN-P | Comparative Dashboard", layout="wide", page_icon="🧬")

# STYLING
st.markdown("""
    <style>
        body, .stApp { background-color: #0f111a; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
        h1, h2, h3, h4, h5, h6, p, .stMarkdown {
            color: #ffffff !important;
        }
        .stTabs [role="tab"] {
            background-color: #1c1f2b;
            color: #00ffe1;
            font-size: 18px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #00ffe1;
            color: #000;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 NUCLIREGEN-P: Comparative Intelligence Dashboard")

tab1, tab2 = st.tabs(["📊 Dynamic Table", "🕸️ Radar Insights"])

# COMPARATIVE DATA
data = {
    "Therapy": ["NEUCLIREGEN-P", "Lonafarnib", "CRISPR", "Progerinina"],
    "Efficacy (%)": [78, 28, 45, 22],
    "Safety Score (1-10)": [9.5, 6.2, 5.1, 4.0],
    "Cost (USD)": [8000, 100000, 500000, 60000],
    "Reversibility (1-10)": [9.2, 3.0, 2.1, 6.0],
    "Toxicity (%)": [0, 5.2, 12.4, 8.7],
    "Permanence (1-10)": [7.8, 4.0, 10.0, 3.5]
}
df = pd.DataFrame(data)

with tab1:
    st.subheader("📊 Interactive Performance Table: Therapy Comparison")
    st.dataframe(df.style
        .background_gradient(cmap="viridis", subset=df.columns[1:])
        .format(precision=1)
        .set_properties(**{
            'text-align': 'center',
            'border': '1px solid white',
            'padding': '12px'
        }), 
        use_container_width=True, height=500
    )

with tab2:
    st.subheader("🕸️ Radar Chart: Multi-Axis Visual Analysis")
    radar_df = pd.DataFrame({
        "Metric": ["Efficacy", "Safety", "Reversibility", "Toxicity", "Permanence", "Cost Efficiency"],
        "NEUCLIREGEN-P": [78, 95, 92, 100, 78, 91],
        "Lonafarnib": [28, 62, 30, 48, 40, 25],
        "CRISPR": [45, 51, 21, 38, 100, 12],
        "Progerinina": [22, 40, 60, 13, 35, 30]
    })

    fig = go.Figure()
    for therapy in radar_df.columns[1:]:
        fig.add_trace(go.Scatterpolar(
            r=radar_df[therapy],
            theta=radar_df["Metric"],
            fill='toself',
            name=therapy
        ))

    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='white')),
            angularaxis=dict(tickfont=dict(color='white'))
        ),
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        title="Radar Chart: NUCLIREGEN-P vs. Other Therapies"
    )
    st.plotly_chart(fig, use_container_width=True)
