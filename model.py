from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """Users table."""

    __tablename__ = "users"

    id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=True,
                       )
    username = db.Column(db.String(50), nullable=False, unique=True,)
    email = db.Column(db.String(100), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False,)
    
# making the class User and Users table
# id is the primary key, it autoincrements with each new user
# column names = id, user_name, email, password
# only user_name and email have to be unique
# all columns must have values, no NULL



def connect_to_db(flask_app, db_uri='postgresql:///blog', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app