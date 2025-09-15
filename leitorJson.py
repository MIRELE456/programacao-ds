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
for pagamento in cliente["pagamentos"]:
    # Para cada pagamento, imprime a descrição e o valor
    print(f" - {pagamento['descricao']}: R$ {pagamento['valor']}")
