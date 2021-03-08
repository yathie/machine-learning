'''A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

salario             percentual de reajuste
0 - 400.00          15%
400.01 -800.00      12%
800.01 - 1200.00    10%
1200.01 - 2000.00    7%
acima de 2000.00     4%

leia o salário do funcionário, calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual
'''

salario = float(input("Digite o salário: "))

if salario <= 400:
    percentual = "15%"
    reajuste = salario * 0.15
elif salario <= 800:
	percentual = "12%"
	reajuste = salario * 0.12
elif salario <= 1200:
	percentual = "10%"
	reajuste = salario*0.10

elif salario <= 2000:
	percentual = "7%"
	reajuste = salario * 0.07
else:
	percentual = "4%"
	reajuste = salario * 0.04

print ("novo salario: ", str("%.2f"%(salario + reajuste)))
print ("reajuste: ", str("%.2f"%reajuste))
print ("percentual: ", percentual)


