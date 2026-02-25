import requests
import pandas as pd
import matplotlib.pyplot as plt


def buscar_dados(coin_id: str, dias: int = 30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": dias}

    r = requests.get(url, params=params, timeout=20)

    if r.status_code != 200:
        print("Erro ao buscar dados:", r.status_code)
        print(r.text)
        return None

    data = r.json()
    if "prices" not in data:
        print("ID da moeda inválido ou resposta inesperada.")
        print("Resposta:", data)
        return None

    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df


def main():
    print("ANÁLISE CRYPTO (simples) 🚀")
    print("Exemplo de IDs: bitcoin, ethereum, solana, dogecoin, etc.")
    coin_id = input("Digite umas das moedas do exemplo : ").strip().lower()

    dias_txt = input("Quantos dias? (padrão 30): ").strip()
    dias = int(dias_txt) if dias_txt else 30

    df = buscar_dados(coin_id, dias)
    if df is None:
        return

    preco_inicial = df["price"].iloc[0]
    preco_final = df["price"].iloc[-1]
    variacao = ((preco_final - preco_inicial) / preco_inicial) * 100

    print(f"\nPreço inicial: ${preco_inicial:.2f}")
    print(f"Preço final:   ${preco_final:.2f}")

    if variacao > 0:
        print(f"Valorizou ✅ (+{variacao:.2f}%)")
    elif variacao < 0:
        print(f"Desvalorizou ❌ ({variacao:.2f}%)")
    else:
        print("Ficou no mesmo valor ➖ (0.00%)")

    
    plt.figure()
    plt.plot(df["timestamp"], df["price"])
    plt.title(f"{coin_id.upper()} - Últimos {dias} dias")
    plt.xlabel("Data")
    plt.ylabel("Preço (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()