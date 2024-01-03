# Importa as bibliotecas necessárias.
from flask import Flask, render_template, request, redirect, url_for

# Importa o módulo sqlite3 para trabalhar com o banco de dados SQLite.
import sqlite3

# Importa o módulo migration para manipular o banco de dados.
import migration as db

# Inicializa uma instância da aplicação Flask.
app = Flask(__name__)

# Inicializa o banco de dados SQLite chamando a função 'init()' do módulo 'db'.
db.init()

# Rota principal que listará todos os usuários cadastrados no banco de dados.
@app.route('/')
def listar_usuarios():
    # Faz chamada a função 'listar_usuarios()' do módulo 'db' para obter os usuários do banco de dados.
    usuarios = db.listar_usuarios()
    # Renderiza o template 'lista.html' passando a lista de usuários como argumento
    return render_template('lista.html', usuarios=usuarios)

# Rota para adicionar um novo usuário.
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_usuario():
     # Verifica se o método da requisição é POST (para envio de formulário).
    if request.method == 'POST':
        # Obtém os dados do formulário enviado pelo método POST.
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Faz chamada a função 'criar_usuario()' do módulo 'db' para adicionar um novo usuário no banco de dados.
        db.criar_usuario(nome, email, senha)
        # Redireciona para a rota 'listar_usuarios' após adicionar o usuário.
        return redirect(url_for('listar_usuarios'))
    
    # Se o método da requisição não for POST, exibe o formulário para adicionar um novo usuário.
    return render_template('formulario.html', acao='Adicionar')