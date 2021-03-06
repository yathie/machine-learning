#Algoritmo para aprender todos os atributos e os nomes dos animais, e o conhecimento obtido com esses dados é usado para testar novos animais.
from sklearn import tree

features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]

labels = ["chicken", "chicken", "horse", "horse"]
#labels = [0, 0, 1, 1]

classif = tree.DecisionTreeClassifier()

classif.fit(features, labels)

#teste de previsão 1
print (classif.predict([[7, 0.6, 41]]))
#output
# [0]  or a Chicken

#teste de previsão 1
print (classif.predict([[38, 600, 37.5]]))
# output
# [1]  or a Horse