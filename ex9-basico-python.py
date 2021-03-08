'''leia os valores de um vetor, encontre o menor elemento deste vetor e a sua posição dentro do vetor
'''
vetor = [int(i) for i in input("Digite um vetor: ").split()]

menor_valor = min(vetor) # min() funcao que retorna o menor elemento
indice = vetor.index(menor_valor)

print("Menor valor: ", menor_valor)
print("Posição: ", indice)
