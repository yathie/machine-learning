'''leia dois valores inteiros (a, b). Após, o programa deve mostrar uma mensagem "Sao multiplos" ou "Nao sao multiplos", indicando se os valores lidos são múltiplos entre si.
'''

a, b = map(int, input("Digite dois valores: ").split())

if a % b == 0 or b % a == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")

