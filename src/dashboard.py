import streamlit as st
import pandas as pd
import plotly.express as px

CORES = {
    "endividamento": "#00BFFF",
    "selic": "#FF4B4B",
    "inad_pf": "#FFA500",
    "inad_total": "#2ECC71"
}

# Carrega dataset analítico
df = pd.read_parquet("data/analytics/endividamento_10anos.parquet")

st.set_page_config(
    page_title="Endividamento das Famílias",
    page_icon="📊",
    layout="wide"
)

st.markdown(
"""
<div style="background-color:#111827;padding:25px;border-radius:10px">
<h1 style="text-align:center;color:white;">Endividamento das Famílias no Brasil</h1>
<p style="text-align:center;color:lightgray;font-size:18px">
Análise dos principais indicadores econômicos brasileiros nos últimos 10 anos
</p>
</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

st.markdown(
"""
### Sobre o projeto

O objetivo deste projeto é analisar a evolução do **endividamento das famílias brasileiras**
nos últimos 10 anos e entender sua relação com outros indicadores econômicos,
como a **taxa Selic** e os níveis de **inadimplência no país**.

Os dados utilizados são provenientes de séries temporais públicas do
**Banco Central** e foram processados em um pipeline de dados que inclui:

- Coleta via API
- Transformação e tratamento dos dados
- Armazenamento em dataset analítico
- Visualização interativa através de dashboard

O dashboard permite explorar tendências, correlações e padrões econômicos
que ajudam a entender o comportamento do crédito e do endividamento no Brasil.
"""
)
st.divider()

# KPIs principais 
st.subheader("📈 Indicadores Atuais da Economia")
ultimo = df.iloc[-1]
selic_anual = ultimo["selic"] * 12

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Endividamento Atual",
    f"{ultimo['endividamento']:.2f}%",
    f"{ultimo['endividamento'] - df['endividamento'].mean():.2f}"
)

col2.metric(
    "Selic Mensal",
    f"{ultimo['selic']:.2f}%"
)

st.caption(f"Selic Anual - Aproximadamente {selic_anual:.2f}% ao ano")

col3.metric(
    "Inadimplência PF",
    f"{ultimo['inadimplencia_pf']:.2f}%",
)

col4.metric(
    "Inadimplência Total",
    f"{ultimo['inadimplencia_total']:.2f}%"
)

st.markdown("---")

# Gráfico de evolução atemporal
st.subheader("Evolução dos Indicadores (últimos 10 anos)")
fig = px.line(
    df,
    x="data",
    y=["endividamento", "selic", "inadimplencia_pf", "inadimplencia_total"],
    labels={"value": "%", "variable": "Indicador"},
    title="Indicadores Econômicos",
)

st.plotly_chart(fig, width="stretch")
st.markdown("---")

# Filtro por período 
st.subheader("Análise por período")
periodo =st.selectbox("Selecione o período:", df["periodo"].unique())
df_filtrado = df[df["periodo"] == periodo]

col_a, col_b = st.columns(2)

with col_a:
    fig2 = px.line(
        df_filtrado,
        x="data",
        y="endividamento",
        title=f"Endividamento - {periodo}",
        color_discrete_sequence=["blue"],
    )
    st.plotly_chart(fig2, width="stretch")

with col_b:
    fig3 = px.line(
        df_filtrado,
        x="data",
        y="selic",
        title=f"Selic - {periodo}",
        color_discrete_sequence=["red"],
    )
    st.plotly_chart(fig3, width="stretch")


st.markdown("---")

# Correlação Selic x Endividamento 
st.subheader("Correlação Selic x Endividamento")
fig4 = px.scatter(
    df,
    x="selic",
    y="endividamento",
    trendline="ols",
    labels={"selic": "Selic (%)", "endividamento": "Endivamento (%)"},
    title="Correlação Selic vs Endividamento",
    color="periodo"
)
st.plotly_chart(fig4, width="stretch")

st.markdown(
"""
<br>

<div style="background-color:#111827;
padding:15px;
border-radius:8px;
text-align:center;
color:#9CA3AF;
font-size:14px;">

Projeto desenvolvido por <b>Dhayane Rocha</b> como estudo prático de 
<b>Engenharia de Dados</b>.<br>

Pipeline de dados: API Banco Central → Processamento em Python → Dataset Parquet → Dashboard Streamlit.<br>

2026
</div>
""",
unsafe_allow_html=True
)