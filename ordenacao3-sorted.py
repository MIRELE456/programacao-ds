# Declara a lista de dicionários representando estudantes e suas notas 
estudantes = [
    {"nome": "Carlos", "nota_media": 85.5},
    {"nome": "Ana", "nota_media": 92.0},
    {"nome": "Pedro", "nota_media": 78.0},
    {"nome": "Beatriz", "nota_media": 88.5},
    {"nome": "Mariana", "nota_media": 95.0}
]

# Ordenar estudantes pela variavel nota_media de forma decrescente
estudantes_ordenados_nota = sorted(estudantes, key=lambda x: x['nota_media'], reverse=True)

# Mostra lista ordenada de nome por nota media decrescente
print("Estudantes ordenados pela nota média (decrescente):")
for estudante in estudantes_ordenados_nota:
    print(f"{estudante['nome']}: {estudante['nota_media']}")

# Ordenar estudantes pela variavel nome em ordem alfabética
estudantes_ordenados_nome = sorted(estudantes, key=lambda x: x['nome'])

# Mostra lista ordenada de nomes alfabeticamente
print("\nEstudantes ordenados pelo nome (alfabética):")
for estudante in estudantes_ordenados_nome:
    print(f"{estudante['nome']}: {estudante['nota_media']}")
