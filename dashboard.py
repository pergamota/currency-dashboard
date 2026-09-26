import requests 
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://open.er-api.com/v6/latest/USD"

def metodo_response():
    response = requests.get(BASE_URL, timeout=10)
    dados = response.json()

    cotacoes = dados['rates']
    moedas = ["BRL", "EUR", "GBP", "JPY", "CHF", "KYD", "BHD", "KWD"]
    valores = [cotacoes[m] for m in moedas]
    
    df = pd.DataFrame({"Moeda": moedas, "Cotacao": valores})
    print(df)

    output_path = "data/currency.csv"
    df.to_csv(output_path, index=False)

    plt.style.use('seaborn-v0_8') 
    plt.figure(figsize=(8, 5))
    plt.grid(axis='y', alpha=0.3)
    plt.bar(df['Moeda'], df['Cotacao'], color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    plt.title("Cotacoes das principais moedas (em USD)")
    plt.xlabel("Moeda")
    plt.ylabel("Cotacao")
    plt.show()

metodo_response()
