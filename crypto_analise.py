import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuração da página
st.set_page_config(
    page_title="Crypto Analise", 
    page_icon="🪙", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CSS PARA O TEMA ESCURO ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.9)), 
url("https://images.unsplash.com/photo-1609554496796-c345a5331ce1?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(25, 25, 25, 0.75);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    h1, h2, h3, p {
        color: #ffffff !important;
    }
    [data-testid="stMetricLabel"] {
        color: #a0aec0 !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def buscar_dados(coin_id: str, dias: int = 30, moeda_fiat: str = "usd"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": moeda_fiat, "days": dias}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            st.error(f"Erro ao buscar dados de {coin_id}. Verifique o nome da moeda.")
            return None
        data = r.json()
        if "prices" not in data:
            st.error(f"ID da moeda '{coin_id}' inválido.")
            return None
        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        st.error("Erro de conexão. Verifique sua internet.")
        return None

def buscar_preco_atual(moedas: list, moeda_fiat: str = "usd"):
    ids = ",".join(moedas)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ids, "vs_currencies": moeda_fiat}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None

# --- FUNÇÃO PARA DESENHAR O GRÁFICO ---
def plotar_grafico(df, titulo, cor_linha, ax, label_fiat):
    ax.plot(df["timestamp"], df["price"], color=cor_linha, linewidth=2.5)
    ax.fill_between(df["timestamp"], df["price"], df["price"].min() * 0.99, alpha=0.15, color=cor_linha)
    ax.set_title(titulo, fontsize=14, color='white')
    ax.set_ylabel(f"Preço ({label_fiat})", color='lightgray') # Agora o eixo Y muda dependendo da moeda
    ax.tick_params(axis='x', colors='lightgray', rotation=45)
    ax.tick_params(axis='y', colors='lightgray')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('gray')
    ax.spines['left'].set_color('gray')
    ax.set_facecolor('none')

# --- INTERFACE PRINCIPAL ---
def main():
    st.markdown("<h1 style='text-align: center;'>🪙 Crypto Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0aec0; font-size: 18px;'>Acompanhe e compare o mercado em tempo real</p>", unsafe_allow_html=True)
    
    st.info("💡 **Dica de Ouro:** Digite até duas moedas separadas por vírgula para comparar (ex: `bitcoin, ethereum`).")
    st.markdown("<br>", unsafe_allow_html=True)

    # PAINEL DE CONTROLE (Com seleção de moeda) ---
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        entrada = st.text_input("🔎 IDs das moedas:", placeholder="Ex: solana, dogecoin").strip().lower()
    
    with col2:
        # Seletor de moeda base
        escolha_fiat = st.selectbox("Moeda:", ["USD ($)", "BRL (R$)"])
        # Configurando as variáveis baseado na escolha
        moeda_fiat = "usd" if escolha_fiat == "USD ($)" else "brl"
        simbolo = "$" if escolha_fiat == "USD ($)" else "R$"

    with col3:
        modo = st.selectbox("Visualizar:", ["Preço Atual ⚡", "Histórico 📈"])

    if modo == "Histórico 📈":
        dias = st.slider("📅 Quantos dias de histórico?", min_value=1, max_value=365, value=30)
    else:
        dias = 7 

    analisar_btn = st.button("🚀 Analisar Mercado", use_container_width=True, type="primary")
    st.divider()

    # -EXIBIÇÃO ---
    if analisar_btn:
        if not entrada:
            st.warning("⚠️ Por favor, digite ao menos uma moeda.")
            return
            
        moedas = [m.strip() for m in entrada.split(',')]
        
        if len(moedas) > 2:
            st.warning("⚠️ Por favor, digite no máximo 2 moedas para comparação.")
            return

        with st.spinner('Analisando o mercado... ⏳'):
            dados_hist = {}
            for moeda in moedas:
                
                df = buscar_dados(moeda, dias, moeda_fiat)
                if df is not None:
                    dados_hist[moeda] = df
            
            if len(dados_hist) != len(moedas):
                return

            if modo == "Preço Atual ⚡":
                st.subheader(f"💰 Cotação em Tempo Real (Tendência de {dias} dias)")
                
                dados_atuais = buscar_preco_atual(moedas, moeda_fiat)
                
                colunas_metricas = st.columns(len(moedas))
                for i, moeda in enumerate(moedas):
                    df = dados_hist[moeda]
                    preco_inicial = df["price"].iloc[0]
                    preco_final = df["price"].iloc[-1]
                    variacao = ((preco_final - preco_inicial) / preco_inicial) * 100
                    
                    with colunas_metricas[i]:
                        # Buscando o valor correto (usd ou brl) no dicionário retornado
                        preco = dados_atuais[moeda][moeda_fiat] if dados_atuais and moeda in dados_atuais else preco_final
                        st.metric(label=f"{moeda.upper()}", value=f"{simbolo} {preco:,.4f}", delta=f"{variacao:.2f}% na semana")

            elif modo == "Histórico 📈":
                st.subheader(f"📊 Desempenho nos últimos {dias} dias")
                colunas_metricas = st.columns(len(moedas))
                
                for i, moeda in enumerate(moedas):
                    df = dados_hist[moeda]
                    preco_inicial = df["price"].iloc[0]
                    preco_final = df["price"].iloc[-1]
                    variacao = ((preco_final - preco_inicial) / preco_inicial) * 100
                    
                    with colunas_metricas[i]:
                        st.metric(label=f"{moeda.upper()} (Último fechamento)", value=f"{simbolo} {preco_final:,.4f}", delta=f"{variacao:.2f}%")

    # GRÁFICOS ---
            fig_bg_color = 'none' 

            if len(moedas) == 1:
                moeda = moedas[0]
                df = dados_hist[moeda]
                variacao = ((df["price"].iloc[-1] - df["price"].iloc[0]) / df["price"].iloc[0]) * 100
                cor = "#00C805" if variacao >= 0 else "#FF4A4A"
                
                fig, ax = plt.subplots(figsize=(10, 4), facecolor=fig_bg_color)
                plotar_grafico(df, f"Tendência - {moeda.upper()}", cor, ax, moeda_fiat.upper())
                st.pyplot(fig)

            elif len(moedas) == 2:
                moeda1, moeda2 = moedas[0], moedas[1]
                df1, df2 = dados_hist[moeda1], dados_hist[moeda2]
                
                var1 = ((df1["price"].iloc[-1] - df1["price"].iloc[0]) / df1["price"].iloc[0]) * 100
                cor1 = "#00C805" if var1 >= 0 else "#FF4A4A"
                
                var2 = ((df2["price"].iloc[-1] - df2["price"].iloc[0]) / df2["price"].iloc[0]) * 100
                cor2 = "#00C805" if var2 >= 0 else "#FF4A4A"
                
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, facecolor=fig_bg_color)
                
                plotar_grafico(df1, f"{moeda1.upper()}", cor1, ax1, moeda_fiat.upper())
                plotar_grafico(df2, f"{moeda2.upper()}", cor2, ax2, moeda_fiat.upper())
                
                plt.tight_layout()
                st.pyplot(fig)

if __name__ == "__main__":
    main()