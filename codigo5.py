nomes = []
contador = 0

while contador <= 10:
    nome = input("Digite o nome (ou digite 'fim' para encerrar): ")

    if nome.lower() == 'fim':
        break

    if nome.isalpha():
        nomes.append(nome)
        contador += 1
    else:
        print("Nome inválido. Por favor, digite apenas letras.")

nomes.sort() 
print(nomes)
