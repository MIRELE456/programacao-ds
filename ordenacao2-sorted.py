# Lista de dicionários representando produtos
produtos = [
    {"nome": "Teclado", "preco": 45.50, "quantidade": 12},
    {"nome": "Mouse", "preco": 20.75, "quantidade": 50},
    {"nome": "Monitor", "preco": 150.00, "quantidade": 8},
    {"nome": "CPU", "preco": 500.00, "quantidade": 5},
    {"nome": "Cabo HDMI", "preco": 15.00, "quantidade": 30}
]
# Ordenar os produtos pelo comprimento do nome
ordenacao_comprimento_nome = sorted(produtos, key=lambda x: len(x['nome']))
# Mostra lista ordenada com nome e preço dos produtos
print("\nProdutos ordenados pelo comprimento do nome:")
for produto in ordenacao_comprimento_nome:
    print(f"{produto['nome']}: ${produto['preco']}")
