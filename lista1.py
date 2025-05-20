def main():
    # Recebe um número inteiro positivo n
    n = int(input("Digite a quantidade de números a serem inseridos na lista: "))
    
    # Cria uma lista e adiciona os n números inteiros fornecidos pelo usuário
    lista = []
    for _ in range(n):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)

    # Recebe um número inteiro x e verifica se ele pertence à lista
    x = int(input("Digite o número a ser verificado na lista: "))

    if x in lista:
        print(f"O número {x} está na lista.")
    else:
        print(f"O número {x} não está na lista.")

if __name__ == "__main__":
    main()
