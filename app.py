import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="NUCLIREGEN-P | Comparative Dashboard", layout="wide", page_icon="🧬")

st.markdown("""
    <style>
        body, .stApp { background-color: #0e1117; color: #ffffff; }
        h1, h2, h3, h4, h5, h6, p, .stMarkdown {
            color: #ffffff !important;
        }
        .stTabs [role="tab"] {
            background-color: #1e2127;
            color: #00ffff;
        }
        .stTabs [aria-selected="true"] {
            background-color: #00ffff;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 NUCLIREGEN-P: Ultra-Advanced Comparative Analytics")

tab1, tab2 = st.tabs(["📊 Comparative Table", "🕸️ Radar Chart"])

# Tabla comparativa
with tab1:
    st.subheader("📊 Advanced Comparative Table: NEUROREGEN-P vs. Other Therapies")

    df = pd.DataFrame({
        "Therapy": ["NEUROREGEN-P", "Lonafarnib", "CRISPR", "Progerinina"],
        "Efficacy (%)": [78, 28, 45, 22],
        "Safety Score (1-10)": [9.5, 6.2, 5.1, 4.0],
        "Cost (USD)": [8000, 100000, 500000, 60000],
        "Reversibility (1-10)": [9.2, 3.0, 2.1, 6.0],
        "Toxicity (%)": [0, 5.2, 12.4, 8.7],
        "Permanence (1-10)": [7.8, 4.0, 10.0, 3.5]
    })

    fig_table = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='cyan',
                    font=dict(color='black', size=14),
                    align='center'),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color='darkslategray',
                   font=dict(color='white', size=12),
                   align='center'))
    ])

    fig_table.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_table, use_container_width=True)

# Gráfico de radar
with tab2:
    st.subheader("🕸️ Radar Chart: Multi-Criteria Comparison")

    radar_df = pd.DataFrame({
        "Metric": ["Efficacy", "Safety", "Reversibility", "Toxicity", "Permanence", "Cost Efficiency"],
        "NEUROREGEN-P": [78, 95, 92, 100, 78, 91],
        "Lonafarnib": [28, 62, 30, 48, 40, 25],
        "CRISPR": [45, 51, 21, 38, 100, 12],
        "Progerinina": [22, 40, 60, 13, 35, 30]
    })

    fig_radar = go.Figure()

    therapies = radar_df.columns[1:]
    for therapy in therapies:
        fig_radar.add_trace(go.Scatterpolar(
            r=radar_df[therapy],
            theta=radar_df["Metric"],
            fill='toself',
            name=therapy
        ))

    fig_radar.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='white')),
            angularaxis=dict(tickfont=dict(color='white'))
        ),
        template="plotly_dark",
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        title="Radar Chart: NUCLIREGEN-P vs. Other Therapies"
    )

    st.plotly_chart(fig_radar, use_container_width=True)
