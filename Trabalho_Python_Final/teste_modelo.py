
import joblib

# Carrega o modelo treinado a partir do arquivo './model.joblib'
model = joblib.load('./Trabalho_Python_Final/model/model.joblib')

# Faz a previsão usando os dados de entrada carregados
y_pred = model.predict([[50,30.47,93,139.82,7.87,9,29,21,15,23,6,13,18,13]])

print(y_pred)
