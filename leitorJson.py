import json  # Importa o módulo JSON para trabalhar com dados no formato JSON

# Define uma string JSON com os dados de um cliente e seus pagamentos
dados_json = '''
{
    "id": 2020,
    "nome": "Maria Aparecida",
    "pagamentos": [
        {"id": 123, "descricao": "Compra do livro Cangaceiro JavaScript", "valor": 50.5},
        {"id": 124, "descricao": "Mensalidade escolar", "valor": 1500}
    ]
}
'''

# Converte a string JSON em um dicionário Python
cliente = json.loads(dados_json)

# Exibe o nome e o ID do cliente formatado
print(f"Cliente: {cliente['nome']} (ID: {cliente['id']})")

# Exibe os pagamentos realizados pelo cliente
print("Pagamentos:")
total_gasto = 0  # Inicializa o total gasto

for pagamento in cliente["pagamentos"]:
    print(f" - {pagamento['descricao']}: R$ {pagamento['valor']}")
    total_gasto += pagamento["valor"]  # Soma o valor ao total

# Exibe o total gasto
print(f"\n💰 Total gasto: R$ {total_gasto:.2f}")
