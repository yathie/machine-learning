'''um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido:
1 álcool
2 gasolina
3 diesel
4 fim

caso o usuário informe um código inválido deve ser solicitado um novo código, até que seja válido.

o programa será encerrado quando o código informado for o número 4
'''
count_alcool = 0
count_gasolina = 0
count_diesel = 0
opcao = 5

print ("1.álcool\n2.gasolina\n3.diesel\n4.fim")

while opcao != "4":
	opcao = input("escolha uma opção: ")

	if opcao == "1":
		count_alcool += 1
	elif opcao == "2":
		count_gasolina += 1
	elif opcao == "3":
		count_diesel += 1

print("\nmuito obrigado")
print("Álcool: ", count_alcool)
print("Gasolina: ", count_gasolina)
print("Diesel: ", count_diesel)
