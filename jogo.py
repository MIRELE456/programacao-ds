# Importa o módulo random para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
tentativas = 0  # Inicializa a contagem de tentativas
max_tentativas = 5  # Define o número máximo de tentativas

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop do jogo
while tentativas < max_tentativas:
    # Captura a entrada do usuário e converte para inteiro
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas
    tentativas += 1

    # Verifica o palpite do jogador
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    else:
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restam
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Se o jogador não acertar dentro do número máximo de tentativas
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")
