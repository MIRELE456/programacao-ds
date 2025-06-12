# Lista de alunos (nome, nota)
alunos = [
    ("Carlos", 85),
    ("Ana", 92),
    ("Bruno", 78),
    ("Mariana", 92),
    ("Pedro", 88)
]

# Ordenação por nome (modifica a lista original)
alunos.sort(key=lambda aluno: aluno[0])  # Ordena pelo nome (alfabético)
print("Ordenado por nome:", alunos)

# Ordenação por nota em ordem decrescente (gera nova lista)
alunos_por_nota = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
print("Ordenado por nota (decrescente):", alunos_por_nota)
