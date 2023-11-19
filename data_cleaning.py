import pandas as pd
import re

#Lendo o arquivo original
data = pd.read_csv("./SolarPrediction.csv/SolarPrediction.csv")
print(data.head())

#Fazendo uma cópia do dataframe
df = data.copy()

df['Data'] = df['Data'].apply(lambda x: x.split()[0])

#Criando as colunas 'Month' e 'Day' apartir da coluna fonte 'Data'
df['Month'] = pd.to_datetime(df['Data']).dt.month
df['Day'] = pd.to_datetime(df['Data']).dt.day

#Criando as colunas 'Hour', 'Minute' e 'Second' apartir da coluna fonte 'Time'
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df['Minute'] = pd.to_datetime(df['Time']).dt.minute
df['Second'] = pd.to_datetime(df['Time']).dt.second

print(df.head)

#Criando as colunas 'risehour' e 'riseminute' apartir da coluna fonte 'TimeSunRise'
df['risehour'] = df['TimeSunRise'].apply(lambda x : re.search(r'^\d+', x).group(0)).astype(int)
df['riseminute'] = df['TimeSunRise'].apply(lambda x : re.search(r'(?<=\:)\d+(?=\:)', x).group(0)).astype(int)

#Criando as colunas 'sethour' e 'setminute' apartir da coluna fonte 'TimeSunSet'
df['sethour'] = df['TimeSunSet'].apply(lambda x : re.search(r'^\d+', x).group(0)).astype(int)
df['setminute'] = df['TimeSunSet'].apply(lambda x : re.search(r'(?<=\:)\d+(?=\:)', x).group(0)).astype(int)

print(df.head)

#Removendo as colunas que não vão ter utilizadas
df.drop(['UNIXTime', 'Data', 'Time', 'TimeSunRise', 'TimeSunSet'], axis=1, inplace=True)

print(df.head)

#Passando o dataframe com os dados limpos do arquivo antigo para um novo
df.to_csv('SolarPrediction_CleanData.csv')
