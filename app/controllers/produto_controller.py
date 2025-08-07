from app.db import produtos
from bson.regex import Regex

def listar_produtos(filtro_nome=None):
    if filtro_nome:
        return list(produtos.find({"nome": Regex(filtro_nome, "i")}))
    return list(produtos.find())

def cadastrar_produto(dados):
    produto = {
        "nome": dados["nome"],
        "preco": float(dados["preco"]),
        "estoque": int(dados["estoque"]),
        "tags": [t.strip() for t in dados["tags"].split(",")]
    }
    produtos.insert_one(produto)

def deletar_produto(id_produto):
    produtos.delete_one({"_id": id_produto})
