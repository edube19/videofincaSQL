from app import app
from utils.db_administradores import db_administradores

db_administradores.init_app(app)
with app.app_context():
    db_administradores.create_all()

if __name__ == "__main__":
    app.run(debug=True)