from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados temporários (substituem um banco de dados real)
usuarios = {
    "admin": {"senha": "admin123", "tipo": "admin"},
    "cliente@exemplo.com": {"senha": "cliente123", "tipo": "cliente"}
}

pedidos = {
    "PG-2023-001": {
        "cliente": "cliente@exemplo.com",
        "status": "em_producao",
        "itens": ["Janela de Alumínio", "Porta de Correr"]
    }
}

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')

    if email in usuarios and usuarios[email]['senha'] == senha:
        return jsonify({"mensagem": "Login bem-sucedido!", "tipo": usuarios[email]['tipo']})
    
    return jsonify({"mensagem": "E-mail ou senha incorretos"}), 401

@app.route('/pedidos/<email>', methods=['GET'])
def listar_pedidos(email):
    pedidos_cliente = {k: v for k, v in pedidos.items() if v['cliente'] == email}
    return jsonify(pedidos_cliente)

if __name__ == '__main__':
    app.run(debug=True)