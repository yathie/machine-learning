'''leia 3 valores (A,B e C) que são as três notas de um aluno. 
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))

media = (a*2 + b*3 + c*5) / 10
media = str("%.1f"%media) #precisão de uma casa decimal

print("Média = ",media)