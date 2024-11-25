# Importa o BD do arquivo models.py
export PYTHONPATH=$PYTHONPATH:~/Documents/senai/controle_estoque/backend
from ..models import init_db

# Inicializa o Banco de Dados
init_db()

# Imprime a msg na tela para identificar Sucesso na execução do BD
print("Banco de Dados inicializado com sucesso")