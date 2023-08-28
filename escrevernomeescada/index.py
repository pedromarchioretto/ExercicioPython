import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("-nome", type=str, help='o nome do usuário') 
parser.add_argument("-reps", type=int, help='o número de repetições') 
args = parser.parse_args()

#garante que o nome e a quantidaed de repetições tenham sido fornecidas
#ensures that the name and quantity of repetitions have been provided
if not args.nome:
    print("[+] Especifique o nome")
    exit()
elif not args.reps:
    print("[+] Especifique a quantidade de repetições")
    exit()

repeticoes = args.reps

#repetirá a quantidade fornecida
#to repeat the quantity provided
for i in range(0, repeticoes):
    nome = args.nome
    lennome = len(nome) - 1
    indice = 1

    #escreve o nome em escada do primeiro até o ultimo caractere
    #write the name in stairs style from the first to the last character
    while indice <= lennome:
        validar = nome[0:indice]
        if validar[-1] != " ":
            print(nome[0:indice])
        
        indice += 1

    indice = lennome + 1

    #escreve o nome em escada do último até o primeiro caractere
    #write the name in stairs style from the last to the first character
    while indice >= 1:
        validar = nome[0:indice]
        if validar[-1] != " ":
            print(nome[0:indice])

        indice -= 1