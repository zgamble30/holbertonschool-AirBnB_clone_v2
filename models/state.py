from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models import storage


class State(BaseModel):
    """
    State class
    """
    name = ""

    # New code added
    @property
    def cities(self):
        """getter attribute that returns the list of City instances"""
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

    @property
    def places(self):
        """getter attribute that returns the list of Place instances"""
        place_list = []
        for place in storage.all(Place).values():
            if place.city.state_id == self.id:
                place_list.append(place)
        return place_list

    def __init__(self, *args, **kwargs):
        """
        Constructor for State class
        """
        super().__init__(*args, **kwargs)
