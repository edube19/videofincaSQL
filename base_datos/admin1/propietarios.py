from utils.db_admins import db_admins
class Propietarios(db_admins.Model):
    #__bind_key__ = 'two'
    _tablename__ = "propietarios"
    idpropietarios = db_admins.Column(db_admins.Integer, primary_key=True,nullable=False)
    nombres_y_apellidos = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    tipodocumento = db_admins.Column(db_admins.String(45),nullable=False,unique=False)
    nro_documento = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    correo = db_admins.Column(db_admins.String(45),nullable=False,unique=True)
    telefono = db_admins.Column(db_admins.Integer,nullable=True,unique=False)
    fecha_creacion = db_admins.Column(db_admins.String(45))
    fecha_modificacion = db_admins.Column(db_admins.String(45))
    estado = db_admins.Column(db_admins.String(45),nullable=False,unique=False)
    def __init__(self, idpropietarios, nombres_y_apellidos, tipodocumento,nro_documento,correo,telefono,fecha_creacion,fecha_modificacion,estado):
        self.idpropietarios = idpropietarios
        self.nombres_y_apellidos = nombres_y_apellidos
        self.tipodocumento = tipodocumento
        self.nro_documento = nro_documento
        self.correo = correo
        self.telefono = telefono
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.estado = estado