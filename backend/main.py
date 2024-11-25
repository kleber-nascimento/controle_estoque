from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from scripts.init_db import init_db
#import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

# Importando as rotas
from routes.home import home
from routes.auth import auth_bp
#from routes.user_bp import user_bp

# Registrando as rotas
app.register_blueprint(home)
app.register_blueprint(auth_bp)
#app.register_blueprint(user_bp, url_prefix="/api")

# Banco de Dados: Verifica se já existe BD criado e Inicializa
#with app.app_context():
#    if not os.path.exists('database.db'):
#        init_db()

if __name__ == '__main__':
    app.run(debug=True)