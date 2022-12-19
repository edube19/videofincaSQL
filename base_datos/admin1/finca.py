from utils.db_admins import db_admins
class Finca(db_admins.Model):
    #__bind_key__ = 'two'
    _tablename__ = "finca"
    id = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    admin_id = db_admins.Column(db_admins.Integer,nullable=False,unique=True)
    direccion = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    nombre = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    fecha_creacion = db_admins.Column(db_admins.String(45))
    fecha_modificacion = db_admins.Column(db_admins.String(45))
    total_porc_participacion = db_admins.Column(db_admins.Float(20),nullable=False)

    def __init__(self, id, admin_id, direccion,nombre,fecha_creacion,fecha_modificacion,total_porc_participacion):
        self.id = id
        self.admin_id = admin_id
        self.direccion = direccion
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.total_porc_participacion = total_porc_participacion