from utils.db_admins import db_admins
class Propiedad(db_admins.Model):
    #__bind_key__ = 'two'
    _tablename__ = "propiedad"
    idpropiedad = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    tipo_propietario = db_admins.Column(db_admins.Integer,nullable=False,unique=False)
    porcentaje_participacion = db_admins.Column(db_admins.String(45),nullable=False,unique=False)
    numero_deposito = db_admins.Column(db_admins.String(45),nullable=True,unique=True)
    numero_departamento = db_admins.Column(db_admins.String(45),nullable=True,unique=True)
    numero_estacionamiento = db_admins.Column(db_admins.String(45),nullable=True,unique=True)

    def __init__(self, idpropiedad, tipo_propietario, porcentaje_participacion,numero_deposito,numero_departamento,numero_estacionamiento):
        self.idpropiedad = idpropiedad
        self.tipo_propietario = tipo_propietario
        self.porcentaje_participacion = porcentaje_participacion
        self.numero_deposito = numero_deposito
        self.numero_departamento = numero_departamento
        self.numero_estacionamiento = numero_estacionamiento