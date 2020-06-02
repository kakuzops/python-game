print('Bem vindo ao jogo de adivinhação!')


numero_secreto = 42

chute_str = input("Digite o seu Numero: ")

print("Você digitou", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("vc acertou")
else:
    print("vc errou")