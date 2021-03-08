'''faça um programa que leia um valor e apresente o número de Fibinacci correspondente a este valor lido. Lembre que os primeiros elementos sa série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele.
0 1 1 2 3 5...
'''
posicao = int(input("Digite uma posição: "))

def fib(x):
	seq = [0, 1, 1]
	for i in range(3, x+1): #range(2,4) -> 2,3
		seq.append(seq[i-1] + seq[i-2]) #append() adiciona ao fim
	return seq[x]

resultado = fib(posicao)

print("fib ("+str(posicao)+") = ", resultado)
