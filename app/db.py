from pymongo import MongoClient



uri = "mongodb+srv://micaeld081:Micael123@cluster0.xfh9oqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client['md_produtos']


clientes = db.clientes
fornecedores = db.fornecedores
produtos = db.produtos

