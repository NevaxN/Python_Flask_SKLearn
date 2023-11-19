import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# Carrega os dados do arquivo CSV
data = pd.read_csv('./SolarPrediction_CleanData.csv')
# Remove linhas com valores nulos
data = data.dropna()

# Separa os dados em características (X) e rótulos (y)
X = data.iloc[ : , 1:15].values
y = data.iloc[ : , 0:1].values

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Cria e treina o modelo de regressão RandomForest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salva o modelo treinado em um arquivo joblib
joblib.dump(model, 'model.joblib')

# Faz previsões no conjunto de teste
y_pred = model.predict(X_test)

# Imprime algumas previsões e os valores reais correspondentes
for i in range(20):
    print(y[i], '=>', y_pred[i])

# Avalia o desempenho do modelo usando métricas de regressão
"""
Calcula o Erro Médio Quadrático (MSE) entre os valores reais (y_test) e as previsões do modelo (y_pred). O MSE é uma
métrica que mede a média dos quadrados dos erros entre as previsões e os valores reais. Quanto menor o MSE, melhor o
desempenho do modelo.
"""
mse = mean_squared_error(y_test, y_pred)
"""
Calcula o Erro Médio Absoluto (MAE) entre os valores reais (y_test) e as previsões do modelo (y_pred). O MAE é a
média das diferenças absolutas entre as previsões e os valores reais. Ele fornece uma medida da magnitude média dos
erros, sendo também uma métrica de desempenho.
"""
mae = mean_absolute_error(y_test, y_pred)
"""
Calcula o Coeficiente de Determinação (R²) entre os valores reais (y_test) e as previsões do modelo (y_pred). O R² é uma
métrica que varia de 0 a 1 e indica a proporção da variabilidade nos valores reais que é explicada pelo modelo. Um R²
mais próximo de 1 indica um bom ajuste do modelo.
"""
r2 = r2_score(y_test, y_pred)

# Imprime as métricas de desempenho
print(f"Erro Médio Quadrático (MSE): {mse:.2f}")
print(f"Erro Médio Absoluto (MAE): {mae:.2f}")
print(f"Coeficiente de Determinação (R²): {r2*100:.2f}%")