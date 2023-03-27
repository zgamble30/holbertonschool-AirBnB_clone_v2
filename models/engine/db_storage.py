#!/usr/bin/python3
"""Defines the DBStorage class."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound


class DBStorage:
    """Interacts with the MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(env['HBNB_MYSQL_USER'],
                                              env['HBNB_MYSQL_PWD'],
                                              env['HBNB_MYSQL_HOST'],
                                              env['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session."""
        objects = {}
        classes = [BaseModel]
        if cls is not None:
            classes = [cls] if isinstance(cls, type) else cls
        for c in classes:
            for obj in self.__session.query(c):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
