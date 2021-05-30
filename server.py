from flask import Flask, render_template, request, redirect, session

# import cloudinary.uploader

# from datetime import datetime

from jinja2 import StrictUndefined

import flash

import crud
import model
import os

app = Flask(__name__)
# CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
# CLOUDINARY_KEY_SECRET = os.environ['CLOUDINARY_SECRET']
app.secret_key = 'celesteisprosperous'


@app.route('/')
def show_homepage():
    """Show homepage."""

    return render_template('home.html')

    # shows homepage with login form, add new user button,
    # and forgot password button


@app.route('/login', methods=['GET', 'POST'])
def show_login():
    """ Show login for user on homepage."""

    username = request.form.get('username')
    password = request.form.get('password')
    user = crud.get_user_by_username(username)
    
    if user and password == user.password:
        session["id"] = username
        return redirect('/show-blog-posts-page')
    else:
        return redirect('/') 

        # function for the 'submit' button for login form

        # if user and password from session (entered by user)
        # is in the database, the user plants page will be 
        # loaded for that user

        # if the user and password entered is not stored 
        # in the database, the homepage with the login form 
        # will be loaded for the user to try again or to 
        # register a new user


# should have an admin log in function where the blog-base.html has an option to add posts (a long comment)
# can add a table to model.py for blog posts
    # columns: post/comment, timestamp, title

@app.route('/show-forgotpw', methods=['GET', 'POST'])
def show_forgotpw():
    """ Show form to retrieve user's info."""

    return render_template("/forgotpw.html")

    # function to show forgot password page 

    # where user can enter their information for password retrieval



# @app.route('/process-forgotpw', methods=['GET', 'POST'])
# def process_forgotpw():
#     """ Process new user form."""
    
    # if "email" in session:
    #     email = session["email"]
    #     user_email = CRUD.get_user_by_email(email)
    #     if user_email == None:
    #         return redirect("/")
    
    # return redirect("/")

# function that processes form from forgot password page

# currently, just redirecting user back to homepage after 
# clicking submit on the form

@app.route('/show-new-user-form', methods=['GET', 'POST'])
def show_new_user_form():
    """ Show form to create a new user."""

    return render_template("/new-user.html")

# function that shows the add new user page 

# where the user can enter their info to register a new profile

@app.route('/process-new-user-form', methods=['GET', 'POST'])
def process_new_user_form():
    """ Process new user form."""

    if "username" not in session:
        

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        crud.create_user(username, email, password)
    
    return redirect("/login")

# function that processes the add new user form, creating new user in users table
# after user clicks submit on the page

@app.route('/show-blog-posts-page')
def show_blog_posts_page():
    """Show blog posts page."""

# will need crud function like get_blog_posts but only wanting to show one post (most recent)
# then links for the older ones

    return render_template('blog-base.html')

@app.route('/show-about-me')
def show_about_me():
    """Show creator's about me page."""

    return render_template('about-me.html')

@app.route('/show-tarot-page')
def show_tarot_page():
    """Show tarot page."""

    return render_template('tarot.html')

    # will need another route possibly to process any
    # comments from user entered in the form on tarot page (pending)

@app.route('/show-booking-page')
def show_booking_page():
    """Show booking page."""

    return render_template('booking.html')

    # will need another route to process the booking form 


if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')
