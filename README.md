# 🚀 Análise Simples de Criptomoedas

Projeto em Python que permite analisar rapidamente a valorização ou desvalorização de uma criptomoeda em determinado período, além de gerar um gráfico da variação de preço.

Utiliza a API pública da CoinGecko (não precisa de chave de API).

---

## 📌 Funcionalidades

- Busca dados reais de criptomoedas
- Gera gráfico de preço
- Calcula variação percentual
- Indica se valorizou ou desvalorizou
- Execução direta no terminal

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Requests
- Pandas
- Matplotlib
- API pública CoinGecko

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