import json
from datetime import datetime


class FileStorage:
    """A class to manage storage of objects in a file."""

    def __init__(self, file_path="file.json"):
        """
        Initialize the storage system.

        Args:
            file_path (str, optional): The path to the file where objects are stored. Defaults to "file.json".
        """
        self.__file_path = file_path
        self.__objects = {}  # Dictionary to store objects

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or a filtered list based on class.

        Args:
            cls (class, optional): The class to filter by. Defaults to None (all objects).

        Returns:
            dict or list: A dictionary of all objects or a filtered list based on class.
        """
        if cls is None:
            return self.__objects.copy()
        else:
            return [obj for obj in self.__objects.values() if isinstance(obj, cls)]

    def new(self, obj):
        """
        Adds a new object to the storage system.

        Args:
            obj (BaseModel): The object to add.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Saves the objects in the storage system to a file.
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, default=self.to_dict)

    def reload(self):
        """
        Loads objects from a file into the storage system.
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = self.get_object(value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if itâs inside - if obj is equal to None"""
        try:
            del self.__objects[f"[type(obj) __name__]  [obj id]"]
        except Exception:
            pass

    def get_object(self, obj_dict):
        """
        Instantiates a class from a dictionary representation.

        Args:
            obj_dict (dict): A dictionary representing an object.

        Returns:
            BaseModel: An instantiated object from the dictionary.
        """
        class_name = obj_dict["__class__"]
        from models.base_model import BaseModel
        from models import classes  # Assuming 'classes.py' contains class definitions
        new_obj = classes.get_class(class_name)(**obj_dict)
        new_obj.id = obj_dict["id"]
        new_obj.created_at = datetime.fromisoformat(obj_dict["created_at"])
        new_obj.updated_at = datetime.fromisoformat(obj_dict["updated_at"])
        return new_obj

    def to_dict(self, obj):
        """
        Serializes an object to a dictionary representation.

        Args:
            obj (BaseModel): The object to serialize.

        Returns:
            dict: A dictionary representation of the object.
        """
        obj_dict = obj.__dict__.copy()
        obj_dict["__class__"] = obj.__class__.__name__
        obj_dict["created_at"] = obj.created_at.isoformat()
        obj_dict["updated_at"] = obj.updated_at.isoformat()
        return obj_dict
