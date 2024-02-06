#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """Base model class for other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Constructor method for BaseModel"""

        if kwargs:
            # If keyword arguments are provided during object instantiation
            for key, value in kwargs.items():
                # Loop through each key-value pair in kwargs

                # Convert string representation of created_at to datetime object
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                # Convert string representation of updated_at to datetime object
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                # Set attributes of the object excluding __class__
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # If no keyword arguments are provided during object instantiation
            self.id = str(uuid.uuid4())  # Unique id for the object
            self.created_at = datetime.now()  # Date and time when the object is created
            self.updated_at = datetime.now()  # Date and time when the object is last updated
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime and save the object"""
        self.updated_at = datetime.now() # Update the updated_at attribute
        models.storage.save()

    def to_dict(self):        
        """Return a dictionary representation of the object"""

        # Create a copy of the object's dictionary attributes
        dict_copy = self.__dict__.copy()

        # Convert created_at and updated_at attributes to string in ISO format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        # Add the class name to the dictionary
        dict_copy['__class__'] = self.__class__.__name__

        return dict_copy
