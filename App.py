import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página optimizada para la pantalla del iPad (Wide mode)
st.set_page_config(page_title="Earnings Analyst Pro", layout="wide", initial_sidebar_state="expanded")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .metric-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .red-flag { background-color: #ffe6e6; border-left: 5px solid #ff4b4b; padding: 10px; border-radius: 5px; }
    .catalyst { background-color: #e6f4ea; border-left: 5px solid #34a853; padding: 10px; border-radius: 5px; }
    .price-meaning { background-color: #e8f0fe; border-left: 5px solid #1a73e8; padding: 15px; border-radius: 5px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (iPad Sidebar) ---
with st.sidebar:
    st.title("📊 Earnings Analyst")
    ticker = st.text_input("Introduce el Ticker de la Empresa:", value="AAPL").upper()
    quarter = select_quarter = st.selectbox("Trimestre a Analizar:", ["Q1 2026", "Q4 2025", "Q3 2025", "Q2 2025"])
    
    st.markdown("---")
    st.subheader("🌐 Entorno Macroeconómico")
    st.caption("Contexto económico en la fecha del reporte")
    st.metric(label="Tasa de Interés Fed", value="4.75%", delta="-0.25% (Último cambio)")
    st.metric(label="Inflación CPI (YoY)", value="2.8%", delta="-0.1% vs mes anterior")
    st.metric(label="Crecimiento PIB (QoQ)", value="2.1%")

# --- DATOS SIMULADOS (Para demostración) ---
# En una app real, aquí conectarías con APIs como Alpha Vantage, Yahoo Finance o OpenAI para el texto.
data = {
    "revenue_actual": 118.5, "revenue_est": 116.0, "revenue_guidance": 115.0,
    "eps_actual": 2.18, "eps_est": 2.10, "eps_guidance": 2.05,
    "margin_actual": 45.2, "margin_est": 44.5, "margin_guidance": 44.0,
    "market_reaction": "+4.2% (After-hours)",
    "next_rev_guidance": "122.0B - 125.0B", "cagr_projected": "8.5% (Próximos 3 años)"
}

# --- CUERPO PRINCIPAL ---
st.title(f"Resultados Trimestrales: {ticker} ({quarter})")

# Fila 1: Resumen de Mercado y Reacción Directa
col_title, col_react = st.columns([2, 1])
with col_title:
    st.subheader("Métricas Clave: Real vs Estimado vs Guidance Previo")
with col_react:
    st.markdown(f"<div style='text-align: right;'><b>Reacción del Mercado:</b> <span style='color:green; font-size:20px; font-weight:bold;'>{data['market_reaction']}</span></div>", unsafe_allow_html=True)

# Fila 2: Tabla Comparativa (Real vs Esperado vs Guidance)
metrics_df = pd.DataFrame({
    "Métrica": ["Revenue (Ingresos)", "EPS (Ganancia por Acción)", "Margen Bruto (%)"],
    "Guidance Previo": [f"${data['revenue_guidance']}B", f"${data['eps_guidance']}", f"{data['margin_guidance']}%"],
    "Estimado Consenso": [f"${data['revenue_est']}B", f"${data['eps_est']}", f"{data['margin_est']}%"],
    "Resultado Real": [f"${data['revenue_actual']}B", f"${data['eps_actual']}", f"{data['margin_actual']}%"],
    "Resultado vs. Guidance": ["🟢 Superó", "🟢 Superó", "🟢 Superó"]
})
st.table(metrics_df.set_index("Métrica"))

st.markdown("---")

# Fila 3: Gráfico de Proyecciones Futuras y CAGR
st.subheader("📈 Proyecciones Futuras y Tasa de Crecimiento")
col_chart, col_cagr = st.columns([2, 1])

with col_chart:
    # Gráfico de barras simple del crecimiento proyectado de ingresos
    years = ['2024', '2025', '2026 (Est)', '2027 (Est)']
    rev_trend = [385.7, 391.0, 420.0, 455.0]
    fig = go.Figure(data=[go.Bar(x=years, y=rev_trend, marker_color='#1a73e8')])
    fig.update_layout(title="Trayectoria de Ingresos Anuales (Billions $)", height=250, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

with col_cagr:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.metric(label="Tasa de Crecimiento Anual Compuesto (CAGR Proyectado)", value=data['cagr_projected'])
    st.info(f"**Siguiente Trimestre:** Guidance de Ingresos guiado por la empresa: **{data['next_rev_guidance']}**")

st.markdown("---")

# Fila 4: Pestañas de Análisis Cualitativo (Análisis profundo para el Inversor)
st.subheader("🔍 Análisis Cualitativo y Tesis de Inversión")

tab1, tab2, tab3 = st.tabs(["🎙️ Señales del Management", "🚨 Riesgos y Catalizadores", "💰 ¿Qué significa para el precio?"])

with tab1:
    st.markdown("### Comentarios clave en la llamada de ganancias (Earnings Call)")
    st.markdown("""
    * **Sobre la Demanda:** El management señala una resiliencia fuerte en el sector premium, especialmente en mercados emergentes (India creció a doble dígito).
    * **Sobre la Competencia:** Se observa una estabilización de la pérdida de cuota en China debido a agresivas campañas de marketing locales.
    * **Sobre los Costos:** Los costos de la cadena de suministro han bajado un 4%, compensando las inversiones agresivas en Capex para Centros de Datos e Inteligencia Artificial.
    """)

with tab2:
    col_red, col_cat = st.columns(2)
    with col_red:
        st.markdown("#### 🚨 Red Flags (Alertas)")
        st.markdown("""
        <div class='red-flag'>
        <ul>
            <li>El crecimiento de servicios se está desacelerando ligeramente (11% vs 13% esperado).</li>
            <li>Escrutinio regulatorio en Europa podría presionar los márgenes de la App Store en el largo plazo.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_cat:
        st.markdown("#### 🚀 Catalizadores Relevantes")
        st.markdown("""
        <div class='catalyst'>
        <ul>
            <li>Anuncio de un nuevo programa de recompra de acciones por $90B.</li>
            <li>La integración de las nuevas funciones de IA está aumentando el ciclo de renovación de dispositivos hardware más rápido de lo previsto.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("#### 🎯 Conclusión e Impacto en la Valoración")
    st.markdown("""
    <div class='price-meaning'>
    Los resultados demuestran que el negocio principal sigue siendo una máquina de generar efectivo y que el miedo a la desaceleración en China estaba sobrevalorado. 
    Dado que el guidance hacia adelante se mantuvo sólido y superior al consenso, el múltiplo actual (P/E) está justificado. 
    
    <b>Efecto probable en el precio:</b> El reporte actúa como un piso fuerte para la acción. Es probable que veamos revisiones al alza en los precios objetivo de los analistas de Wall Street en los próximos días, manteniendo una tendencia alcista a corto plazo.
    </div>
    """, unsafe_allow_html=True)
