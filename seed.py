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


usernames = ["moon_baby1", "overthemoon", 
            "bluemoon"]

passwords = ["1234", "1111", "4444"]

emails = ["moonbaby1@gmail.com", "testmoon@gmail.com", 
             "444@gmail.com"]

for n in range(3):
    email = f'user{n}@test.com'  
    password = 'test'
    username = f'username{n}'
    # variables to pass into CRUD.create_user

    user = crud.create_user(username=username, 
        email=email, password=password)



admin_name = 'thee_cellestial'
admin_email = 'cellesstialbechanneling@gmail.com' 
admin_password = '12345'
status = 'blessed and highly favored'
photo_url = '/static/img/purplestars.jpg'

    # variables to pass into CRUD.create_user

admin = crud.store_admin(admin_name=admin_name, admin_email=admin_email, 
        admin_password=admin_password, status=status, photo_url=photo_url)



blog_ids = [1, 2, 3]

timestamps = datetime.now()

titles = ["Moondays: My Born Day", "Say Hi to Mama Moon tonight", 
            "How To: Moon Water"]

photo_urls =  ["/static/img/cosmos.jpg",
               "/static/img/eyecosmos.jpg",
               "/static/img/purplestars.jpg"]

blogposts = ["don't forget your moon water, loves", 
            "take a pic of the moon tonight", 
            "my moon sign and how it's expression"]


for n in range(3):

    blog_id = choice(blog_ids)
    timestamp = datetime.now()
    title = choice(titles)
    photo_url = choice(photo_urls)
    blogpost = choice(blogposts)

    new_entry = crud.create_blogpost(blog_id=blog_id, timestamp=timestamp, 
        title=title, photo_url=photo_url, blogpost=blogpost)



