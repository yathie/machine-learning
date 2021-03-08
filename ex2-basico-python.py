'''faça um programa que leia o nome de um vendedor, o seu salário e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais
'''

vendedor = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário: "))
vendas = float(input("Digite o total de vendas:"))

salario_final = salario + vendas*0.15
salario_final = str("%.2f"%salario_final) #precisão de duas casas decimais

print("Total para ",vendedor, " receber: ", salario_final)