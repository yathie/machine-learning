'''a corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que várias pessoas dediquem suas vidas tentando capturar lesmas velozes, e treiná-las para faturar milhões em corridas pelo mundo.
Porém, a tarefa de capturar lesmas velozes não é uma tarefa muito fácil, pois praticamente todas as lesmas são muito lentas. Cada lesma é classificada em um nível, dependendo de sua velocidade:

nível 1: se a velocidade é menor que 10cm/h
nível 2: se a velocidade é maior ou igual a 10cm/h e menor que 20cm/h
nível 3: se a velocidade é maior ou igual a 20cm/h

sua tarefa é identificar qual nível de velocidade da lesma mais veloz de um grupo de lesmas
'''
lesmas = [int(i) for i in input("Digite as velocidades: ").split()]

maior_valor = max(lesmas) # max() funcao que retorna o maior elemento

if maior_valor < 10:
	print(1)
elif maior_valor < 20:
	print(2)
else:
	print(3)




