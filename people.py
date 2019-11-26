from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API

PEOPLE = {
    "Farrell":{
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    }, # key == 'Farrell'

    "Cordeiro":{
        "fname": "Leonardo",
        "lname": "Cordeiro",
        "timestamp": get_timestamp()
    }, # key == 'Cordeiro'

    "Garcia":{
        "fname": "Leonardo",
        "lname": "Garcia",
        "timestamp": get_timestamp()
    }, # key == Garcia .. etc

    "Marcatti":{
        "fname": "Luma",
        "lname": "Marcatti",
        "timestamp": get_timestamp()
    },
}


# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):

    # Does the person exists in our list?
    if lname in PEOPLE: # Porque aqui é só 'in PEOPLE' e não 'in PEOPLE.keys'?
        # person = PEOPLE[lname] # Isso não funciona
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found.".format(lname=lname)
        )

    return person

    


def create():
    pass


def update():
    pass


def delete():
    pass
