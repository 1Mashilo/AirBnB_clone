import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_attributes(self):
        """Test if the BaseModel object has the correct attributes"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_generation(self):
        """Test if the id attribute is generated correctly"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_at_and_updated_at(self):
        """Test if created_at and updated_at attributes are datetime objects"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute"""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns a dictionary representation"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()

