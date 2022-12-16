from flask import Blueprint, render_template, request, redirect, url_for
from base_datos.admin1.finca import Finca
from utils.db_admins import db_admins

finca = Blueprint("finca", __name__)

@finca.route("/")
def index():
    return "Lista index"

@finca.route("/new", methods=['POST'])
def add_contact():
    admin_id  = request.form['admin_id']
    direccion = request.form['direccion']
    nombre = request.form['nombre']
    fecha_creacion = request.form['fecha_creacion']
    fecha_modificacion = request.form['fecha_modificacion']
    total_porc_participacion = request.form['total_porc_participacion']
    new_finca = Finca(admin_id, direccion,nombre,fecha_creacion,fecha_modificacion,total_porc_participacion)
    
    db_admins.session.add(new_finca)
    db_admins.session.commit()

    return "add_contact()"

@finca.route("/update")
def update():
    return "update a contact"

@finca.route("/delete/<id>")
def delete(id):

    contact = Finca.query.get(id)

    db_admins.session.delete(contact)
    db_admins.session.commit()

    return "eliminado"

@finca.route("/about")
def about():
    return "about"


