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
df.head(5)

#atribuindo cabeçalho
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

#substituindo o cabeçalho padrão pelo 'headers'
df.columns = headers

#print(df.head(5))

#exportar dados para csv
#automoveis.csv -> nome escolhido para salvar o arquivo
path = "/home/.../cars.csv"
#df.to_csv(path)



#metodos basicos do pandas

#checar typos de dados de um conjunto de dados
df.dtypes

#resumo estatístico de cada coluna
#as métricas estatísticas podem dizer se há problemas matemáticos, como anomalias extremas e grandes desvios
df.describe(include = "all")

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
#df.info()


'''
#acesso a banco de dados com Python

#code using DB-API
from dbmodule import connect

#create connection object
connection = connect('databasename', 'username', 'pswd')
#create a cursor object
cursor = connection.cursor()

#run queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

#free resources
Cursor.close()
connection.close()
'''



##
#técnicas de pré-processamento
'''
objetivos
-identify and handle missing values
-data formatting
-data normalization (centering/scaling)
-data binning
-turning categorical values to numeric variables
'''

#remover ou substituir missing values em Python
#.dropna() -> permite remover linhas ou colunas com valores ausentes
#axis=0 remove toda a linha
#axis=1 remove toda a coluna
#ex.: df.dropna(subset=["coluna"], axis=0, inplace = True)
#df.dropna(subset=["coluna"], axis=0) -> não muda oa estrutura de dados
#inplace = True -> escreve o resultado de volta no conjunto de dados
#http://pandas.pydara.org/

#substituir
#df.replace(missing_value, new_value)
'''exemplo: substituir um valor  NaN na coluna normalized_losses
1- calcular a media da coluna: mean = df["normalized_losses"].mean()
2 -  substituir: df["normalized_losses"].replace(np.nan, mean)
'''

#formatacao de dados
'''exemplo converter "mpg" para "L/100km" em df
1- converter os valores da coluna: df["city-mpg"] = 235/df["city-mpg"]
2- renomear a coluna: df.rename(columns = {"city-mpg": "city-L/100km"}, inplace = True)
'''
#converter tipo de dados de uma coluna
#identificar os tipos de dados
print(df.dtypes["price"])
#converter -> df['price'] = df['price'].astype(int)
#teste claisa df['price'] = df['price'].convert_dtypes() 
#converter para float
df.price = pd.to_numeric(df.price, errors="coerce")
print(df.dtypes["price"])

#normalizando dados
#simple feature scaling ->xnew=xold/xmax -> dessa forma os valores variam de 0 a 1
'''min-max -> xnew = (xold-xmin)/(xmax-xmin) -> dessa forma os valores variam de 0 a 1
exemplo numa coluna chamada length
df["length"] = (df["length"]-df["length"].min()) / (df["length"].max() - df["length"].min())

Z-score -> xnew = (xold-mu)/sigma (mu=media do elemento) (sigma=desvio padrão) - tipicamente variam entre -3 a +3, mas pode ser mais alto ou menor
dessa forma os valores variam de 0 a 1
exemplo numa coluna chamada length
df["length"] = (df["length"]-df["length"].mean()) / (df["length"].std())
'''

#Compartimentação (binning)
''' compartimentação é quando agrupamos valores em compratimentos. Por exemplo, colocar 'idade' em grupos de [0 a 5], [6 a 10], [11 a 15],...
#gerar os 4 compartimentos igualmente espaçados
import numpy as np
bins = np.linspace(min(df["price"]), max(df["price"], 4))
#criar lista para nomear os grupos
group_names = ["Low", "Medium", "High"]
#vincular o nome da lista ao compartimento gerado
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)
'''

'''Categorical variables
transformando variáveis categóricas em variaveis quantitativas
#exemplo de uma coluna 'fuel' com valores 'gas' e 'diesel'
pd.get_dummies(df['fuel']) -> gera automaticamente uma lista de números, cada um correspondendo a uma categoria especifica de variável
'''

##
#Análise de dados exploratórios - básico
'''objetivos
- descriptve statistics -> estatistica descritiva descreve aspectos básicos de um conjunto de dados
-groupBy
-ANOVA -> análise de variância, metodo estístico no qual a variação em um grupo de observações é dividido em componentes distintos
- correlation
-correlation - statistics (Pearson e mapas termicos)
'''

'''descriptve statistics 
é importante explorar os dados antes de construir modelos complicados, estatistica descritiva ajuda nisso.
A análise estatística descritiva descreve elementos básicos de um conjunto, e obtem um breve resumo sobre a amostra e as medidas dos dados
#metodo1 
#computa automaticamente estatísticas básicas de todas as variaveis numericas - Os valores de NaN serão excluídos
df.describe()
#metodo2
#resumir variaveis categoricas - elas são variáveis que podem ser divididas em diferentes categorias ou grupos
#exemplo categoria 'drive-wheels', pode-se contar o total de cada variavel diferente.
  drive_wheels_counts = df["drive-wheels"].value_counts().to_frame()
  drive_wheels_counts.rename(columns={'drive-wheels':'values_counts'}, inplace=True)
'''
drive_wheels_counts = df["drive-wheels"].value_counts().to_frame()
#alterando nome da coluna para facilitar a leitura
drive_wheels_counts.rename(columns={'drive-wheels':'values_counts'}, inplace=True)
print(drive_wheels_counts)

'''GroupBy
o método .Groupby() agrupa os dados em subconjuntos segundo diferentes categorias dessa variável.
Ex. queremos encontrar o preço médio dos veículos , mas eles diferem entre tipos de tração e estilo de carroceria:
'''
#1- pegamos as colunas de interesse
df_test = df[['drive-wheels', 'body-style', 'price']]
#2 - agrupamos dados reduzidos de tração e carroceria
#estamos interessados em saber como o preço medio varia, pegamos a média de cada grupo e anexamos esse pedaço ao fim da linha. Os dados estão agrupados em subcategorias, e somente o preço médio de cada subcategoria é mostrado
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
print(df_grp)
#tabela dinamica com body-style na coluna e drive-wheels na linha
df_pivot = df_grp.pivot(index= 'drive-wheels', columns='body-style')
print(df_pivot)
#tabela dinamica de grafico de calor
'''import matplotlib.pyplot as plt
plt.pcolor(df_pivot, cmap='RdBu')
plt.colorbar()
plt.show()'''

'''correlação
é uma metrica estatistica para medir que ponto variaveis diferentes sao interdependentes. em outras palavras, quando olhamos para duas variaveis ao longo do tempo, se uma variavel mudar, como isso afeta a mudanca na outra variavel?
exemplo: cancer de pulmao -> fumantes; chuva -> sombrinha
eh importante saber que a correlaçao nao implica causalidade. ou seja, pode-se dizer q chuva e sombrinha estao correlacionadas, mas nao ha informacao suficiente para se dizer se a soombringa causou a chuva ou se a chuva causa a sombrinha
'''
#positive linear relationship
#correlacao entre tamanho do motor e preco
#grafico dispersao com linha de regressao
'''import matplotlib.pyplot as plt
import seaborn as sns
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()'''
#negative linear relationship
#correlacao entre highway-mpg e price
import matplotlib.pyplot as plt
import seaborn as sns
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()