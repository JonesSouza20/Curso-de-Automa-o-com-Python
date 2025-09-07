frutas = ["maçã", "banana", "uvas"]

print(frutas[1])

pessoa = {"Nome": "Jones", "Idade": 26}

print(pessoa["Idade"])


for fruta in frutas:
    print(fruta)

contador = 0

while contador < 4:
    print("Rodada:", contador)
    contador += 1

''' with open("text.txt", "w") as f:
    f.write("Carne, arroz, banana, morango do amor, pistache, labubu") 

with open("text.txt", "r") as f:
    print(f.read()) '''

import os
caminho = r"C:\Users\Particular\Documents\GitHub\Curso-Python\text.txt"

with open(caminho, "r", encoding="utf-8") as f:
    itens = [linha.strip() for linha in f if linha.strip()]

    for i, item in enumerate(itens, start=1):
        print(f"{i}.{item}")
