import json
from datetime import date

# Define a classe Cliente
class Cliente:
    def __init__(self, id, nome, email, pagamentos=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.pagamentos = pagamentos if pagamentos is not None else []

    # Adiciona um pagamento à lista
    def adicionar_pagamento(self, valor, data_pagamento, status):
        pagamento = {
            "valor": valor,
            "data": data_pagamento.isoformat(),
            "status": status
        }
        self.pagamentos.append(pagamento)

    # Converte o objeto Cliente em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "pagamentos": self.pagamentos
        }

# Crie um cliente
cliente = Cliente(1, "Joaquim Silva", "joaquim@email.com")

# Adiciona alguns pagamentos
cliente.adicionar_pagamento(250.00, date(2025, 9, 10), "pago")
cliente.adicionar_pagamento(150.00, date(2025, 9, 12), "pendente")

# Converta para JSON
cliente_json = json.dumps(cliente.to_dict(), indent=4)

# Imprime os dados em formato JSON
print(cliente_json)
