from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        "id": 1,
        "titulo": "stumble guys",
        "genero": "Corrida de obstáculos",
        "plataforma": "PC, Androids e iOS",
        "ano": 2008
    },
    {
        "id": 2,
        "titulo": "Roblox",
        "genero": "Mundo virtual",
        "plataforma": "PC, Androids e iOS",
        "ano": 2017
    },
    {
        "id": 3,
        "titulo": "Fortnite",
        "genero": "Battle Royale",
        "plataforma": "PC, Androids e iOS",
        "ano": 2015
    }
]

@app.route('/api/jogos', methods=['GET'])
def listar_jogos():
    return jsonify(jogos)


@app.route('/api/jogos/<int:id>', methods=['GET'])
def obter_jogo(id):
    jogo = next((j for j in jogos if j['id'] == id), None)
    if jogo is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404
    return jsonify(jogo)


@app.route('/api/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()
    novo_jogo = {
        "id": len(jogos) +1,
        "titulo": dados.get("titulo"),
        "genero": dados.get("genero"),
        "plataforma": dados.get("plataforma"),
        "ano": dados.get("ano")
    }

    jogos.append(novo_jogo)
    return jsonify(novo_jogo), 201

@app.route('/api/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    jogo = next((j for j in jogos if j['id'] == id), None)
    if jogo is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    dados = request.get_json()
    jogo["nome"] = dados.get("nome", jogo["nome"])
    jogo["descricao"] = dados.get("descricao", jogo["descricao"])
    jogo["coordenador"] = dados.get("coordenador", jogo["coordenador"])
    jogo["membros"] = dados.get("membros", jogo["membros"])
   
    return jsonify(jogo)

@app.route('/api/jogos/<int:id>', methods=['DELETE'])
def excluir_jogo(id):
    global jogos
    jogos = [j for j in jogos if j['id'] != id]
    if not jogos:
        return jsonify({"erro": "Jogo não encontrado"}), 404
    
    jogos = [j for j in jogos if j['id'] != id]
    return jsonify({"mensagem": "Jogo excluido com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)