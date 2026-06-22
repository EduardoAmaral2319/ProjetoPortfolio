from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/contato', methods=['POST'])
def contato():
    # 1 - Captura todos os campos criados no HTML
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('mensagem')
    
    # 2 - Retorna a página de sucesso estilizada no tema preto/verde
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mensagem Enviada</title>
    </head>
    <body style="background-color: #0d1117; color: #c9d1d9; font-family: sans-serif; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; text-align: center;">
        <div style="background-color: #161b22; padding: 40px; border-radius: 12px; border: 1px solid #30363d; max-width: 500px;">
            <h2 style="color: #00ff66; margin-bottom: 16px;">Mensagem Enviada! 🚀</h2>
            <p>Obrigado pelo contato, <strong>{nome}</strong>.</p>
            <p style="margin-bottom: 24px;">Sua mensagem foi recebida com sucesso e retornarei o mais breve possível.</p>
            <a href="/" style="background-color: #00ff66; color: #0d1117; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block;">Voltar ao Portfólio</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)