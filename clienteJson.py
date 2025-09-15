# Importa a biblioteca JSON do Python
import json

# Define a classe cliente
class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        
#Converte o objeto Cliente em um dicionário.
#Isso facilita a serialização para JSON ou outros formatos.
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }

# Crie um cliente
cliente = Cliente(1, "Joaquim Silva", "joaquim@email.com")

# Converta para JSON
cliente_json = json.dumps(cliente.to_dict(), indent=4)

# Imprime os dados em formato JSON 
print(cliente_json)
