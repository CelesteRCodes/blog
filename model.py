from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """Users table."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=True,
                       )
    username = db.Column(db.String(50), nullable=False, unique=True,)
    email = db.Column(db.String(100), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False,)
    user_comment = db.Column(db.String(150), nullable=True)
    

class Admin(db.Model):
    """Admin table."""

    __tablename__ = "admin"

    id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=False,
                       )
    admin_name = db.Column(db.String(50), nullable=False, unique=True,)
    admin_email = db.Column(db.String(100), nullable=False, unique=True,)
    admin_password = db.Column(db.String(50), nullable=False,)
    status = db.Column(db.String(250), nullable=True,)
    photo_url = db.Column(db.String, nullable=True)

    # blogposts = db.relationship("BlogPosts", backref = "blogposts")

class BlogPosts(db.Model):
    """Blog post table."""

    __tablename__ = "blogposts"

    blog_id = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )
    admin_id = db.Column(db.Integer,
                        db.ForeignKey("admin.id"),
                        )
    
    timestamp = db.Column(db.DateTime)
    title = db.Column(db.String(250), nullable=True,)
    photo_url = db.Column(db.String, nullable=True,)
    blogpost = db.Column(db.String(2500), nullable=True)
    
    # admin = db.relationship("Admin", backref = "admin")



def connect_to_db(flask_app, db_uri='postgresql:///blog', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app