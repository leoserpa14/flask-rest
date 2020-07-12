from datetime import datetime
from flask import make_response, abort

from config import db
from models import Person, PersonSchema

# Important: Comment from the tutorial page -> "change XY.data occurences to XY in people.py"


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# # Data to serve with our API
#
# PEOPLE = {
#     "Farrell":{
#         "fname": "Doug",
#         "lname": "Farrell",
#         "timestamp": get_timestamp()
#     }, # key == 'Farrell'

#     "Cordeiro":{
#         "fname": "Leonardo",
#         "lname": "Cordeiro",
#         "timestamp": get_timestamp()
#     }, # key == 'Cordeiro'

#     "Garcia":{
#         "fname": "Leonardo",
#         "lname": "Garcia",
#         "timestamp": get_timestamp()
#     }, # key == Garcia .. etc

#     "Marcatti":{
#         "fname": "Luma",
#         "lname": "Marcatti",
#         "timestamp": get_timestamp()
#     },
# }
# UNUSED for part 2 as we put that on a database

# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    """
    # Create the list of people from our data
    people = Person.query.order_by(Person.lname).all()

    # Serialize the data for the response
    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people)

    return data


def create(person):
    lname = person.get("lname")
    fname = person.get("fname")

    existing_person = Person.query.filter(Person.fname==fname).filter(Person.lname==lname).one_or_none()

    # Does the person exists already?
    if existing_person is None:
        
        # Create a person instance using the schema and the passed-in person
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session)

        # Add the person to the database
        db.session.add(new_person)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_person)
        return data, 201

    else:
        abort(409, "Person {fname} {lname} already exists".format(fname=fname, lname=lname))


def read_one(person_id):

    # Get the person requested
    person = Person.query.filter(Person.person_id == person_id)
        .outerjoin(Note)
        .one_or_none()

    # Did we find a person?
    if person is not None:

        # Serialize the data for the response
        person_schema = PersonSchema() # many=False as default
        data = person_schema.dump(person)
        return data
    
    # Else, if we didn't find that person
    else:
        abort(
            404, "Person with ID: {person_id} not found.".format(person_id=person_id)
        )


def update(person_id, person):

    # Get the person requested from the db into session
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()

    # Try to find an existing person with the same name as the update
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    # Are we trying to find a person that does not exist?
    if update_person is None:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=person_id),
        )

    # Would our update create a duplicate of another person already existing?
    elif (
        existing_person is not None and existing_person.person_id != person_id
    ):
        abort(
            409,
            "Person {fname} {lname} exists already".format(
                fname=fname, lname=lname
            ),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = PersonSchema()
        update = schema.load(person, session=db.session)

        # Set the id to the person we want to update
        update.person_id = update_person.person_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person)

        return data, 200

def delete(person_id):

  # Get the person requested
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # Did we find a person?
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(
            "Person {person_id} deleted".format(person_id=person_id), 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=person_id),
        )

# IMPORTANTE: Desse jeito que a lista foi montada, se eu utilizar a função 'update' em 'Leonardo Cordeiro' por exemplo, eu vou
# pesquisar pela chave do dicionário que está meu nome, ou seja, vou fazer o request procurando 'Cordeiro', agora se eu mudar 
# o meu sobrenome com a função update, para 'Leonardo Serpa' por exemplo, esse nome ainda vai estar vinculado à 'Cordeiro', pois
# essa é a chave do dicionário do meu nome, isso não vai mudar para 'Serpa'.


# Arquivo vai ter que ser alterado para se adaptar à parte 2 do tutorial, com leitura de dados na database através do SQLite3