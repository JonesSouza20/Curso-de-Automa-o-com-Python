#Tipos de dados
nome = "Jones"      # string (texto)
idade = 22          # int (número inteiro)
altura = 1.80       # float (número decimal)
ativo = True        # booleano (verdadeiro/falso)


#Listas e Dicionários
#Lista: coleção ordenada
frutas = ["maçã", "banana", "uva"]
print(frutas[0])  # mostra "maçã"

#Dicionário: chave → valor
pessoa = {"nome": "Jones", "idade": 28}
print(pessoa["nome"])  # mostra "Jones"

#Loops
#For: repetir sobre listas
for fruta in frutas:
    print(fruta)

#While: repetir até condição parar
contador = 0
while contador < 3:
    print("Rodada:", contador)
    contador += 1

#Arquivos
#Criar e escrever em arquivo:
with open("teste.txt", "w") as f:
    f.write("Olá, mundo da automação!")

#Ler arquivo:
with open("teste.txt", "r") as f:
    print(f.read())


#Mini-projeto ao vivo
#Criar script que lê um arquivo de lista de compras e imprime cada item numerado.
with open("compras.txt", "r") as f:
    itens = f.readlines()

for i, item in enumerate(itens, start=1):
    print(f"{i}. {item.strip()}")
