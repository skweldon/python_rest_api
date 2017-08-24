#Used to set the initial database up. We have the id, username, password, email, address and phone

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String,unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    address = Column(String)
    phone = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, username, password, email, address, phone):
        """"""
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone = phone


# create tables
Base.metadata.create_all(engine)