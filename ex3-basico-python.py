'''ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago
'''

cod1, qtd1, valor1 = map(float,input("infos peça 1: ").split())
cod2, qtd2, valor2 = map(float,input("infos peça 2: ").split())


total = (qtd1 * valor1) + (qtd2 * valor2)


print("Valor a pagar: ", str("%.2f"%total))