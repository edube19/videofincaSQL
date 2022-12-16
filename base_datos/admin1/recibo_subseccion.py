from utils.db_admins import db_admins
class Recibo_subseccion(db_admins.Model):
    _tablename__ = "recibo_subseccion"
    id_subseccion = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    nombre = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    monto = db_admins.Column(db_admins.Double(45),nullable=False,unique = False)
    descripcion = db_admins.Column(db_admins.String(45),nullable=False,unique = False)

    def __init__(self, id_subseccion, nombre, monto,descripcion):
        self.id_subseccion = id_subseccion
        self.nombre = nombre
        self.monto = monto
        self.descripcion = descripcion