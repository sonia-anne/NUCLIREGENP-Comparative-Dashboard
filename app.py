import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración general
st.set_page_config(page_title="NUCLIREGEN-P | Ultra Comparative Dashboard", layout="wide", page_icon="🧬")

# Estilo modo oscuro
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0d1117;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .stDataFrame div {
            color: white !important;
            background-color: #1e1e1e;
            font-size: 16px;
        }
        .stDataFrame th {
            background-color: #111827;
            font-size: 18px;
            color: #00ffff !important;
        }
        h1, h2, h3, h4, h5 {
            color: #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🧬 NUCLIREGEN-P: Ultra Comparative Analytics Dashboard")
st.markdown("#### 📌 Scientific Comparative Metrics of Advanced Therapies")

# Datos comparativos
df = pd.DataFrame({
    "Metric": [
        "Efficacy (%)", "Safety (1-10)", "Cost (USD)", "Reversibility (1-10)",
        "Toxicity (%)", "Permanence (1-10)", "Molecular Specificity (%)",
        "Nuclear Restoration (%)", "Latency for Action (min)", "Off-Target Risk (%)"
    ],
    "NEUCLIREGEN-P": [78, 9.5, 8000, 9.2, 0, 7.8, 99.7, 85, 15, 0.002],
    "Lonafarnib": [28, 6.2, 100000, 3.0, 5.2, 4.0, 43, 10, 120, 3.8],
    "CRISPR": [45, 5.1, 500000, 2.1, 12.4, 10.0, 70, 35, 90, 12.0],
    "Progerinina": [22, 4.0, 60000, 6.0, 8.7, 3.5, 51, 12, 75, 6.1]
})

# Gráfico de burbujas
st.markdown("### 🌐 Multi-Metric Bubble Chart View")
df_transposed = df.set_index("Metric").T.reset_index().rename(columns={"index": "Therapy"})
bubble_df = df_transposed.melt(id_vars=["Therapy"], var_name="Metric", value_name="Score")

fig = px.scatter(
    bubble_df,
    x="Metric",
    y="Therapy",
    size="Score",
    color="Therapy",
    size_max=55,
    color_discrete_sequence=px.colors.qualitative.Safe,
    template="plotly_dark",
    title="🧠 Comparative Bubble View: NEUCLIREGEN-P vs. Other Therapies"
)
fig.update_layout(
    height=700,
    xaxis_tickangle=-45,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white", size=14)
)
st.plotly_chart(fig, use_container_width=True)

# Tabla comparativa
st.markdown("### 📊 Enhanced Scientific Comparative Table")

st.dataframe(df.style
    .highlight_max(axis=1, color='darkcyan')
    .format("{:.2f}")
    .set_properties(**{
        'text-align': 'center',
        'font-size': '16px'
    }),
    use_container_width=True,
    height=600
)
