#Proposta da atividade: Criar um programa que leia números de um arquivo externo e calcule em um processo filho todos os números pares no intervalo entre os números informados. Ao final os números calculados devem ser alocados em um novo arquivo e exibidos na tela.

import os

#Recebendo os números do arquivo e exibindo-os na tela:
numeroInicial = int(input())
numeroFinal = int(input())
print("\nNúmero inicial: ", numeroInicial)
print("Número final: ", numeroFinal, "\n")

#Duplicando o processo:
PID = os.fork()

#Fazendo com que o pai aguarde a execução do filho:
if PID != 0:
    os.wait()

    #Pai volta a executar exibindo o arquivo gerado pelo filho:
    arq = open("tmp/pares.txt")
    linhas = arq.readlines()
    print('\nConteúdo do arquivo: \n')
    for linha in linhas:
        print(linha)

#Filho escrevendo os números pares dentro do intervalo no arquivo:
else:
    arquivo = open("tmp/pares.txt", "w+")
    for i in range (numeroInicial, numeroFinal + 1):
        if i % 2 == 0:
            arquivo.write((f'{i} \n'))
            