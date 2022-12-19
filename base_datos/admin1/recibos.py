from utils.db_admins import db_admins
class Recibos(db_admins.Model):
    #__bind_key__ = 'two'
    _tablename__ = "recibos"
    idrecibos = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    year = db_admins.Column(db_admins.Integer,nullable=False,unique=False)
    mes = db_admins.Column(db_admins.Integer,nullable=False,unique=False)
    nombre = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    fecha_modificacion = db_admins.Column(db_admins.String(45))

    def __init__(self,idrecibos,year,mes,nombre,fecha_modificacion):
        self.idrecibos = idrecibos
        self.year = year
        self.mes = mes
        self.nombre = nombre
        self.fecha_modificacion = fecha_modificacion