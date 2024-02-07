import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")  # Test if state_id attribute is initialized correctly
        self.assertEqual(city.name, "")       # Test if name attribute is initialized correctly

    def test_set_attributes(self):
        city = City()
        city.state_id = "state_123"
        city.name = "New York"
        self.assertEqual(city.state_id, "state_123")  # Test if state_id attribute can be set correctly
        self.assertEqual(city.name, "New York")        # Test if name attribute can be set correctly

if __name__ == '__main__':
    unittest.main()
