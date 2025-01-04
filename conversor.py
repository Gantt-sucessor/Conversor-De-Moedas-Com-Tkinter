import tkinter as tk

def mostrar_selecao():
    try:
        # Pega o valor digitado no Entry
        valor = float(entrada.get())  # Converte o valor para número (float)
        
        # Pega as moedas de origem e destino
        origem = moeda_origem.get()
        destino = moeda_destino.get()

        taxas_conversao = {
            ("Real", "Euro"): 0.18,
            ("Real", "Iene"): 26.32,
            ("Real", "Libra Esterlina"): 0.13015, 
            ("Real", "Dólar"): 0.19,

            ("Euro", "Real"): 5.55,
            ("Euro", "Iene"): 162.11,
            ("Euro", "Real"): 6.37622 ,
            ("Euro", "Libra Esterlina"): 0.82971,

            ("Dólar", "Real"): 6.185,
            ("Dólar", "Iene"): 157.23,
            ("Dólar", "Libra Esterlina"): 0.8057 ,
            ("Dólar", "Euro"): 0.9698,

            ("Libra Esterlina", "Real"): 7.68258 ,
            ("Libra Esterlina", "Euro"): 1.20524,
            ("Libra Esterlina", "Iene"): 196.81,
            ("Libra Esterlina", "Dolar"): 1.24220,

            ("Iene", "Real"): 0.03933,
            ("Iene", "Dolar"): 0.006357,
            ("Iene", "Euro"):  0.00619,
            ("Iene", "Libra Esterlina"): 0.0051 ,
              
        }

        chave = (origem, destino)
        if chave in taxas_conversao:
            taxa_conversao = taxas_conversao[chave]
            resultado = valor * taxa_conversao
            label_resultado.config(text=f"Converter {valor} de {origem} para {destino} = {resultado:.2f}")
        else:
            label_resultado.config(text="Conversão não disponível para estas moedas.")
        
    except ValueError:
        # Caso o valor inserido não seja um número válido
        label_resultado.config(text="Por favor, insira um valor numérico válido.")
        
        resultado = valor  
        
        # Atualiza o label com a informação da conversão
        label_resultado.config(text=f"Converter {valor} de {origem} para {destino} = {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")

janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("400x300")

moedas = ["Iene", "Euro", "Dólar", "Real", "Libra Esterlina"]

# Variáveis para armazenar a moeda selecionada em cada OptionMenu
moeda_origem = tk.StringVar()
moeda_origem.set(moedas[0])  # Valor inicial da moeda de origem

moeda_destino = tk.StringVar()
moeda_destino.set(moedas[1])  # Valor inicial da moeda de destino

# Label e OptionMenu para a moeda de origem
label_origem = tk.Label(janela, text="Quero converter de: ")
label_origem.pack()

menu_origem = tk.OptionMenu(janela, moeda_origem, *moedas)
menu_origem.pack(pady=20)

# Label e OptionMenu para a moeda de destino
label_destino = tk.Label(janela, text="Para: ")
label_destino.pack()

menu_destino = tk.OptionMenu(janela, moeda_destino, *moedas)
menu_destino.pack(pady=20)

# Label para mostrar a conversão
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Campo de entrada para o valor
entrada = tk.Entry(janela)
entrada.pack()

# Botão para confirmar a conversão
botao = tk.Button(janela, text="Converter", command=mostrar_selecao)
botao.pack(pady=10)

janela.mainloop()
