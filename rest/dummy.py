import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from base64 import b64encode

engine = create_engine('sqlite:///users.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("python", b64encode("python"), "administrator", "address", "123123123")
session.add(user)

#user = User("python", "python", "hello", "Hello", "hello")
#session.add(user)

#user = User("jumpiness", "python", "hello", "Hello", "hello")
#session.add(user)

# commit the record the database
session.commit()

session.commit()