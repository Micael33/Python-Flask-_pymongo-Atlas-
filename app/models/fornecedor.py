def novo_fornecedor(nome, produtos: list, contato: dict, categorias: dict):
    return {
        "nome": nome,
        "produtos": [produtos],
        "contato": {
            "telefone": contato.get("telefone"),
            "email": contato.get("email")
        },
        "lista_categorias": {
            0: categorias.get("categoria1"),
            1: categorias.get("categoria2"),
        }
    }