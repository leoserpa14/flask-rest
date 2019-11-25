from datetime import datetime

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
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
