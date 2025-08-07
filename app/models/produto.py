from bson import ObjectId

def novo_produto(nome, preco, estoque, fornecedor_id):
    return {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "fornecedor_id": ObjectId(fornecedor_id)
    }
