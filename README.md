# Sistema de Controle de Estoque - Cadastro de Usuários  

## Descrição do Sistema  
O **Sistema de Controle de Estoque** é uma aplicação web simples que permite controlar usuários cadastrados. Nesta primeira versão, o sistema oferece funcionalidades para adicionar, visualizar, editar e deletar usuários.  

Atualmente, ele é projetado para ser usado por controladores de estoque de materiais, sendo acessível apenas por administradores para gerenciar dados de usuários, como nome, telefone, e-mail e CPF.  

⚠️ **Nota:** A funcionalidade de controle de produtos será entregue em uma versão futura.  

---

## Tecnologias Utilizadas  
- **Linguagens:** Python, JSON, HTML, CSS  
- **Framework:** Flask  

---

## Como Rodar o Sistema  
### Pré-requisitos  
- Python 3.12.13 instalado  
- Ambiente virtual configurado com `virtualenv`  

---

### Instruções  
1. Clone o repositório para sua máquina local.  
2. Ative o ambiente virtual no diretório raiz do projeto (opcional, mas recomendado).  
3. Execute o arquivo `main.py` na pasta raiz:  
   ```bash
   python main.py
4. Abra o navegador e acesse o endereço exibido no terminal (por padrão, será http://127.0.0.1:5000).

---

## Funcionalidades
### Versão 01
- Adicionar usuários: Permite cadastrar novos usuários com nome, telefone, e-mail e CPF.
- Visualizar usuários: Exibe a lista de usuários cadastrados.
- Editar usuários: Possibilidade de atualizar informações de usuários existentes.
- Deletar usuários: Remove usuários da lista.

---

## Estrutura de Arquivos
```
Controle_Estoque/
│
├── static/               # Arquivos estáticos
│   ├── css/              # Arquivos de estilo
│   │   ├── admin.css
│   │   └── home.css
│   └── imagens/          # Imagens usadas no projeto
│       └── fundo.jpg
│
├── templates/            # Arquivos HTML
│   ├── admin.html
│   ├── login.html
│   └── user.html
│
├── venv/                 # Ambiente virtual (opcional)
├── main.py               # Arquivo principal para executar o sistema
├── README.md             # Documentação do sistema
└── users.json            # Base de dados em JSON para os usuários
```
---

## Contribuições
- O repositório é público, e contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias ou compartilhar dicas para aprendizado e desenvolvimento contínuo.

---

## Licença
- Este projeto não possui licença de uso.