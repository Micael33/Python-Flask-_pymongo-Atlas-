# Projeto Flask com MongoDB Atlas via PyMongo

Este projeto implementa um sistema de gerenciamento de clientes, produtos e fornecedores usando:
- Python + Flask
- MongoDB Atlas com PyMongo
- Interface Web simples (HTML + CSS)

## Estrutura
- CRUD completo para cada entidade
- Integração com Atlas
- Web frontend com templates

## 📌 Funcionalidades

- Cadastro, listagem, atualização e remoção de:
  - Clientes
  - Fornecedores
  - Produtos (com chave estrangeira para fornecedores)
- Sistema de busca por nome
- Interface estilizada com HTML + CSS (efeito vidro)
- Organização por rotas e Blueprints do Flask

## Como rodar
1. Crie seu ambiente virtual
2. Instale as dependências:
   pip install -r requirements.txt
3. Execute:
   python main.py
