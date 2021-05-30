from model import User, Admin, BlogPosts, db, connect_to_db

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

def get_user_by_user_id(user_id):
    """ For example:
    >>> get_user_by_id(11)

    [<User 11>]
    """ 
    user_id = User.query.filter_by(user_id = user_id).first()
    
    return user_id

def store_admin(id, admin_name, admin_email, admin_password, status, photo_url):
    """ 
    For example:

    >>> create_user("celestercodes", "celestercodes@gmail.com", "bestcoderever")

    [<User 12>]
    """
    admin = Admin(id=id, admin_name = admin_name, admin_email = admin_email, 
            admin_password = admin_password, status=status, photo_url=photo_url)
    
    db.session.add(admin)
    db.session.commit()
    return admin

def create_blogpost(blog_id, timestamp, title=None, photo_url=None, 
        blogpost=None):

    """ For example:
    >>> create_entry(1, "leaves are green", datetime.now(), "1-5ml", 
    "5-10ml", "eggshells", "70-75", "30-35%", "/static/img/aloe.jpg")

    [<BlogPost 12>] 
    """ 

    new_entry = BlogPosts(blog_id=blog_id, timestamp=timestamp, 
        title=title, photo_url=photo_url, blogpost=blogpost)

    db.session.add(new_entry)
    db.session.commit()
    return new_entry

def get_all_entries():
    """ For example:
    >>> get_all_entries()
    [<GrowLog 1>, <GrowLog 2>, <GrowLog 3>, <GrowLog 4>, <GrowLog 5>, <GrowLog 6>, <GrowLog 7>,
    <GrowLog 8>, <GrowLog 9>, <GrowLog 10>, <GrowLog 11>, <GrowLog 12>] """ 
   
    return BlogPosts.query.all()

def get_entry_by_blog_id(blog_id):
    """ For example:
    >>> get_entry_by_id(2)
    [<GrowLog2>] 
    """ 
    return BlogPosts.query.filter_by(blog_id = blog_id).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
