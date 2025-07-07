from flask import Flask, render_template, request
from main import predict_strategy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_strategy', methods=['POST'])
def get_strategy():
    circuit_input = request.form['circuit']
    constructor_input = request.form['constructor']

    result = predict_strategy(circuit_input, constructor_input)
    return render_template('index.html', result=result, circuit=circuit_input)

if __name__ == '__main__':
    app.run(debug=True)
