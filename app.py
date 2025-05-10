"""
app.py

Dashboard Interativo com Streamlit
Objetivo: explorar vendas por categoria, evolução temporal e clusters de forma interativa.
"""

# ──────────────────────────────────────────────────────────────────────────────
# 1) Imports e Configurações Iniciais
# ──────────────────────────────────────────────────────────────────────────────

import streamlit as st
import pandas as pd
import plotly.express as px

# Cache para acelerar recarregamento
@st.cache_data
def load_data():
    return pd.read_csv(
        "data/ecommerce_clean.csv",
        parse_dates=["order_purchase_timestamp"]
    )

df = load_data()

# ──────────────────────────────────────────────────────────────────────────────
# 2) Título e Descrição
# ──────────────────────────────────────────────────────────────────────────────

st.title("📊 Dashboard de Varejo Online")
st.write(
    """
    Use o painel lateral para filtrar categorias e veja KPIs, gráficos de
    receita mensal e clusters de categorias.
    """
)

# ──────────────────────────────────────────────────────────────────────────────
# 3) Filtros na Sidebar
# ──────────────────────────────────────────────────────────────────────────────

# Remove NaN e obtém lista única de categorias
categorias = df["product_category_name"].dropna().unique().tolist()
categorias.sort()  # ou: categorias = sorted(categorias)

selecionada = st.sidebar.multiselect(
    "Escolha categorias",
    options=categorias,
    default=categorias[:5]  # ou outro slice de sua preferência
)

# Aplica filtro no DataFrame
df_filt = df[df["product_category_name"].isin(selecionada)]


# ──────────────────────────────────────────────────────────────────────────────
# 4) KPIs Principais
# ──────────────────────────────────────────────────────────────────────────────

col1, col2, col3 = st.columns(3)
col1.metric("Total de Pedidos", df_filt["order_id"].nunique())
col2.metric("Ticket Médio (R$)", f"{df_filt['total_price'].mean():.2f}")
col3.metric("Avaliação Média", f"{df_filt['review_score'].mean():.2f}")

# ──────────────────────────────────────────────────────────────────────────────
# 5) Receita Mensal
# ──────────────────────────────────────────────────────────────────────────────

df_filt["order_month"] = df_filt["order_purchase_timestamp"] \
                            .dt.to_period("M") \
                            .dt.to_timestamp()

monthly = (
    df_filt.groupby("order_month")
           .agg(receita=("total_price", "sum"))
           .reset_index()
)

fig = px.line(
    monthly,
    x="order_month",
    y="receita",
    title="Receita Mensal de Vendas",
    labels={"order_month":"Mês", "receita":"Receita (R$)"}
)
st.plotly_chart(fig, use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────────
# 6) Clusters de Categorias
# ──────────────────────────────────────────────────────────────────────────────

# Carrega clusters (supondo que você tenha gerado e salvo em CSV antes)
clusters = pd.read_csv("data/category_clusters.csv")

# Agrega métricas para o scatter
agg = (
    df_filt.groupby("product_category_name")
          .agg(
              ticket_medio=("total_price", "mean"),
              pedidos=("order_id", "nunique")
          )
          .reset_index()
          .merge(clusters, on="product_category_name", how="left")
)

fig2 = px.scatter(
    agg,
    x="ticket_medio",
    y="pedidos",
    color="cluster",
    hover_name="product_category_name",
    title="Clusters de Categorias"
)
st.plotly_chart(fig2, use_container_width=True)
