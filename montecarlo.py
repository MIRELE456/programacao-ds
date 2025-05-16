import numpy as np
import matplotlib.pyplot as plt

# Definição de parâmetros
anos = 10
retorno_medio = 0.07  # 7% de retorno médio anual
desvio_padrao = 0.20  # 20% de desvio padrão
simulacoes = 10  # Número de trajetórias simuladas
capital_inicial = 1000  # Valor inicial da carteira

# Simulação de Monte Carlo
anos_array = np.arange(anos + 1)
valores_simulados = np.zeros((simulacoes, anos + 1))
valores_simulados[:, 0] = capital_inicial

for i in range(simulacoes):
    for j in range(1, anos + 1):
        crescimento = np.random.normal(retorno_medio, desvio_padrao)
        valores_simulados[i, j] = valores_simulados[i, j - 1] * (1 + crescimento)

# Plotando os resultados
plt.figure(figsize=(10, 5))
for i in range(simulacoes):
    plt.plot(anos_array, valores_simulados[i], linewidth=1)

plt.xlabel("Ano")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo para Investimentos em Ações")
plt.grid(True)
plt.show()
