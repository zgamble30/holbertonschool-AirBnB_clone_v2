from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from .base import Base


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    city_id = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', back_populates='place')
    amenities = relationship('PlaceAmenity', back_populates='place', cascade='all, delete, delete-orphan')
    city = relationship('City', back_populates='places')

    def __repr__(self):
        return f"<Place(name='{self.name}', owner_id={self.owner_id}, city_id={self.city_id})>"

