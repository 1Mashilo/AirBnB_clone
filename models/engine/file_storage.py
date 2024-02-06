import json

class FileStorage:
    """A class for handling file storage of objects in JSON format."""

    # Path to the JSON file
    __file_path = "file.json"

    # Dictionary to store objects
    __objects = {}

    def all(self):
        """
        Retrieve all objects stored in the file storage.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def add_object(self, obj):
        """
        Add a new object to the file storage.

        Args:
            obj: The object to be added to the storage.
        """
        object_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[object_key] = obj

    def save(self):
        """Save the objects to the JSON file."""
        serialized_objects = {}

        # Serialize objects and store them in the dictionary
        for object_key, obj in self.__objects.items():
            serialized_objects[object_key] = obj.to_dict()

        # Write the serialized objects to the JSON file
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Load objects from the JSON file."""
        try:
            with open(self.__file_path, "r", encoding="UTF8") as file:
                # Deserialize JSON data and populate the storage dictionary
                serialized_data = json.load(file)
                for object_key, serialized_obj in serialized_data.items():
                    # Create object instances based on class names and attributes
                    obj_instance = eval(serialized_obj["__class__"])(**serialized_obj)
                    self.__objects[object_key] = obj_instance
        except FileNotFoundError:
            # If the file does not exist, do nothing
            pass

