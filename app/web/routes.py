from flask import Blueprint, render_template, request, redirect, flash
from app.controllers import cliente_controller, fornecedor_controller, produto_controller
from bson import ObjectId

web = Blueprint("web", __name__)

@web.route("/")
def index():
    return render_template("index.html")

@web.route("/produtos", methods=["GET", "POST"])
def produtos_view():
    from app.db import produtos, fornecedores
    if request.method == "POST":
        produtos.insert_one({
            "nome": request.form["nome"],
            "preco": float(request.form["preco"]),
            "estoque": int(request.form["estoque"]),
            "tags": [tag.strip() for tag in request.form["tags"].split(",")],
            "fornecedor_id": ObjectId(request.form["fornecedor_id"])
        })
        flash("✅ Produto cadastrado com sucesso!")
        return redirect("/produtos")

    busca = request.args.get("q")
    if busca:
        lista = list(produtos.find({"nome": {"$regex": busca, "$options": "i"}}))
    else:
        lista = list(produtos.find())

    fornecedores_lista = list(fornecedores.find())
    return render_template("produtos.html", produtos=lista, fornecedores=fornecedores_lista)


@web.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        cliente_controller.cadastrar_cliente(request.form)
        return redirect("/clientes")
    
    lista = cliente_controller.listar_clientes()
    return render_template("clientes.html", clientes=lista)

@web.route("/fornecedores", methods=["GET", "POST"])
def fornecedores():
    if request.method == "POST":
        fornecedor_controller.cadastrar_fornecedor(request.form)
        return redirect("/fornecedores")
    
    lista = fornecedor_controller.listar_fornecedores()
    return render_template("fornecedores.html", fornecedores=lista)

# ======================== PRODUTOS ========================

@web.route("/produtos/editar/<id>", methods=["GET", "POST"])
def editar_produto(id):
    from app.db import produtos, fornecedores

    if request.method == "POST":
        produtos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nome": request.form["nome"],
                "preco": float(request.form["preco"]),
                "estoque": int(request.form["estoque"]),
                "tags": [tag.strip() for tag in request.form["tags"].split(",")],
                "fornecedor_id": ObjectId(request.form["fornecedor_id"])
            }}
        )
        flash("✅ Produto atualizado com sucesso!")
        return redirect("/produtos")

    produto = produtos.find_one({"_id": ObjectId(id)})
    fornecedores_lista = list(fornecedores.find())
    return render_template("editar_produto.html", produto=produto, fornecedores=fornecedores_lista)

@web.route("/produtos/delete/<id>")
def deletar_produto(id):
    from app.db import produtos
    produtos.delete_one({"_id": ObjectId(id)})
    flash("❌ Produto deletado com sucesso!")
    return redirect("/produtos")


# ======================== CLIENTES ========================

@web.route("/clientes/editar/<id>", methods=["GET", "POST"])
def editar_cliente(id):
    from app.db import clientes
    cliente = clientes.find_one({"_id": ObjectId(id)})

    if request.method == "POST":
        clientes.update_one({"_id": ObjectId(id)}, {
            "$set": {
                "nome": request.form["nome"],
                "cpf": request.form["cpf"],
                "email": request.form["email"],
                "enderecos": [request.form["endereco"]],
                "telefones": [request.form["telefone"]]
            }
        })
        flash("✅ Cliente atualizado com sucesso!")
        return redirect("/clientes")

    return render_template("editar_cliente.html", cliente=cliente)

@web.route("/clientes/delete/<id>")
def deletar_cliente(id):
    from app.db import clientes
    clientes.delete_one({"_id": ObjectId(id)})
    flash("❌ Cliente deletado com sucesso!")
    return redirect("/clientes")


# ======================== FORNECEDORES ========================

@web.route("/fornecedores/editar/<id>", methods=["GET", "POST"])
def editar_fornecedor(id):
    from app.db import fornecedores
    fornecedor = fornecedores.find_one({"_id": ObjectId(id)})

    if request.method == "POST":
        fornecedores.update_one({"_id": ObjectId(id)}, {
            "$set": {
                "nome": request.form["nome"],
                "produtos_fornecidos": [p.strip() for p in request.form["produtos"].split(",")],
                "contato": {
                    "email": request.form["email"],
                    "telefone": request.form["telefone"]
                },
                "categorias": [c.strip() for c in request.form["categorias"].split(",")]
            }
        })
        flash("✅ Fornecedor atualizado com sucesso!")
        return redirect("/fornecedores")

    return render_template("editar_fornecedor.html", fornecedor=fornecedor)

@web.route("/fornecedores/delete/<id>")
def deletar_fornecedor(id):
    from app.db import fornecedores
    fornecedores.delete_one({"_id": ObjectId(id)})
    flash("❌ Fornecedor deletado com sucesso!")
    return redirect("/fornecedores")