from app.db import clientes

def listar_clientes():
    return list(clientes.find())

def cadastrar_cliente(dados):
    cliente = {
        "nome": dados["nome"],
        "cpf": dados["cpf"],
        "email": dados["email"],
        "enderecos": [dados["endereco"]],
        "telefones": [dados["telefone"]]
    }
    clientes.insert_one(cliente)

def deletar_cliente(id_cliente):
    clientes.delete_one({"_id": id_cliente})
