import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

# Criar tabela de alunos se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL,
        idade INTEGER NOT NULL,
        senha TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/alunos', methods=['GET'])
def get_alunos():
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    if len(get_alunos()) >= 30:
        return jsonify({'message': 'Limite de alunos atingido. Não é possível adicionar mais alunos.'}), 403
    
    data = request.get_json()
    nome = data['nome']
    email = data['email']
    telefone = data['telefone']
    idade = data['idade']
    senha = data['senha']
    
    cursor.execute('INSERT INTO alunos (nome, email, telefone, idade, senha) VALUES (?, ?, ?, ?, ?)', (nome, email, telefone, idade, senha))
    conn.commit()
    
    return jsonify({'message': 'Aluno adicionado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)

