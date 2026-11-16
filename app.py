import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Mundo das Bicicletas",
    page_icon="🚴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CORES E ESTILO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background: #f1f5fc;
    color: #09265c;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06265e, #00183e);
    border-right: 1px solid #183e79;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.brand {
    text-align: center;
    padding: 18px 5px 28px;
    border-bottom: 1px solid #244579;
    margin-bottom: 22px;
}

.brand .bike { font-size: 52px; }
.brand h2 {
    color: white;
    font-size: 23px;
    line-height: 1.05;
    margin: 5px 0;
    font-weight: 800;
}
.brand p {
    color: #b9d3ff;
    font-size: 11px;
    margin: 0;
}

.topbar {
    background: #06265e;
    color: white;
    padding: 15px 22px;
    border-radius: 13px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.hero {
    background: linear-gradient(105deg, #ffffff 0%, #e1edff 55%, #8dbbff 100%);
    border: 1px solid #d5e2f6;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 18px;
    min-height: 115px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.hero h1 {
    color: #082b68;
    font-size: 27px;
    margin: 0;
    font-weight: 800;
}
.hero p { color: #31517f; margin: 5px 0 0; }
.hero .bike-art { font-size: 62px; }

.metric {
    background: white;
    border: 1px solid #dce6f5;
    border-radius: 15px;
    padding: 19px;
    box-shadow: 0 3px 12px #173c7110;
    min-height: 120px;
}
.metric-icon {
    font-size: 28px;
    margin-bottom: 5px;
}
.metric-value {
    color: #082b68;
    font-size: 27px;
    font-weight: 800;
}
.metric-label {
    color: #405575;
    font-size: 13px;
}
.metric-change {
    color: #13a64a;
    font-size: 12px;
    font-weight: 700;
    margin-top: 5px;
}

.panel {
    background: white;
    border: 1px solid #dce6f5;
    border-radius: 15px;
    padding: 17px;
    box-shadow: 0 3px 12px #173c710a;
    margin-bottom: 15px;
}
.panel-title {
    color: #092b68;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 12px;
}

.status {
    background: #e1f8e9;
    color: #11813a;
    padding: 8px 13px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}

.alert-line {
    padding: 9px 0;
    border-bottom: 1px solid #edf1f7;
    color: #233d63;
    font-size: 13px;
}
.alert-line:last-child { border: 0; }

div[data-testid="stMetric"] {
    background: white;
    padding: 12px;
    border-radius: 12px;
}

.stButton button {
    background: #0875f5;
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}
.stButton button:hover {
    background: #075fc6;
    color: white;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# MENU LATERAL
with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="bike">🚴</div>
        <h2>MUNDO DAS<br>BICICLETAS</h2>
        <p>Pedalando sempre mais!</p>
    </div>
    """, unsafe_allow_html=True)

    pagina = st.radio(
        "NAVEGAÇÃO",
        [
            "🏠  Dashboard",
            "📦  Produtos",
            "🏬  Estoque",
            "🛒  Vendas",
            "📥  Entradas",
            "📊  Relatórios",
            "⚙️  Configurações",
            "ℹ️  Sobre"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style="background:#0b397b;padding:16px;border-radius:13px;text-align:center;">
        <div style="font-size:28px;">🚲</div>
        <b>Qualidade e confiança</b>
        <p style="font-size:12px;color:#c7dcff;">
        Tudo para sua próxima pedalada!
        </p>
    </div>
    """, unsafe_allow_html=True)

# CABEÇALHO
st.markdown("""
<div class="topbar">
    <div><b>🔎 &nbsp; Mundo das Bicicletas</b></div>
    <div>🟢 Sistema Online &nbsp; | &nbsp; 👤 Administrador</div>
</div>
""", unsafe_allow_html=True)

# DASHBOARD
if "Dashboard" in pagina:
    st.markdown("""
    <div class="hero">
        <div>
            <h1>👋 Bem-vindo, Administrador!</h1>
            <p>Aqui está um resumo da sua loja hoje.</p>
        </div>
        <div class="bike-art">🚴‍♂️</div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("DADOS ILUSTRATIVOS — DEMONSTRAÇÃO")

    cards = [
        ("🚲", "124", "Produtos no Estoque", "↑ 5%"),
        ("🛒", "32", "Vendas Hoje", "↑ 12%"),
        ("💰", "R$ 4.850,75", "Faturamento Hoje", "↑ 18%"),
        ("⚠️", "2", "Produtos em Estoque Baixo", "Verificar")
    ]

    cols = st.columns(4)
    for col, card in zip(cols, cards):
        with col:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-icon">{card[0]}</div>
                <div class="metric-value">{card[1]}</div>
                <div class="metric-label">{card[2]}</div>
                <div class="metric-change">{card[3]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([1.5, 1])

    with left:
        st.markdown('<div class="panel"><div class="panel-title">📊 Vendas dos Últimos 7 Dias</div>', unsafe_allow_html=True)

        dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        valores = [1100, 2300, 1600, 2900, 2200, 3700, 4100]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dias,
            y=valores,
            mode="lines+markers",
            line=dict(color="#16ad4b", width=4),
            marker=dict(size=9, color="#0875f5"),
            fill="tozeroy",
            fillcolor="rgba(22,173,75,0.12)"
        ))
        fig.update_layout(
            height=270,
            margin=dict(l=5, r=5, t=10, b=5),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#173768"),
            yaxis=dict(title="Vendas (R$)", gridcolor="#e9eef7"),
            xaxis=dict(showgrid=False),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel"><div class="panel-title">📦 Estoque por Categoria</div>', unsafe_allow_html=True)

        fig2 = go.Figure(data=[go.Pie(
            labels=["Bicicletas", "Peças", "Acessórios", "Outros"],
            values=[35, 45, 15, 5],
            hole=.62,
            marker=dict(colors=["#0875f5", "#19bd58", "#174b99", "#77b8ff"]),
            textinfo="percent",
            hoverinfo="label+percent"
        )])
        fig2.update_layout(
            height=270,
            margin=dict(l=0, r=0, t=5, b=5),
            paper_bgcolor="white",
            showlegend=True,
            legend=dict(orientation="h", y=-0.12)
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    a, b = st.columns(2)

    with a:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">🔔 Alertas Importantes</div>
            <div class="alert-line">⚠️ 2 produtos estão com estoque baixo.</div>
            <div class="alert-line">📥 Última entrada de produtos: hoje às 10:15.</div>
            <div class="alert-line">🟢 Sistema funcionando normalmente.</div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">⚡ Atividades Recentes</div>
            <div class="alert-line">🛒 Venda realizada — Bicicleta Aro 29</div>
            <div class="alert-line">📦 Entrada de estoque — Capacete</div>
            <div class="alert-line">👤 Novo cliente cadastrado</div>
        </div>
        """, unsafe_allow_html=True)

# OUTRAS TELAS — PRIMEIRA VERSÃO VISUAL
else:
    nomes = {
        "Produtos": "📦 Produtos",
        "Estoque": "🏬 Controle de Estoque",
        "Vendas": "🛒 Vendas",
        "Entradas": "📥 Entradas de Produtos",
        "Relatórios": "📊 Relatórios",
        "Configurações": "⚙️ Configurações",
        "Sobre": "ℹ️ Sobre o Sistema"
    }

    chave = pagina.split("  ")[-1].strip()
    st.markdown(f"""
    <div class="hero">
        <div>
            <h1>{nomes.get(chave, chave)}</h1>
            <p>Área do sistema Mundo das Bicicletas.</p>
        </div>
        <div class="bike-art">🚴</div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Esta área será implementada na próxima etapa. O painel inicial é uma demonstração visual.")
    if st.button("Voltar ao Dashboard"):
        st.rerun()

st.markdown("""
<div style="text-align:center;color:#7185a5;font-size:11px;padding:20px;">
    Mundo das Bicicletas • Sistema de Gestão • Versão demonstrativa
</div>
""", unsafe_allow_html=True)
