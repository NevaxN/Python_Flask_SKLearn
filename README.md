# Python_Flask_SKLearn
# Alunos: Arthur Phelipe Mayer Santos e Lucas Gabriel

O objetivo é usar machine learning com scikit-learn para prever a radiação solar por meio de uma API. Isso beneficia previsões solares, eficiência em edifícios, agricultura, previsões meteorológicas e mais.

A Api utilizada foi pega no Kaggle: https://www.kaggle.com/datasets/dronio/SolarEnergy

Ouve uma limpeza dos dados dessa Api para que algumas colunas que eram inúteis para o treinamento do modelo de Machine Learning fossem removidas e outras novas colunas que condizem com o objetivo final da previsão foram adicionadas assim criando um novo arquivo csv.

Inicialmente o modelo de Machine Learning foi criado e treinado no arquivo "training.py", ouve então o teste no arquivo "teste_modelo".
Após o teste o modelo foi adicionado ao arquivo "app.py" que utiliza o framework Flask para fazer requisições HTTP.

Obs 1: o arquivo "model.joblib" está compactado em um arquivo pois era grande demais e não era possível adicionar ao repositório, só precisará descompactalo e rodar a rota  "./Trabalho_Python_Final/model/model.joblib" até o arquivo ja está adicionada. Caso tirar o arquivo
joblib da pasta model deverá mudar a rota nos arquivos "app.py" e "teste_modelo.py".

Obs 2: É possível que ocorra um erro de "timeout" quando enviar os valores do formulário para conseguir a previsão, o motivo é o tempo que o modelo esta levando para fazer a previsão, nesse caso recomendo que aumente o tempo de timeout no arquivo "app.py", a variáve
timeout estará na linha: 
"response = requests.post("http://127.0.0.1:5000/solar", json=data, headers=headers, timeout=10)".

Todos os arquivos estão comentados explicando a função de cada linha no código, existem alguns prints para que haja um acompanhamento de todo processo até a visualização da página final onde está o resultado da previsão. 

Obrigado pela atenção!
