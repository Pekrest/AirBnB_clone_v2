#!/usr/bin/python3
"""Defines the City class."""
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from models.base_model import Base
from models.base_model import BaseModel

class City(BaseModel, Base):
    """
    Represents a city for a MySQL database.
    """
     __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
