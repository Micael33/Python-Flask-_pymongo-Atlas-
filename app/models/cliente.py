def novo_cliente(cpf, nome, email, enderecos: list, telefones: list):
    return {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "telefones": [telefones], 
        "enderecos": [enderecos]  
    }
