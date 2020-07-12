# flask-rest
Flask REST API again

Originally tried to do a FLASK RESTFUL API, problem is that the migrate function crashed the cmd prompt.
Then I tried with Django, discovered that the problem was not that Flask crashed, but Postgresql crashed. Turns out that the Django tutorial I was following was incomplete, so I decided to start a REST API with Flask again, this time with Sqlite3 as a database.


Part 1: Created the REST Api with CRUD applications. Learned to build GET POST PUT DELETE requests with swagger.yml. Learned to use the Swagger UI, and then finally build a web page that makes use of the REST API requests that we build with swagger. - "pip install flask" and "pip install connexion[swagger-ui]" were the packages needed for this part.
https://realpython.com/flask-connexion-rest-api/

Part 2: Going to create a database to store our data with SQLAlchemy and Marshmallow - "pip install Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow" are the packages we'll need to install. At the moment, our data is being stored internally in a dict variable that resets everytime we run the server again. We're going to use SQLite, which is supposed to come with the python installation.
What SQLAlchemy does is it allows us to use object oriented programming, so instead of receiving the data of our database as lists of lists (tuples inside tuples), we actually get objects. For example, if we have a 'people' database, once we ask for a specific part of the db, we will get 'person' objects, which have their own attributes, a 'person' object can have 'lname' and 'fname' attributes for instance. OBS: SQLAlchemy already sanitizes our data automatically. 
Marshmallow is the responsible for the serialization an deserialization of our data, which means converting python objects into simpler structures that can be parsed into json, and vice-versa. Marshmallow does this through 'Schemas'.
After putting our data into a real database with SQLite3, we're gonna have to change the way we do our requests to our API. For example:
before we had "/api/people/{lname}", now, we're gonna use the primary keys of our database to get the object we want, using "/api/people/{person_id}" in our URL.
Important: With the latest flask-sqlalchemy module, everytime I tried to make a request for the API, I would get a KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'. Found in StackOverflow that if I installed the version 2.1.0 of flask-sqlalchemy the problem would go away, which it did, but ideally I would find the source of the problem and use the latest version of the package. #TODO
https://realpython.com/flask-connexion-rest-api-part-2/

Part 3: This part teaches how to set relations between different tables and why this is important, teaching us the relational database concept. So we created a second table of "notes" which any kind of "people" object may or may not have. It's a one-to-many relationship.
https://realpython.com/flask-connexion-rest-api-part-3/


