#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """
    Class States
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:

        @property
        def cities(self):
            """
            Getter for cities related to a state using a FIlEStorage engine
            """
            cities = []
            for city in models.storage.all(City).values():
                if (self.id == city.state_id):
                    cities.append(city)
            return cities

        def close(self):
            """Close session"""
            Session.close()