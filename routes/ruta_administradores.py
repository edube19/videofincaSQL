from flask import Blueprint, render_template, request, redirect, url_for
from base_datos.administradores.lista import Lista
from utils.db_administradores import db_administradores
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
administradores = Blueprint("administradores", __name__)

@administradores.route("/")
def index():
    return "Lista index"

@administradores.route("/registro", methods=['POST'])
def add_contact():
    user  = request.form['user']
    password = request.form['password']
    data_base = request.form['data_base']
    
    new_administrador = Lista(user, password, data_base)
    
    db_administradores.session.add(new_administrador)
    db_administradores.session.commit()

    engine = create_engine(f'mysql://root:admin@localhost/{data_base}')
    if not database_exists(engine.url):
        create_database(engine.url)

    #print(database_exists(engine.url))
    #print(type(database_exists(engine.url))) es booleano
    return "add_contact()",data_base

@administradores.route("/update")
def update():
    return "update a contact"

@administradores.route("/delete/<id>")
def delete(id):

    contact = Lista.query.get(id)

    db_administradores.session.delete(contact)
    db_administradores.session.commit()

    return "eliminado"

@administradores.route("/about")
def about():
    return "about"




