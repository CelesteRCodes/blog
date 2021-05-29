from model import User, db, connect_to_db

def create_user(username, email, password):
    """ 
    For example:

    >>> create_user("celestercodes", "celestercodes@gmail.com", "bestcoderever")

    [<User 12>]
    """
    user = User(username = username, email = email, password = password)
    
    db.session.add(user)
    db.session.commit()
    return user

    # can have function that deletes user (for when they want to deactivate their profile)
    # will also have to ensure it deletes all the user's data in db like the plants/entries

def get_user_by_username(username):
    """ For example:
    >>> get_user_by_username("celestercodes")

    [<User 12>]
    """ 
    return User.query.filter_by(username=username).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
