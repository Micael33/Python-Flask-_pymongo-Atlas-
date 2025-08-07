from flask import Flask
from app.web.routes import web
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

template_dir = os.path.join(BASE_DIR, 'app', 'web', 'templates')
static_dir = os.path.join(BASE_DIR, 'app', 'web', 'static')  # Aqui está a mágica

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = "mongodb+srv://micaeld081:Micael123@cluster0.xfh9oqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

app.register_blueprint(web)

if __name__ == "__main__":
    app.run(debug=True)
