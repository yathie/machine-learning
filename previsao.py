#como ler dados com o pacote Pandas do Python
#https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data

#importar pandas
import pandas as pd

#caminho do arquivo
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

#metodo read_csv para importar os dados
df = pd.read_csv(url, header = None) #header = None -> indica que o arquivo não possui cabeçalho

#df.head(n) mostra as primeiras n linhas do conjunto dados
#df.tail(n) mostra as ultimas n linhas do conjunto dados
#print(df.head(5))

#atribuindo cabeçalho
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

#substituindo o cabeçalho padrão pelo 'headers'
df.columns = headers

#print(df.head(5))

#exportar dados para csv
#automoveis.csv -> nome escolhido para salvar o arquivo
path = "/home/.../cars.csv"
df.to_csv(path)



#metodos basicos do pandas

#checar typos de dados de um conjunto de dados
print(df.dtypes)

#resumo estatístico de cada coluna
#as métricas estatísticas podem dizer se há problemas matemáticos, como anomalias extremas e grandes desvios
print(df.describe(include = "all"))

'''
count - total de linhas por coluna
mean - valor médio da coluna
std - desvio padrão
min - valor mínimo
25% - limite de quartis
50%
75%
max - valor máximo

.describe() -> ignora linhas e colunas sem números
.describe(include = "all") -> mostra os resultados de todas as 26 colunas de df (colunas do tipo object). Apresentando um conjunto diferente de estatísticas:
unique - número de objetos distintos na coluna
top - objeto que ocorre com mais frequência
freq - número de vezes que o objeto top aparece na coluna
'''

#.info() -> mostra 30 linhas superiores e inferiores do conjunto de dados. É um sumário conciso da base de dados
print(df.info())