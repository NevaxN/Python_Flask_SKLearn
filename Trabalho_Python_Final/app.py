
import joblib
from flask import Flask, jsonify, redirect, request, render_template, url_for
from flask_cors import CORS, cross_origin
import requests

'''Cria o app Flask e adiciona o CORS que permite que recursos restritos em uma página da web sejam recuperados por
outro domínio fora do domínio ao qual pertence o recurso que será recuperado.'''
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    """
    Rota principal que renderiza o formulário HTML para entrada de dados.
    """
    return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
@cross_origin()
def show_form():
    """
    Rota que processa os dados do formulário enviado via POST.
    Os dados são coletados do formulário HTML, convertidos em um objeto JSON
    e enviados para outra rota '/solar' para fazer a previsão de radiação solar.
    """
    print(f"Request Method => {request.method}")
    if request.method == 'POST':
        temperature = request.form['temperature']
        pressure = request.form['pressure']
        humidity = request.form['humidity']
        winddirection = request.form['winddirection']
        speed = request.form['speed']
        month = request.form['month']
        day = request.form['day']
        hour = request.form['hour']
        minute = request.form['minute']
        second = request.form['second']
        risehour = request.form['risehour']
        riseminute = request.form['riseminute']
        sethour = request.form['sethour']
        setminute = request.form['setminute']

        # Cria um objeto JSON com os dados coletados
        data = {
            "Temperature": temperature,
            "Pressure": pressure,
            "Humidity": humidity,
            "WindDirection(Degrees)": winddirection,
            "Speed": speed,
            "Month": month,
            "Day": day,
            "Hour": hour,
            "Minute": minute,
            "Second": second,
            "risehour": risehour,
            "riseminute": riseminute,
            "sethour": sethour,
            "setminute": setminute
        }

        print(data)

        # Envia os dados para a rota '/solar' usando o método POST
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://127.0.0.1:5000/solar", json=data, headers=headers, timeout=10)
        print(f'Resposta => {response}')
        retorno = response.json()
        print(f'Retorno => {retorno}')

        # Renderiza a página HTML de previsão com o resultado retornado
        return render_template('prev.html', prediction=retorno['prediction'])


@app.route('/solar', methods=['POST'])
@cross_origin()
def get_solarRadiation_prediction():
    """
    Rota que recebe os dados JSON enviados pela rota '/form' e faz a previsão
    de radiação solar usando um modelo previamente treinado.
    """
    features = request.json
    print('Received JSON data:', features)

    X = [features['Temperature'],
            features['Pressure'],
            features['Humidity'],
            features['WindDirection(Degrees)'],
            features['Speed'],
            features['Month'],
            features['Day'],
            features['Hour'],
            features['Minute'],
            features['Second'],
            features['risehour'],
            features['riseminute'],
            features['sethour'],
            features['setminute']]
    print(f"Valor de X: {X}")

    # Carrega o modelo treinado
    model = joblib.load('./Trabalho_Python_Final/model/model.joblib')

     # Faz a previsão usando o modelo
    y_pred = model.predict([X])
    print(f'Previsão => {y_pred[0]}')

    # Retorna a previsão em formato JSON
    prev = jsonify({'prediction': y_pred[0]})
    return prev

@app.route('/show_pred/<prediction>')
def show_pred(prediction):
    """
    Rota para exibir a previsão na página HTML.
    """
    return render_template('prev.html', prediction=prediction)

if __name__ == '__main__':
    # Inicia a aplicação Flask em modo de depuração
    app.run(debug=True)
