from app.db import fornecedores

def listar_fornecedores():
    return list(fornecedores.find())

def cadastrar_fornecedor(dados):
    fornecedor = {
        "nome": dados["nome"],
        "produtos_fornecidos": [p.strip() for p in dados["produtos"].split(",")],
        "contato": {
            "email": dados["email"],
            "telefone": dados["telefone"]
        },
        "categorias": [c.strip() for c in dados["categorias"].split(",")]
    }
    fornecedores.insert_one(fornecedor)

def deletar_fornecedor(id_fornecedor):
    fornecedores.delete_one({"_id": id_fornecedor})
