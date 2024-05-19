#!/usr/bin/python3
"""Defines the amenity class."""

from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
from models.base_model import Base
from models.base_model import BaseModel


class Amenity(BaseModel, Base):
    """
    Represents an Amenity for a MySQL database.
    """
     __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
