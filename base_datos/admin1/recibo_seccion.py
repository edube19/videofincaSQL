from utils.db_admins import db_admins
class Recibo_seccion(db_admins.Model):
    _tablename__ = "recibo_seccion"
    idseccion = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    descripcion = db_admins.Column(db_admins.String(45),nullable=False,unique=False)

    def __init__(self, idseccion, descripcion):
        self.idseccion = idseccion
        self.descripcion = descripcion