import os
from datetime import datetime
from random import choice, randint

import crud
import model
import server

os.system('dropdb project')
os.system('createdb project')
# creates and deletes databases

model.connect_to_db(server.app)
# runs like python3 model.py

model.db.create_all()
# creates db tables


# usernames = ["moon_baby1", "overthemoon", 
#             "bluemoon"]
# numbers = ["one", "two", "three", "four", "five"]
# passwords = ["1234", "1111", "4444"]

# emails = ["moonbaby1@gmail.com", "testmoon@gmail.com", 
#              "444@gmail.com"]

# for n in range(3):
email = 'user@test.com'  
password = 'test'
username = 'testuser'
    # variables to pass into CRUD.create_user

user = crud.create_user(username=username, 
        email=email, password=password)


# ids = [1, 2, 3, 4]
# admin_names = ['thee_cellestial', 'empress_celeste', 
#             'thee high priestess']
# admin_emails = ['cellesstialbechanneling@gmail.com',
#             'celestial@gmail.com', 'celeste@gmail.com']
# admin_passwords = ['12345', '111', '2222']
# statuses = ['blessed and highly favored', 'finding balance', 
#             'attitude of gratitude']
# admin_photo_urls = ["/static/img/cosmos.jpg",
#                "/static/img/eyecosmos.jpg",
#                "/static/img/purplestars.jpg"]


# for n in range(3):
id = 1
admin_name = 'empress_celeste'
admin_email = 'cellesstialbechanneling@gmail.com'
admin_password = '2222'
status = 'attitude of gratitude'
photo_url = '/static/img/eyecosmos.jpg'

    # variables to pass into CRUD.create_user

admin = crud.store_admin(id=id, admin_name=admin_name, admin_email=admin_email, 
        admin_password=admin_password, status=status, photo_url=photo_url)



# blog_ids = [1, 2, 3]

# timestamps = datetime.now()

# titles = ["Moondays: My Born Day", "Say Hi to Mama Moon tonight", 
#             "How To: Moon Water"]

# photo_urls =  ["/static/img/cosmos.jpg",
#                "/static/img/eyecosmos.jpg",
#                "/static/img/purplestars.jpg"]

# blogposts = ["don't forget your moon water, loves", 
#             "take a pic of the moon tonight", 
#             "my moon sign and how it's expression"]


# for n in range(3):

blog_id = 3
timestamp = datetime.now()
title = 'Moondays: My Born Day'
photo_url = '/static/img/cosmos.jpg'
blogpost = 'fasting on my born day which is moon day'

new_entry = crud.create_blogpost(blog_id=blog_id, timestamp=timestamp, 
        title=title, photo_url=photo_url, blogpost=blogpost)



