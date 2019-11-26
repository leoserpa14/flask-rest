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
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    # Does the person exists already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
        return make_response("{lname} successfully created.".format(lname=lname), 201)
    else:
        abort(406, "Person with last name {lname} already exists or is null".format(lname=lname))


def read_one(lname):
    # Does the person exists in our list?
    if lname in PEOPLE: # Porque aqui é só 'in PEOPLE' e não 'in PEOPLE.keys'? - Porque PEOPLE é um dicionário de dicionários, e os dicionários já retornam as chaves
        # person = PEOPLE[lname] # Isso não funciona
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found.".format(lname=lname)
        )
    return person   


def update(lname, person):
    # 'person' tem que receber um dicionário    
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["lname"] = person.get("lname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, "Person with last name {lname} not found.".format(lname=lname))


def delete(lname):
    # Does the person exists in our list?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response("{lname} successfully deleted".format(lname=lname))
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))
