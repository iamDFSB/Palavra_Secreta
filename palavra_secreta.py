import os
from time import sleep
##########################
print('COMEÇOU O JOGO DA PALAVRA SECRETA')
palavra = 'caderno'
palavra_formada = ''
contador = 0
##########################
while True:

    contador += 1
    chance = input('\nDigite (1) letra para descobrir a palavra: ').lower()
    if len(chance) > 1:
        print('Muitas letras, é apenas uma')
        continue

    if chance in palavra:
        palavra_formada += chance
        print('Acertou 😁')
    else:
        print('ERROU 😭')
    palavra_chave = ''

    for chance in palavra:
        if chance in palavra_formada:
            palavra_chave+=chance
        else:
            palavra_chave += '*'
    print(palavra_chave)

    if palavra_chave == palavra:
        os.system('cls')
        print('=+'*50)
        print('\t\033[32mVocê ganhou')
        print(f'\tSua palavra era "{palavra}"')
        print(f'\tVocê teve {contador} chances para acertar\033[m')
        print('=+'*50)
        sleep(5)
        break
