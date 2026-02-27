
# 🚀 Análise Simples de Criptomoedas

Uma aplicação web interativa e moderna desenvolvida em Python com Streamlit para monitorar, analisar e comparar o mercado de criptomoedas em tempo real ou através de gráficos históricos.

O projeto utiliza a API pública da CoinGecko, dispensando a necessidade de chaves de API (API Keys).

---

## 📌 Funcionalidades

- **Interface Web Dashboard:** Layout centralizado com temática escura (Dark Theme) estilo corretoras de criptomoedas.
- **Suporte Multi-Moedas:** Opção de visualizar valores tanto em Dólar (USD) quanto em Real Brasileiro (BRL).
- **Tempo Real & Histórico:** Visualize o preço exato do momento (com tendência de 7 dias) ou escolha um período histórico de até 365 dias.
- **Comparação de Ativos:** Digite até duas criptomoedas simultaneamente para comparar seus desempenhos lado a lado.
- **Gráficos Dinâmicos:** Gráficos com preenchimento (sombra) que mudam de cor automaticamente (verde para lucro, vermelho para queda).
- **Cálculo de Variação:** Exibe a variação percentual exata do período selecionado.
---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Streamlit** (Criação da Interface Web)
- **Requests** (Comunicação com a API)
- **Pandas** (Estruturação dos dados)
- **Matplotlib** (Plotagem dos gráficos)
- **API Pública CoinGecko**
---

## 📦 Instalação

pip install requests pandas matplotlib

---

## ▶️ Como Executar

python crypto_analise.py

O programa solicitará:

- ID da criptomoeda (ex: `bitcoin`, `ethereum`, `solana`)
- Quantidade de dias para análise

---

## ⚠️ Observações

- A CoinGecko usa o ID da moeda (ex: `bitcoin`), não o símbolo (BTC).
- Não é necessário API Key.
- Pode haver limitação se muitas requisições forem feitas rapidamente.

---

## 🎯 Objetivo

Projeto educacional para praticar:

- Consumo de APIs
- Manipulação de dados com Pandas
- Visualização com Matplotlib
- Estrutura básica de aplicações em Python