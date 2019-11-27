# File to create the database and fill it with the original 'PEOPLE' data

import os
from config import db
from models import Person


# Data to initialize the database with
PEOPLE = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Leonardo", "lname": "Cordeiro"},
    {"fname": "Leonardo", "lname": "Garcia"},
    {"fname": "Luma", "lname": "Marcatti"}
]


# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    # Create a Person object from Person model for each loop
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()
# Only after the db.session.commit() that the session actually interacts with the database
# Before that, nothing happens with our 'people.db' file
