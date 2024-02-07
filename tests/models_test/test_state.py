import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_initialization(self):
        state = State()
        self.assertEqual(state.name, "")  # Test if the name attribute is initialized correctly

    def test_set_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")  # Test if the name attribute can be set correctly

if __name__ == '__main__':
    unittest.main()
