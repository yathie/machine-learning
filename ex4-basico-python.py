'''escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B, C.
Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3,14159)
c) a área do trapézio que tem A e B por bases e C por altura. ((A+B)C)/2
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''

a, b, c = map(float,input("Digite A, B e C: ").split())

#area do triangulo retangulo
triangulo = (a * c) / 2
#area do circulo
circulo = 3.14159 * (c ** 2)
#area do trapezio
trapezio = ((a + b) * c) / 2
#area quadrado
quadrado = b ** 2
#area retangulo
retangulo = a * b


print("triangulo: ", str("%.3f"%triangulo))
print("circulo: ", str("%.3f"%circulo))
print("trapezio: ", str("%.3f"%trapezio))
print("quadrado: ", str("%.3f"%quadrado))
print("retangulo: ", str("%.3f"%retangulo))