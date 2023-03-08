from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    place_amenities = relationship('PlaceAmenity', back_populates='amenity')

    def __repr__(self):
        return f"<Amenity(name='{self.name}')>"

