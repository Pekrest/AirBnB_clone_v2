#!/usr/bin/python3
"""Defines the State class."""

import models
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import Column
from models.city import City
from sqlalchemy import String
from models.base_model import Base
from models.base_model import BaseModel


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list