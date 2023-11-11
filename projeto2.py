import tkinter as tk
from tkinter import messagebox
import math
import requests
import xmltodict

def meta_financeira():
    def calcular_meses():
        # Obtém os valores da meta e mensal
        meta = entry_meta.get()
        mensal = entry_mensal.get()

        # Verifica se os valores são numéricos
        if not meta.isnumeric() or not mensal.isnumeric():
            messagebox.showerror("Erro", "Os valores da meta e mensal devem ser números")
            return

        # Converte os valores para inteiros
        meta = int(meta)
        mensal = int(mensal)

        # Calcula o número de meses necessários para atingir a meta
        meses = math.ceil(meta / mensal)

        # Atualiza o rótulo com o resultado
        label_meses.config(text=meses)

    # Cria a janela principal
    janela = tk.Tk()
    janela.geometry("400x100")
    janela.title("Meta Financeira")
    janela.config(padx=10, pady=10)

    # Cria e configura os widgets na janela
    label_meta = tk.Label(janela, text="Meta de poupança:")
    label_meta.grid(row=0, column=0)

    entry_meta = tk.Entry(janela)
    entry_meta.configure(width=20)
    entry_meta.grid(row=0, column=1)

    label_mensal = tk.Label(janela, text="Valor de poupança mensal:")
    label_mensal.grid(row=1, column=0)

    entry_mensal = tk.Entry(janela)
    entry_mensal.configure(width=20)
    entry_mensal.grid(row=1, column=1)

    button_calcular = tk.Button(janela, text="Calcular", command=calcular_meses)
    button_calcular.grid(row=2, column=0)

    label_meses_total = tk.Label(janela, text="Número de meses:")
    label_meses_total.grid(row=2, column=1)
    label_meses = tk.Label(janela, text="")
    label_meses.grid(row=2, column=2)

    # Inicia o loop principal da interface gráfica
    janela.mainloop()

def conversor_moedas():
    # Faz uma requisição à API para obter as moedas disponíveis
    symbols_url = "https://economia.awesomeapi.com.br/xml/available"
    response_symbols = requests.get(symbols_url)

    # Desserializa o resultado da requisição
    symbols_data = xmltodict.parse(response_symbols.content)
    symbols_list = {}
    for symbol, country in symbols_data["xml"].items():
        symbols_list[symbol] = country

    def convert():
        # Função auxiliar para encontrar a chave correspondente ao valor no dicionário
        def encontrar_chave(valor, dicionario):
            for chave, valor_atual in dicionario.items():
                if valor_atual == valor:
                    return chave
            return None

        # Obtém a moeda escolhida pelo usuário
        coins_value = coins_variable.get()
        coins_symbols = encontrar_chave(coins_value, symbols_list)
        coins_symbols_xml = coins_symbols.replace("-", "")

        # Obtém a cotação da moeda escolhida
        url_cotacao = f"https://economia.awesomeapi.com.br/last/{coins_symbols}"
        response_cotacao = requests.get(url_cotacao)

        if response_cotacao.status_code == 200:
            rate = float(response_cotacao.json()[coins_symbols_xml]["bid"])
        else:
            rate = None

        # Obtém o valor a ser convertido e realiza a conversão
        amount = amount_entry.get()
        # Verifica se há valor inserido e se ele é numérico
        if not amount.isnumeric() or not amount:
            messagebox.showerror("Erro", "O valor deve ser preenchido e deve ser numérico")
            return
        converted_amount = round((float(amount) * rate), 2)

        # Exibe o resultado
        result_label.config(text=f"O valor convertido é igual a {converted_amount}")

    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Conversor de moedas")

    janela.geometry("400x100")
    country_list = list(symbols_list.values())
    coins_variable = tk.StringVar(janela)
    coins_variable.set("Escolha a moeda que deseja converter.")
    coins_select = tk.OptionMenu(janela, coins_variable, *country_list)
    coins_select.pack()

    # Adiciona um botão para realizar a conversão
    convert_button = tk.Button(janela, text="Converter", command=lambda: convert())
    convert_button.pack()

    # Adiciona um campo de entrada para o valor a ser convertido
    amount_entry = tk.Entry(janela)
    amount_entry.pack()

    # Adiciona um rótulo para exibir o valor convertido
    result_label = tk.Label(janela, text="")
    result_label.pack()

    # Inicia o loop principal da interface gráfica
    janela.mainloop()


janela = tk.Tk()
janela.title("Menu")
janela.geometry("400x100")

app_label = tk.Label(janela, text="Escolha a ferramenta desejada.")
app_label.pack()

# Cria os botões
botao_meta = tk.Button(janela, text="Meta financeira", command=meta_financeira)
botao_moedas = tk.Button(janela, text="Conversor de moedas", command=conversor_moedas)
botao_meta.pack(anchor=tk.CENTER)
botao_moedas.pack(anchor=tk.CENTER)

# Inicia o loop principal da interface gráfica
janela.mainloop()