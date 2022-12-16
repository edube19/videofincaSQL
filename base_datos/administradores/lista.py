from utils.db_administradores import db_administradores

class Lista(db_administradores.Model):
    _tablename__ = "lista"
    id = db_administradores.Column(db_administradores.Integer, nullable=False,primary_key=True)
    user = db_administradores.Column(db_administradores.String(100),nullable=False,unique=True)
    password = db_administradores.Column(db_administradores.String(100),nullable=False)
    data_base = db_administradores.Column(db_administradores.String(20),nullable=False,unique=True)

    def __init__(self, user, password, data_base):
        self.user = user
        self.password = password
        self.data_base = data_base
