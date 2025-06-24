
# Declara uma lista de dicionarios
pessoas = [
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 25},
    {"nome": "Pedro", "idade": 40}
]
# Salva a lista ordenada na variável ordenado_por_idade
ordenado_por_idade = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
# Mostra a lista ordenada com sorted()
print(ordenado_por_idade)

# Declara lista com nomes desordenados
nomes = ["Ana", "Beatriz", "Carlos", "Dê"]
# Ordena nova lista por comprimento usando função len
nomes_ordenados = sorted(nomes, key=len)
# Mostra a nova lista ordenada com sorted()
print(nomes_ordenados)
