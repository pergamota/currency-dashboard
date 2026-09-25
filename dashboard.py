import requests 
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://open.er-api.com/v6/latest/USD"

def metodo_response():
    response = requests.get(BASE_URL, timeout=10)
    dados = response.json()
    cotacoes = dados['rates']
    moedas = ["BRL", "EUR", "GBP", "JPY"]
    valores = [cotacoes[m] for m in moedas]
    print(pd.DataFrame({"Moeda": moedas, "Cotacao": valores}))
    df = pd.DataFrame({"Moeda": moedas, "Cotacao": valores})
    print(df)
    output_path = "data/currency.csv"
    df.to_csv(output_path, index=False)

metodo_response()
