from flask import Flask
from routes.ruta_finca import finca
from routes.ruta_administradores import administradores
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin@localhost/administradores'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

SQLALCHEMY_BINDS = {
    "meta": "sqlite:////path/to/meta.db",
    "auth": {
        "url": "mysql://localhost/users",
        "pool_recycle": 3600,
    },
}

SQLAlchemy(app)

app.register_blueprint(administradores)
