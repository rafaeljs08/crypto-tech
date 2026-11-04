# Crypto Analise

Aplicação web em **Python + Streamlit** para acompanhar e comparar criptomoedas, com preço atual e histórico de até 365 dias. Usa a API pública da [CoinGecko](https://www.coingecko.com/en/api), sem necessidade de chave.

---

## Funcionalidades

- **Duas moedas ao mesmo tempo:** digite até dois IDs separados por vírgula (por exemplo `bitcoin, ethereum`) para comparar lado a lado.
- **USD ou BRL:** escolha em qual moeda os valores são exibidos.
- **Preço atual:** cotação do momento, com a variação dos últimos 7 dias.
- **Histórico:** escolha de 1 a 365 dias e veja o desempenho no período.
- **Gráficos:** linha com preenchimento, verde quando o período fecha em alta e vermelho quando fecha em queda.
- **Variação percentual** calculada entre o primeiro e o último ponto do período.
- **Tema escuro** aplicado por CSS na própria página.

---

## Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3 | Linguagem |
| Streamlit | Interface web |
| Requests | Chamadas à API |
| Pandas | Estruturação dos dados |
| Matplotlib | Gráficos |
| CoinGecko API | Fonte dos preços |

---

## Como executar

```bash
# 1. (Opcional) crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instale as dependências
pip install streamlit requests pandas matplotlib

# 3. Inicie o app
streamlit run crypto_analise.py
```

O navegador abre em `http://localhost:8501`.

---

## Observações

- A CoinGecko usa o **ID** da moeda (`bitcoin`), não o símbolo (`BTC`).
- Não é preciso chave de API, mas a API pública tem limite de requisições por minuto. Se aparecer erro de busca, aguarde um pouco e tente de novo.
- A imagem de fundo é carregada de um serviço externo (Unsplash) e exige conexão com a internet.

---

## Objetivo

Projeto educacional para praticar consumo de APIs, manipulação de dados com Pandas, visualização com Matplotlib e criação de interfaces com Streamlit.
