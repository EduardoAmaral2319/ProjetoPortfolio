from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    return f"Obrigado, {nome}! Dados recebidos com sucesso pelo back-end em Python."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
